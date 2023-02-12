import pymysql, logging
from common.conf import Conf

logging.basicConfig(level=logging.DEBUG)


# 读sql 语句的函数
def read_sqls(sqlfile):
    '''功能：读取sqlfile 文件中的sql语句'''
    try:
        sqlfile = '../initsqls/' + sqlfile
        file = open(sqlfile, encoding='utf-8')

        sqls = []
        for sql in file:
            if sql.strip() and sql.strip()[:2] != '--':
                sqls.append(sql.strip())
        logging.debug(f'读取sql数据成功{sqlfile}')
        return sqls
    except BaseException as e:
        logging.error(f'读取sql数据出错{sqlfile}：{e}')
        exit()


# 数据库类
class DB:
    def __init__(self):
        '''功能：连接数据库  成员变量：数据库连接对象、游标'''
        try:
            dbinfo = Conf().get_dbonfo()
            self.__conn = pymysql.connect(**dbinfo)
            self.__cursor = self.__conn.cursor()
            logging.debug(f'数据库连接成功{dbinfo}成功')
        except BaseException as e:
            logging.error(f'数据库连接成功{dbinfo}出错：{e}')
            exit()

    def init_db(self, sqlfile):
        '''功能：执行sqlfile所有语句，实现数据库初始化'''
        try:
            sqls = read_sqls(sqlfile)
            for sql in sqls:
                self.__cursor.execute(sql)
            self.__conn.commit()
            self.__conn.close()
            logging.debug(f'数据库执行{sqlfile}语句，初始化成功')
        except BaseException as e:
            logging.error(f'数据库执行{sqlfile}语句，初始化出错{e}')
            exit()

    def check_db(self, case_info, tables, args, check_sql, db_expect):
        '''功能：执行sqlfile所有语句，实现数据库验库'''
        try:
            self.__cursor.execute(check_sql)
            db_actlual = self.__cursor.fetchone()
            if db_actlual == db_expect:
                passed,msg =True ,""#给pytest用
                logging.info(f'数据库执行{case_info}语句验库成功')#测试通过用info
            else:
                passed, msg = False, f"{case_info}==验库失败，检查表{tables}中，参数为{args}的\n\t预期{db_expect}\n\t实际{db_actlual}语句"
                logging.warning(msg)
            return passed,msg
        except BaseException as e:
             # 给pytest用
            logging.error(f'数据库执行{case_info}，检查表{tables}中，参数为{args}的{check_sql}语句验库出错{e}')
            exit()


if __name__ == '__main__':
    # DB().init_db('longin.sql')
    # DB().init_db('signup.sql')
    DB().check_db('随便用例','随便用例的数据','随便用例的表名',"select count(*) from users",(7,0))

# 构造方法：连接数据库，把数据库连接对象和游标存入成员变量

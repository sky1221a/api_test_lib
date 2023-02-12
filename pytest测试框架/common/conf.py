# 创建类conf
# 构造方法：用于创建配置对象，读配置文件，将配置对象做成私有成员变量
import configparser, logging

logging.basicConfig(level=logging.DEBUG)


class Conf:
    def __init__(self):
        '''功能：创建配置对象，读配置文件到对象中'''
        try:
            self.__conf = configparser.ConfigParser()
            file = '../conf/server.conf'
            self.__conf.read(file, encoding='utf-8')

            if self.__conf.sections():  # 这句话的意思：如果conf中存有节点名(成功)，不是空列表(空列表在if后面相当于False)
                logging.debug(f'读配置文件{file}成功')
            else:
                logging.error(f'读配置文件出错：请检查文件名{file}是否正确')
                exit()  # 退出测试
        except BaseException as e:
            logging.error(f'读配置文件{file}出错：{e}')

    def get_sever_info(self):
        '''功能：读接口服务器信息方法 ，返回值：形如http://ip:port的字符串'''
        try:
            which_server = 'api_server'
            ip = self.__conf.get(which_server, 'ip')
            port = self.__conf.get(which_server, 'port')
            base_url = f'http://{ip}:{port}'
            logging.debug(f'获取接口服务器信息{base_url}成功')
            return base_url
        except BaseException as e:
            logging.debug(f'获取接口服务器信息出错:{e}')
            exit()

    def get_dbonfo(self):
        '''功能 获取数据库服务信息，返回值数据库信息字典'''
        try:
            which_server = "db_server"
            host = self.__conf.get(which_server, 'host')
            db = self.__conf.get(which_server, 'db')
            user = self.__conf.get(which_server, 'user')
            passwd = self.__conf.get(which_server, 'passwd')
            db_info = {'host': host, 'db': db, 'user': user, 'passwd': passwd}
            logging.debug(f'获取数据库信息{db_info}成功')
            return db_info
        except BaseException as e:
            logging.debug(f'获取数据库信息出错:{e}')
            exit()


if __name__ == '__main__':
    a = Conf()


import pandas, logging, requests
from common.conf import Conf

logging.basicConfig(level=logging.DEBUG)


def read_cases(xlsfile, columns=None, eval_cols=None):
    try:
        file = '../data/' + xlsfile
        data = pandas.read_excel(file, usecols=columns)
        case_info = data['用例编号'] + '-' + data['用例标题']
        base_url = Conf().get_sever_info()
        url = base_url + data['接口路径']
        data.insert(0, '用例信息', case_info)
        data.insert(1, '接口地址', url)
        del data['用例编号'], data['用例标题'], data['接口路径']
        for col in eval_cols:
            data[col] = data[col].apply(eval)
        cases = data.values.tolist()
        logging.debug(f'读取并处理文件{xlsfile}成功')
        return cases
    except BaseException as e:
        logging.error(f'读取并处理文件{xlsfile}出错')
        exit()


def send_request(url, method, args_type, args):
    try:
        send1 = f"requests.{method}('{url}',{args_type}={args})"
        res = eval(send1)
        actual = res.json()
        logging.debug(f'请求地址{send1}成功')
        return actual
    except BaseException as e:
        logging.error(f'请求地址{send1}出错了{e}')
        exit()
def check(case_info,actual,expect):
    try:
        if actual == expect:
            passed,msg = True,''
            logging.info(f'{case_info}+++通过++')

        else:
            passed, msg = False, f"{case_info}==响应比对失败，\n\t预期{expect}\n\t实际{actual}"
            logging.warning(msg)
        return passed,msg
    except BaseException as e:
        logging.error(f'{case_info}++++出错{e}')


if __name__ == '__main__':
    # check("99999",{'a':1},{'a':2})
    # print(read_cases('api_login.xlsx', ['用例编号', '用例标题', '接口路径', '请求方法', '请求类型', '参数', '预期结果'], ['参数', '预期结果']))
    # print(read_cases('api_signup.xlsx',
    #                  ['用例编号', '用例标题', '接口路径', '请求方法', '请求类型', '参数', '预期结果', '验库表名', '验库sql', '数据库预期行数'],
    #                  ['参数', '预期结果', '数据库预期行数']))
   print(send_request('http://192.168.47.132/apitest/signup/','post','json',{'username':'admin','password':'123456','confirm':'123456','name':'管理员'}))
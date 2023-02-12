# 登录接口自动化测试用例（测试函数）
from common.case import read_cases, send_request, check
from common.db import DB
import pytest

DB().init_db(sqlfile='longin.sql')
cases = read_cases('api_login.xlsx', ['用例编号', '用例标题', '接口路径', '请求方法', '请求类型', '参数', '预期结果'], ['参数', '预期结果'])


@pytest.mark.parametrize('case_info, url, method, arg_type, args, expect', cases)  # 自带循环和用例解包
def test_login(case_info, url, method, arg_type, args, expect):  # pytest测试用例
    actual = send_request(url, method, arg_type, args)
    passed, msg = check(case_info, actual, expect)
    assert passed, msg


# def login():
#     DB().init_db(sqlfile='longin.sql')  # 初始化数据库
#     cases = read_cases('api_login.xlsx', ['用例编号', '用例标题', '接口路径', '请求方法', '请求类型', '参数', '预期结果'], ['参数', '预期结果'])  # 获取用例
#     for case in cases:
#         case_info, url, method, arg_type, args, expect = case
#         actual = send_request(url, method, arg_type, args)
#         check(case_info, actual, expect)

#


if __name__ == '__main__':
    pytest.main(['--html=../report/login.html', 'login.py'])

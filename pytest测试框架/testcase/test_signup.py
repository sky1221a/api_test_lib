# 注册接口自动化测试用例
from common.case import read_cases, send_request, check
from common.db import DB
import pytest

DB().init_db(sqlfile='signup.sql')  # 初始化数据库
cases = read_cases('api_signup.xlsx',
                   ['用例编号', '用例标题', '接口路径', '请求方法', '请求类型', '参数', '预期结果', '验库表名', '验库sql', '数据库预期行数'],
                   ['参数', '预期结果', '数据库预期行数'])


@pytest.mark.parametrize('case_info, url, method, args_type, args, expect, tables, check_sql, db_expect', cases)
def test_signup(case_info, url, method, args_type, args, expect, tables, check_sql, db_expect):
    actual = send_request(url, method, args_type, args)
    passed, msg = check(case_info, actual, expect)
    try:
        assert passed, msg
    finally:
        passed, msg = DB().check_db(case_info, tables, args, check_sql, db_expect)
        assert passed, msg


# def signup()
#     DB().init_db(sqlfile='signup.sql')  # 初始化数据库
#     cases = read_cases('api_signup.xlsx',
#                        ['用例编号', '用例标题', '接口路径', '请求方法', '请求类型', '参数', '预期结果', '验库表名', '验库sql', '数据库预期行数'],
#                        ['参数', '预期结果', '数据库预期行数'])  # 获取用例
#     for case in cases:
#         case_info, url, method, args_type, args, expect, tables, check_sql, db_expect = case
#         actual = send_request(url, method, args_type, args)
#         check(case_info, actual, expect)
#         DB().check_db(case_info,tables,args,check_sql,db_expect)


if __name__ == '__main__':
    pytest.main(['--html=../report/signup.html', 'test_signup.py'])

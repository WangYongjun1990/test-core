# -*- coding:utf-8 -*-

"""
File Name: `custom_functions`.py
Version:
Description:

Author: wangyongjun
Date: 2018/8/10 13:57
"""
import datetime
import json

from mitest.httprunner.compat import basestring
from mitest.utils.encryption import Encryption
from mitest.utils.tools import is_json_contains


""" custom functions
"""
def get_current_date(fmt="%Y-%m-%d"):
    """ 获取当前日期
    get current date, default format is %Y-%m-%d
    """
    return datetime.datetime.now().strftime(fmt)

""" custom comparators
"""
def json_contains(check_value, expect_value):
    """ json包含校验
    :param check_value:
    :param expect_value:
    :return:
    """
    assert isinstance(check_value, basestring)
    # bytes转str
    str_content = check_value.decode('utf-8')
    # str转dict
    dict_check = json.loads(str_content)
    assert isinstance(expect_value, basestring)
    dict_expect = json.loads(expect_value)
    # for key in dict_expect:
    #     assert key in dict_check
    #     assert dict_check[key] == dict_expect[key]
    assert is_json_contains(dict_check, dict_expect)


def db_validate(check_value, expect_value):
    """ 数据库校验
    :param check_value:
    :param expect_value:
    :return:
    """
    print(check_value, type(check_value))
    print(expect_value, type(expect_value))
    # res = sql_execute(check_value, env_name='aliuat')
    # check_value = res[0][0]
    assert check_value == expect_value


""" custom hooks
"""
def add_sign(request):
    """ 加签
    :param request:
    :return:
    """
    e = Encryption()
    if 'json' in request:
        request['json'] = json.loads(e.map_to_sign_common(request['json']))


def teardown_db_select(response, sql=None):
    """ 后置数据库查询
    :param response:
    :param sql:
    :return:
    """
    # bytes转str
    str_content = response.content.decode('utf-8')
    # str转dict
    dict_content = json.loads(str_content)
    # 添加sql查询结果
    dict_content['db_result'] = sql
    # dict转str_json
    str_content = json.dumps(dict_content, ensure_ascii=False)
    # str_json转bytes
    response.content = str_content.encode('utf-8')


def db_select(sql):
    """ 数据库操作
    :param sql:
    :return:
    """
    # TODO
    return sql + 's'

# TODO 编辑此文件后校验格式

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
import time

from mitest.api.mysql_sql_executor import sql_execute
from mitest.httprunner.compat import basestring
from mitest.utils.encryption import Encryption
from mitest.utils.send_mq import SendMQ
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
    start_time = time.time()

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

    end_time = time.time()
    d_time = end_time - start_time
    print("==================== json_contains, run {:.3}s ====================>\n".format(d_time))


def db_validate(check_value, expect_value):
    """ 数据库校验
    :param check_value:
    :param expect_value:
    :return:
    """
    start_time = time.time()

    print(check_value, type(check_value))
    print(expect_value, type(expect_value))
    # res = sql_execute(check_value, env_name='aliuat')
    # check_value = res[0][0]
    assert check_value == expect_value

    end_time = time.time()
    d_time = end_time - start_time
    print("==================== db_validate, run {:.3}s ====================>\n".format(d_time))


""" custom setup-hooks
"""
def add_sign(request, remote_host):
    """ 加签
    :param remote_host:
    :param request:
    :return:
    """
    start_time = time.time()

    kwargs = {
        "remote_host": remote_host
    }
    e = Encryption(**kwargs)
    if 'json' in request:
        request['json'] = json.loads(e.map_to_sign_common(request['json']))

    end_time = time.time()
    d_time = end_time - start_time
    print("==================== add_sign, run {:.3}s ====================>\n".format(d_time))


def setup_db_operation(sql, db_connect):
    """ 前置写入、更新、删除数据库操作
    :param db_connect:
    :param sql:
    :return:
    """
    start_time = time.time()

    sql_execute(sql, db_connect=db_connect)

    end_time = time.time()
    d_time = end_time - start_time
    print("==================== setup_db_operation, run {:.3}s ====================>\n".format(d_time))


def setup_send_mq(topic, tag, msg, mq_key, remote_host):
    """ 前置发送mq消息
    :param remote_host:
    :param mq_key:
    :param msg:
    :param tag:
    :param topic:
    :return:
    """
    start_time = time.time()

    kwargs = {
        "mq_key": mq_key,
        "remote_host": remote_host,
    }
    rb = SendMQ(**kwargs)
    return_msg = rb.send_mq(topic, tag, msg)
    # print(return_msg)

    end_time = time.time()
    d_time = end_time - start_time
    print("==================== setup_send_mq, run {:.3}s ====================>\n".format(d_time))


""" custom teardown-hooks
"""
def teardown_db_select(response, sql=None):
    """ 后置数据库查询, 废弃
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


def teardown_db_operation(sql, db_connect):
    """ 后置写入、更新、删除数据库操作
    :param db_connect:
    :param sql:
    :return:
    """
    start_time = time.time()

    sql_execute(sql, db_connect=db_connect)

    end_time = time.time()
    d_time = end_time - start_time
    print("==================== teardown_db_operation, run {:.3}s ====================>\n".format(d_time))


# TODO 编辑此文件后校验格式


if __name__ == '__main__':
    sql_d = "delete from mock_service.mock_info_bak where id=15; delete from mock_service.mock_info_bak where id=17;"
    teardown_db_operation(sql_d, 'aliuat')
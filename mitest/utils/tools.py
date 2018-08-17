# -*- coding:utf-8 -*-

"""
File Name: `tools`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/21 14:03
"""
import datetime
import json
import socket
import time


def get_host():
    """
    获取运行主机host
    :return:
    """
    ip = socket.gethostbyname(socket.gethostname())
    return "{}:7000".format(ip)
    # return "99.48.58.31:7000"


def get_current_time():
    """
    获取当前时间，返回YYYY-mm-dd HH:MM:SS格式的时间字符串
    """
    return str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


def is_json_contains(actual, expect):
    if isinstance(actual, list) and isinstance(expect, list):
        actual_inner_dict_list = []
        actual_inner_list_list = []
        for key in actual:
            if isinstance(key, dict):
                actual_inner_dict_list.append(key)
            elif isinstance(key, list):
                actual_inner_list_list.append(key)
        for key in expect:
            if isinstance(key, dict):
                flag = False
                for _key in actual_inner_dict_list:
                    if is_json_contains(_key, key):
                        flag = True
                if not flag:
                    return False
            elif isinstance(key, list):
                flag = False
                for _key in actual_inner_list_list:
                    if is_json_contains(_key, key):
                        flag = True
                if not flag:
                    return False
            elif key not in actual:
                return False

    elif isinstance(actual, dict) and isinstance(expect, dict):
        for key in expect:
            if key not in actual:
                return False
            if isinstance(actual[key], dict) and isinstance(expect[key], dict):
                if not is_json_contains(actual[key], expect[key]):
                    return False
            elif isinstance(actual[key], list) and isinstance(expect[key], list):
                if not is_json_contains(actual[key], expect[key]):
                    return False
            elif actual[key] != expect[key]:
                return False

    return True


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.__str__()
        return json.JSONEncoder.default(self, obj)


def json_dumps(dic):
    return json.dumps(dic, ensure_ascii=False, cls=DateEncoder)


def json_loads(str_):
    return json.loads(str_)

if __name__ == '__main__':
    print(get_host())
    print(get_current_time())
    check_dict = {"a": {"C": "122", "B": {"C": "122", "B": {"kk": 123}}}, "b": [1, 2, [3, 2], {"1": [{}, "2"]}, {"1": "2"}], "c": 2}
    expect_dict = {"a": {"C": "122", "B": {"B": {"kk": 123}}}, "b": [1, [2, 3], {"1": "2", "2": "2"}], "c": 2}
    print(is_json_contains(check_dict, expect_dict))

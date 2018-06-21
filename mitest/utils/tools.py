# -*- coding:utf-8 -*-

"""
File Name: `tools`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/21 14:03
"""
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

if __name__ == '__main__':
    print(get_host())
    print(get_current_time())

# -*- coding:utf-8 -*-

"""
File Name: `default`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/19 17:47
"""
import platform


class Config(object):
    JSON_AS_ASCII = False
    # SECRET_KEY = os.urandom (24)

    # mysql
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True

    # log
    LINUX_LOG = '/usr/local/src/logs/mitest_platform/mitest_platform.log'
    WINDOWS_LOG = r'E:\git_work\flask_study\my_flask\logs\flask.log'
    MAC_LOG = '/Users/wangyongjun/git_work/mitest-platform-core/mitest/logs/mitest_platform.log'

    if platform.system() == 'Linux':
        LOG_PATH = LINUX_LOG
    elif platform.system() == 'Windows':
        LOG_PATH = WINDOWS_LOG
    elif platform.system() == 'Darwin':
        LOG_PATH = MAC_LOG
    else:
        LOG_PATH = LINUX_LOG


def get_config():
    return Config

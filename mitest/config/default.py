# -*- coding:utf-8 -*-

"""
File Name: `default`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/19 17:47
"""
import os
import platform


class Config(object):

    JSON_AS_ASCII = False
    # SECRET_KEY = os.urandom (24)

    # mysql
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True

    # log
    LINUX_LOG = '/usr/local/src/logs/mitest_platform/mitest_platform.log'
    WINDOWS_LOG = os.getcwd() + r'\mitest\logs\flask.log'
    # WINDOWS_LOG = r'E:\git_mime\mitest-platform-core\mitest\logs\flask.log'
    MAC_LOG = '/Users/wangyongjun/git_work/mitest-platform-core/mitest/logs/flask.log'

    # report path
    LINUX_REPORT_TEMPLATE = '/user/local/src/mitest-platform-core/mitest/engine/templates/default_report_template.html'
    WINDOWS_REPORT_TEMPLATE = os.getcwd() + r'\mitest\engine\templates\default_report_template.html'
    # WINDOWS_REPORT_TEMPLATE = r"E:\git_mime\mitest-platform-core\mitest\engine\templates\default_report_template.html"
    MAC_REPORT_TEMPLATE = '/Users/wangyongjun/git_work/mitest-platform-core/mitest/engine/templates/default_report_template.html'

    if platform.system() == 'Linux':
        LOG_PATH = LINUX_LOG
        REPORT_TEMPLATE_PATH = LINUX_REPORT_TEMPLATE
    elif platform.system() == 'Windows':
        LOG_PATH = WINDOWS_LOG
        REPORT_TEMPLATE_PATH = WINDOWS_REPORT_TEMPLATE
    elif platform.system() == 'Darwin':
        LOG_PATH = MAC_LOG
        REPORT_TEMPLATE_PATH = MAC_REPORT_TEMPLATE
    else:
        LOG_PATH = LINUX_LOG
        REPORT_TEMPLATE_PATH = LINUX_REPORT_TEMPLATE

    # email to
    EMAIL_TO = ['yongjun.wang@mi-me.com']


def get_config():
    return Config


if __name__ == '__main__':
    print(os.path.split(os.path.realpath(__file__))[0])

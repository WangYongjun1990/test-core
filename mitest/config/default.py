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
    #获取文件目录相对路径
    BASE_PATH = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '\..')

    JSON_AS_ASCII = False
    # SECRET_KEY = os.urandom (24)

    # mysql
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True

    # log
    LINUX_LOG = '/usr/local/src/logs/mitest_platform/mitest_platform.log'
    # WINDOWS_LOG = os.getcwd() + r'\mitest\logs\flask.log'
    #WINDOWS_LOG = r'E:\git_mime\mitest-platform-core\mitest\logs\flask.log'

    WINDOWS_LOG =BASE_PATH + r'\logs' + r'\flask.log'

    MAC_LOG = '/Users/wangyongjun/git_work/mitest-platform-core/mitest/logs/flask.log'

    # report path
    LINUX_REPORT_TEMPLATE = '/user/local/src/mitest-platform-core/mitest/engine/templates/default_report_template.html'
    # WINDOWS_REPORT_TEMPLATE = os.getcwd() + r'\mitest\engine\templates\default_report_template.html'
    #WINDOWS_REPORT_TEMPLATE = r"E:\git_mime\mitest-platform-core\mitest\engine\templates\default_report_template.html"
    WINDOWS_REPORT_TEMPLATE = BASE_PATH + r'\engine\templates\default_report_template.html'
    MAC_REPORT_TEMPLATE = '/Users/wangyongjun/git_work/mitest-platform-core/mitest/engine/templates/default_report_template.html'

    # tmp path
    LINUX_TEMP_DIR = '/user/local/src/mitest-platform-core/mitest/api/tmp/'
    # WINDOWS_TEMP_DIR = os.getcwd() + '\\mitest\\api\\tmp\\'
    #WINDOWS_TEMP_DIR = "E:\\git_mime\\mitest-platform-core\\mitest\\api\\tmp\\"
    WINDOWS_TEMP_DIR = BASE_PATH + r'\api\tmp'
    MAC_TEMP_DIR = '/Users/wangyongjun/git_work/mitest-platform-core/mitest/api/tmp/'

    # custom file path
    LINUX_CUSTOM_FILE = '/user/local/src/mitest-platform-core/mitest/utils/custom.py'
    WINDOWS_CUSTOM_FILE = BASE_PATH + r'\utils\custom.py'
    MAC_CUSTOM_FILE = '/Users/wangyongjun/git_work/mitest-platform-core/mitest/utils/custom.py'

    if platform.system() == 'Linux':
        LOG_PATH = LINUX_LOG
        REPORT_TEMPLATE_PATH = LINUX_REPORT_TEMPLATE
        TEMP_DIR = LINUX_TEMP_DIR
        CUSTOM_FILE = LINUX_CUSTOM_FILE
    elif platform.system() == 'Windows':
        LOG_PATH = WINDOWS_LOG
        REPORT_TEMPLATE_PATH = WINDOWS_REPORT_TEMPLATE
        TEMP_DIR = WINDOWS_TEMP_DIR
        CUSTOM_FILE = WINDOWS_CUSTOM_FILE
    elif platform.system() == 'Darwin':
        LOG_PATH = MAC_LOG
        REPORT_TEMPLATE_PATH = MAC_REPORT_TEMPLATE
        TEMP_DIR = MAC_TEMP_DIR
        CUSTOM_FILE = MAC_CUSTOM_FILE
    else:
        LOG_PATH = LINUX_LOG
        REPORT_TEMPLATE_PATH = LINUX_REPORT_TEMPLATE
        TEMP_DIR = LINUX_TEMP_DIR
        CUSTOM_FILE = LINUX_CUSTOM_FILE

    # email to
    EMAIL_TO = ['yongjun.wang@mi-me.com']


def get_config():
    return Config


if __name__ == '__main__':
    print(os.path.split(os.path.realpath(__file__))[0])

# -*- coding:utf-8 -*-

"""
File Name: `sit`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/20 16:41
"""
import platform

from mitest.config.default import Config


class SitConfig(Config):
    # mysql
    if platform.system() == 'Linux':
        SQLALCHEMY_DATABASE_URI = "mysql+pymysql://yongjun.wang:1qaz@WSX@192.168.10.2:3306/mitest_platform_sit?charset=utf8"
    elif platform.system() == 'Windows':
        SQLALCHEMY_DATABASE_URI = "mysql+pymysql://yongjun.wang:1qaz@WSX@192.168.10.2:3306/mitest_platform_sit?charset=utf8"
    elif platform.system() == 'Darwin':
        SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/mitest_platform?charset=utf8"
    else:
        SQLALCHEMY_DATABASE_URI = "mysql+pymysql://yongjun.wang:1qaz@WSX@192.168.10.2:3306/mitest_platform_sit?charset=utf8"

# -*- coding:utf-8 -*-

"""
File Name: `load_config`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/20 16:48
"""


def load_config(mode):
    try:
        if mode == "SIT":
            from mitest.config.sit import SitConfig
            return SitConfig
        elif mode == "ALIUAT":
            from mitest.config.aliuat import AliuatConfig
            return AliuatConfig
        else:
            raise ValueError("ENV MODE selection out of range")
    except ValueError as e:
        from mitest.config.sit import SitConfig
        return SitConfig

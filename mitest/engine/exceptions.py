# -*- coding:utf-8 -*-

"""
File Name: `exceptions`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/22 下午9:49
"""
import json

try:
    JSONDecodeError = json.decoder.JSONDecodeError
except AttributeError:
    JSONDecodeError = ValueError


class LoadCaseError(BaseException):
    """
    组装用例时发生错误
    """
    pass


class RunCaseError(BaseException):
    """
    执行用例时发生错误
    """
    pass
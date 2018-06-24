# -*- coding:utf-8 -*-

"""
File Name: `testsuite`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/21 13:44
"""
import json

from flask import Blueprint
from flask_restful import Resource

from mitest.api.comm_log import logger
from mitest.views.wrappers import timer
from mitest.utils.common import get_request_json, make_response

testsuite = Blueprint('testsuite_interface', __name__)


class Testsuite(Resource):
    def __init__(self):
        pass

    @timer
    def post(self, action):
        data = get_request_json()

        if action == 'add':
            try:
                testsuite_name = data.pop('testsuiteName')
                simple_desc = data.pop('simpleDesc', None)
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

        elif action == 'edit':
            try:
                id = data.pop('id')
                testsuite_name = data.pop('testsuiteName')
                simple_desc = data.pop('simpleDesc', None)
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

        elif action == 'delete':
            try:
                id = data.pop('id')
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

        elif action == 'detail':
            pass

        elif action == 'list':
            pass

        else:
            return make_response({"code": "100", "desc": "url错误，不存在的接口动作<{action}>".format(action=action)})
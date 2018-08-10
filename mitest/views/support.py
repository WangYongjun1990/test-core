# -*- coding:utf-8 -*-

"""
File Name: `testcase`.py
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
from mitest.utils.common import get_request_json, make_response, read_custom

support = Blueprint('support_interface', __name__)


class Support(Resource):
    def __init__(self):
        pass

    @timer
    def post(self, action):
        data = get_request_json()
        custom = read_custom()

        if action == 'queryCustomFunctions':
            functions = custom['functions']

            return make_response({"code": "000", "data": functions})

        elif action == 'queryCustomComparators':
            comparators = custom['comparators']

            return make_response({"code": "000", "data": comparators})

        elif action == 'queryCustomHooks':
            hooks = custom['hooks']

            return make_response({"code": "000", "data": hooks})

        else:
            return make_response({"code": "100", "desc": "url错误，不存在的接口动作<{action}>".format(action=action)})
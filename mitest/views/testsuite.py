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
from mitest.api.mysql_manager import TestsuiteInfoManager

testsuite = Blueprint('testsuite_interface', __name__)


class Testsuite(Resource):
    def __init__(self):
        pass

    @timer
    def post(self, action):
        data = get_request_json()
        tim = TestsuiteInfoManager()

        if action == 'add':
            try:
                testsuite_name = data.pop('testsuiteName')
                simple_desc = data.pop('simpleDesc', None)
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

            tim.insert_testsuite(testsuite_name=testsuite_name, simple_desc=simple_desc)
            return make_response({"code": "000", "desc": "{}测试集已添加".format(testsuite_name)})

        elif action == 'edit':
            try:
                id_ = data.pop('id')
                testsuite_name = data.pop('testsuiteName')
                simple_desc = data.pop('simpleDesc', None)
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

            tim.update_testsuite(id_, project_name=testsuite_name, simple_desc=simple_desc)
            return make_response({"code": "000", "desc": "{}测试集名称已修改".format(testsuite_name)})

        elif action == 'delete':
            try:
                id_ = data.pop('id')
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

            tim.delete_testsuite(id_)
            return make_response({"code": "000", "desc": "测试集已删除"})

        elif action == 'detail':
            pass

        elif action == 'list':
            pass

        else:
            return make_response({"code": "100", "desc": "url错误，不存在的接口动作<{action}>".format(action=action)})
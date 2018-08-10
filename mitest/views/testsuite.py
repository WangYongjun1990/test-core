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
from mitest.utils.tools import json_dumps, json_loads
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
            """
                url: /testsuite/add
                http类型入参: {"testsuiteName":"queryMock", "type":"HTTP", "info":{"apiUrl":"/mock/config/queryMock", "headers":"{\"Content-Type\":\"application/json\",\"oops\":\"oops\"}", "method":"POST"}, "moduleId":"5"}
                dubbo类型入参： {"testsuiteName":"queryMock_mq", "type":"MQ", "info":{"service":"service_for_dubbo", "method":"method_for_dubbo", "parameterTypes":"{\"cn.memedai.sse.facade.model.query.req\",\"cn.memedai.sse.facade.model.query.page\"}"}, "moduleId":"5"}
                mq类型入参：{"testsuiteName":"queryMock_mq", "type":"MQ", "info":{"topic":"topic_for_mq", "tag":"tag_for_mq"}, "moduleId":"5"}
            """
            try:
                testsuite_name = data.pop('testsuiteName')
                intf_type = data.pop('type')
                intf_info = data.pop('info')
                module_id = data.pop('moduleId')
                simple_desc = data.pop('simpleDesc', None)
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

            logger.debug(type(intf_info), intf_info)
            tim.insert_testsuite(testsuite_name=testsuite_name, simple_desc=simple_desc, intf_type=intf_type,
                                 intf_info=json_dumps(intf_info), module_id=module_id)
            return make_response({"code": "000", "desc": "{}测试集已添加".format(testsuite_name)})

        elif action == 'edit':
            """
                url: /testsuite/edit
                input: {"id":"3", "testsuiteName":"queryMock", "type":"HTTP", "info":{"apiUrl":"/mock/config/queryMock", "headers":"{\"Content-Type\":\"application/json\",\"oops\":\"oops\"}", "method":"POST"}, "moduleId":"5"}
            """
            try:
                id_ = data.pop('id')
                testsuite_name = data.pop('testsuiteName')
                intf_type = data.pop('type')
                intf_info = data.pop('info')
                module_id = data.pop('moduleId')
                simple_desc = data.pop('simpleDesc', None)
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

            tim.update_testsuite(id_, project_name=testsuite_name, simple_desc=simple_desc, intf_type=intf_type,
                                 intf_info=json_dumps(intf_info), module_id=module_id)
            return make_response({"code": "000", "desc": "{}测试集已修改".format(testsuite_name)})

        elif action == 'delete':
            """
                url: /testsuite/delete
                input: {"id":"3"}
            """
            try:
                id_ = data.pop('id')
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

            tim.delete_testsuite(id_)
            return make_response({"code": "000", "desc": "测试集已删除"})

        elif action == 'detail':
            """
                url: /testsuite/detail
                input: {"id":"3"}
                output: {"code": "000", "data": {"testsuiteName":"queryMock", "type":"HTTP", "info":{"apiUrl":"/mock/config/queryMock", "headers":"{\"Content-Type\":\"application/json\",\"oops\":\"oops\"}", "method":"POST"}, "moduleId":"5"}}
            """
            try:
                id_ = data.pop('id')
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

            obj = tim.query_testsuite_by_id(id_)
            data = {
                "testsuiteName": obj.testsuite_name,
                "simpleDesc": obj.simple_desc,
                "type": obj.intf_type,
                "info": json_loads(obj.intf_info),
                "moduleId": obj.module_id
            }
            return make_response({"code": "000", "data": data})

        elif action == 'list':
            pass

        else:
            return make_response({"code": "100", "desc": "url错误，不存在的接口动作<{action}>".format(action=action)})
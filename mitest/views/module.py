# -*- coding:utf-8 -*-

"""
File Name: `module`.py
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
from mitest.api.mysql_manager import ModuleInfoManager,TestsuiteInfoManager

module = Blueprint('module_interface', __name__)
import mitest.config.sit
from flask import Flask

Flask(__name__).config.from_object(mitest.config.sit)


class Module(Resource):
    def __init__(self):
        pass

    @timer
    def post(self, action):
        data = get_request_json()
        mim = ModuleInfoManager()
        if action == 'add':
            try:
                system_id = data["systemId"]
                module_name = data["moduleName"]
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})
            module_name_list = mim.query_module(system_id,module_name)
            if len(module_name_list) != 0:
                return make_response({"code": "201", "desc": "这个名称的测试模块已经存在"})
            mim.insert_module(module_name = module_name,system_id = system_id)
            return make_response({"code": "000", "desc": "{}模块添加成功".format(module_name)})
        elif action == 'edit':
            try:
                id = data["id"]
                module_name = data["moduleName"]
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})
            res_module_name = mim.query_module_id(id=id)[0].module_name
            if res_module_name == module_name:
                return make_response({"code": "201", "desc": "您修改的模块名称已存在"})
            mim.update_module(id_=id,module_name=module_name)
            return make_response({"code": "000", "desc": "操作成功"})
        elif action == 'delete':
            try:
                id = data["id"]
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})
            mim.delete_module(id_=id)
            return make_response({"code": "000", "desc": "操作成功"})
        elif action == 'detail':
            pass
        elif action == 'list':
            try:
                system_id = data["systemId"]
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})
            module_list = mim.query_all_module(system_id=system_id)
            res = list()
            id = 0
            for i in module_list:
                module_dict = dict()
                if module_list:
                    id += 1
                    module_dict["id"] = id
                module_dict["moduleId"] = i.id
                module_dict["label"] = i.module_name
                testsuite_list = TestsuiteInfoManager.query_all_testsuite(module_id=i.id)
                testsuite = list()
                for j in testsuite_list:
                    testsuite_dict = dict()
                    if testsuite_list:
                        id += 1
                        testsuite_dict["id"] = id
                    testsuite_dict["testsuiteId"] = j.id
                    testsuite_dict["label"] = j.testsuite_name
                    testsuite.append(testsuite_dict)
                module_dict["children"] = testsuite
                res.append(module_dict)
            return make_response({"code": "000", "desc": res})
        else:
            return make_response({"code": "100", "desc": "url错误，不存在的接口动作<{action}>".format(action=action)})
if __name__ == '__main__':
    Module = Module()
    res = Module.post("list")
    print(res)
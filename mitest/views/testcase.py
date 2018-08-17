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
from mitest.engine.handle_testcase import handle_testcase
from mitest.api.mysql_manager import TestsuiteInfoManager,TestcaseInfoManager
from mitest.views.wrappers import timer
from mitest.utils.common import get_request_json, make_response

testcase = Blueprint('testcase_interface', __name__)


class Testcase(Resource):
    def __init__(self):
        pass

    @timer
    def post(self, action):
        data = get_request_json()
        tim = TestcaseInfoManager()
        if action == 'add':
            handle_testcase(action, **data)


        elif action == 'edit':
            pass

        elif action == 'delete':
            """
                            api:/testcase/delete/:id
                        """
            try:
                id_ = data.pop('id')
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

            if not tim.is_testcase_id_exist(id_):
                return make_response({"code": "200", "desc": "用例不存在,无法删除"})

            tim.delete_testcase(id_)
            return make_response({"code": "000", "desc": "测试用例删除成功"})


        elif action == 'detail':
            pass

        elif action == 'queryByTestsuiteId':
            """
                根据testsuite_id查找该套件下的所有测试用例
                url:/testcase/queryByTestsuiteId/:testsuite_id
            """
            try:
                testsuite_id=data.pop('testsuite_id')
                tsim=TestsuiteInfoManager()
                #判断testsuite_id是否存在
                if not tsim.query_testsuite_by_id(testsuite_id):
                    return make_response({"code": "200", "desc": "测试用例集不存在,无法查询"})
                datas=tim.get_suite_testcase(testsuite_id)
                projects=[]
                desc_list=[]

                for i in datas:
                    projects.append([i.id,i.testcase_name])
                    '''[1,test1]'''
                for j in projects:
                    project_dict={}
                    project_dict["id"]=j[0]
                    project_dict["testcase_name"]=j[1]
                    desc_list.append((project_dict))
                return make_response({"code": "000", "desc": desc_list})
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})


        else:
            return make_response({"code": "100", "desc": "url错误，不存在的接口动作<{action}>".format(action=action)})
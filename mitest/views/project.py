# -*- coding:utf-8 -*-

"""
File Name: `project`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/21 11:41
"""
import json

from flask import Blueprint
from flask_restful import Resource

from mitest.api.comm_log import logger
from mitest.api.mysql_manager import ProjectInfoManager
from mitest.views.wrappers import timer
from mitest.utils.common import get_request_json, make_response

project = Blueprint('project_interface', __name__)


class Project(Resource):
    def __init__(self):
        pass

    @timer
    def post(self, action):
        data = get_request_json()

        if action == 'add':
            try:
                project_name = data.pop('projectName')
                simple_desc = data.pop('simpleDesc', None)
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

            pim = ProjectInfoManager()
            if pim.is_project_name_exist(project_name):
                return make_response({"code": "201", "desc": "项目名称已存在"})

            pim.insert_project(project_name=project_name, simple_desc=simple_desc)
            return make_response({"code": "000", "desc": "项目增加成功"})

        elif action == 'edit':
            try:
                id_ = data.pop('id')
                project_name = data.pop('projectName')
                simple_desc = data.pop('simpleDesc', None)
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

            pim = ProjectInfoManager()
            pim.update_project(id_, project_name=project_name, simple_desc=simple_desc)
            return make_response({"code": "000", "desc": "项目修改成功"})

        elif action == 'delete':
            try:
                id_ = data.pop('id')
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

            pim = ProjectInfoManager()
            pim.delete_project(id_)
            return make_response({"code": "000", "desc": "项目删除成功"})

        elif action == 'detail':
            pass

        elif action == 'list':
            pass

        else:
            return make_response({"code": "100", "desc": "url错误，不存在的接口动作<{action}>".format(action=action)})

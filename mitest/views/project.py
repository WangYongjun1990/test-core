# -*- coding:utf-8 -*-

"""
File Name: `project`.py
Version:
Description:

Author: hanxueyao
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
            try:
                pim = ProjectInfoManager()
                result1 = pim.project_info()
                i_ = 1

                desc_list = []
                projects = []

                # 循环查询project返回所有的Project数据，并将其加入list 方便遍历
                for i in result1:
                    projects.append([i.id, i.project_name])

                    # 遍历project_list 并将其添加到字典中，并对字段赋值
                for j in projects:
                    project_dict = {}
                    project_dict["id"] = i_
                    project_dict["projectId"] = j[0]
                    project_dict["label"] = j[1]
                    project_dict["children"] = []
                    desc_list.append(project_dict)
                    result2 = pim.system_info(j[0])
                    i_ = i_ + 1

                    # 遍历通过project_id查询system_info得到的结果，将其添加到systemlist当中，方便遍历最后组装到response
                    for k in result2:
                        print(k)
                        system_dict = {}
                        system_dict["id"] = i_
                        system_dict["systemId"] = k.id
                        system_dict["label"] = k.system_name
                        project_dict["children"].append(system_dict)
                        i_ = i_ + 1
                return make_response({"code": "000", "desc": desc_list})
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})



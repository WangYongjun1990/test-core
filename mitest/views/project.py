# -*- coding:utf-8 -*-

"""
File Name: `project`.py
Version:
Description:

Author: hanxueyao
Date: 2018/6/21 11:41

增加接口：/project/add
入参格式：
    {
        "projectName":"XXX",
        "simpleDec:"xxx"(非必填)
    }

修改接口：/project/edit
入参格式：
    {
        "id":xx,
        "projectName":"xxx",
        "simpleDec:"xxx"(非必填)
    }

删除接口:/project/delete
入参格式：
    {
        “id":xxx
    }

查询接口:/project/list
入参格式：
    {
        "projectName":"xxx"(非必填)
    }

"""
import json

import time

from flask import Blueprint
from flask_restful import Resource

from mitest.api.comm_log import logger
from mitest.api.mysql_manager import ProjectInfoManager, SystemInfoManager, ModuleInfoManager, TestsuiteInfoManager
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

            # 判断项目名是否已存在，存在无法添加

            if pim.is_project_name_exist_for_update(project_name):
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

            # 校验项目ID是否存在，不存在无法修改

            if not pim.is_project_id_exist(id_):
                return make_response({"code": "201", "desc": "项目不存在，无法修改"})
            elif pim.is_project_name_exist_union(id_,project_name) and simple_desc != None:
                pim.update_project(id_, project_name=project_name, simple_desc=simple_desc)
                return make_response({"code": "000", "desc": "项目修改成功"})
            elif pim.is_project_id_exist(id_) and not pim.is_project_name_exist_for_update(project_name):
                pim.update_project(id_, project_name=project_name, simple_desc=simple_desc)
                return make_response({"code": "000", "desc": "项目修改成功"})
            else:
                return make_response({"code": "201", "desc": "项目名已存在，无法修改"})

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


        elif action == 'list':
            try:
                # time.sleep(5)

                # 查询列表入参可以为空或者输入项目名称
                project_name = data.pop('projectName')
                pim = ProjectInfoManager()

                if project_name != "":
                    if not pim.is_project_name_exist(project_name):

                        return make_response({"code": "200", "desc": "项目名不存在,无法查询"})

                result1 = pim.project_info(project_name)
                print(project_name)
                print(result1)

                desc_list = []
                projects = []

                # 循环查询project返回所有的Project数据，并将其加入list 方便遍历
                for i in result1:
                    projects.append([i.id, i.project_name,i.simple_desc])

                    # 遍历project_list 并将其添加到字典中，并对字段赋值
                for j in projects:
                    project_dict = {}
                    project_dict["id"] = j[0]
                    project_dict["projectName"] = j[1]
                    project_dict["description"] = j[2]
                    desc_list.append(project_dict)
                # 将desc_list 根据项目名进行排序
                desc_list.sort(key = lambda desc_sort:(desc_sort.get("projectName",0)))
                return make_response({"code": "000", "desc": desc_list})
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

        elif action == 'subtree':
            try:
                project_id = data.pop('id')
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

            sim = SystemInfoManager()
            system_list = sim.select_by_project_id(project_id)

            subtree = []
            index_id = 0
            for s in system_list:
                system_dict = dict()
                index_id += 1
                system_dict['id'] = index_id
                system_dict['label'] = s.system_name
                system_dict['systemId'] = s.id

                module_list = ModuleInfoManager.query_all_module(system_id=s.id)
                children_module = list()
                for m in module_list:
                    module_dict = dict()
                    index_id += 1
                    module_dict["id"] = index_id
                    module_dict["moduleId"] = m.id
                    module_dict["label"] = m.module_name

                    testsuite_list = TestsuiteInfoManager.query_all_testsuite(module_id=m.id)
                    children_testsuite = list()
                    for t in testsuite_list:
                        testsuite_dict = dict()
                        index_id += 1
                        testsuite_dict["id"] = index_id
                        testsuite_dict["testsuiteId"] = t.id
                        testsuite_dict["label"] = t.testsuite_name
                        children_testsuite.append(testsuite_dict)

                    module_dict["children"] = children_testsuite
                    children_module.append(module_dict)
                system_dict["children"] = children_module

                subtree.append(system_dict)

            # logger.debug(subtree)
            return make_response({"code": "000", "data": subtree})

        else:
            return make_response({"code": "100", "desc": "url错误，不存在的接口动作<{action}>".format(action=action)})



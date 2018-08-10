# -*- coding:utf-8 -*-

"""
File Name: `system`.py
Version:
Description:

Author: hanxueyao
Date: 2018/6/21 11:44

增加接口：/system/add
入参格式：
    {
        "systemName": "wallet_system5",
        "simpleDesc":"123321",(非必填)
        "testUser":"hanxueyao",
        "devUser":"hanxueyao",
        "projectId":3,
        "publishApp":"wallet"
    }

修改接口：/system/edit

入参格式：
    {
        "systemName": "wallet_system5",
        "simpleDesc":"123321",
        "testUser":"hanxueyao",
        "devUser":"hanxueyao",
        "projectId":3,
        "publishApp":"wallet"
    }

删除接口:/system/delete
入参格式：
    {
        “id":xxx
    }


查询接口:/system/list
入参格式：
    {
        “systemName":xxx（非必填）
    }

"""
import json

from flask import Blueprint
from flask_restful import Resource

from mitest.api.comm_log import logger
from mitest.views.wrappers import timer
from mitest.utils.common import get_request_json, make_response
from mitest.api.mysql_manager import SystemInfoManager

system = Blueprint('system_interface', __name__)


class System(Resource):
    def __init__(self):
        pass

    @timer
    def post(self, action):
        data = get_request_json()

        if action == 'add':
            try:
                system_name = data.pop('systemName')
                simple_desc = data.pop('simpleDesc', None)
                project_id = data.pop('projectId')
                test_user = data.pop('testUser', None)
                dev_user = data.pop('devUser', None)
                publish_app = data.pop('publishApp', None)
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

            pim = SystemInfoManager()

#判断project_id是否存在

            if not pim.is_project_id_exist(project_id):
                return make_response({"code": "200", "desc": "项目不存在"})

# 判断system_name是否存在
            elif pim.is_system_name_exist(system_name):
                return make_response({"code": "201", "desc": "系统名称已存在"})

#针对入参进行入库
            pim.insert_system(system_name=system_name, simple_desc=simple_desc, test_user=test_user, dev_user=dev_user, publish_app=publish_app, project_id=project_id)
            return make_response({"code": "000", "desc": "系统增加成功"})


        elif action == 'edit':
            try:
                id_ = data.pop('id')
                system_name = data.pop('systemName')
                simple_desc = data.pop('simpleDesc')
                project_id = data.pop('projectId')
                test_user = data.pop('testUser', None)
                dev_user = data.pop('devUser', None)
                publish_app = data.pop('publishApp', None)
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

            pim = SystemInfoManager()

            # 判断修改数据是否存在

            if not pim.is_system_id_exist(id_):
                return make_response({"code": "200", "desc": "项目不存在,无法修改"})

            # 根据入参进行数据修改

            pim.update_system(id_,system_name=system_name, simple_desc=simple_desc, test_user=test_user, dev_user=dev_user, publish_app=publish_app, project_id=project_id)
            return make_response({"code": "000", "desc": "系统修改成功"})


        elif action == 'delete':
            try:
                id_ = data.pop('id')
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

            pim = SystemInfoManager()

            # 判断修改数据是否存在

            if not pim.is_system_id_exist(id_):
                return make_response({"code": "200", "desc": "项目不存在,无法删除"})

            # 根据入参进行数据修改

            pim.delete_system(id_)
            return make_response({"code": "000", "desc": "系统删除成功"})

        elif action == 'detail':
            pass

        elif action == 'list':
            try:
                # 查询列表入参可以为空或者输入系统名称
                system_name = data.pop('systemName')
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

            pim = SystemInfoManager()

            if system_name != "":
                if not pim.is_system_name_exist(system_name):

                    return make_response({"code": "200", "desc": "系统名不存在,无法查询"})

            result1 = pim.system_info(system_name)

            # print(system_name)
            # print(result1)

            desc_list = []
            systems = []


            # 循环查询system表返回所有的System数据，先通过project_id查询project_info表对应的name，再通过子循环往systems List添加信息，如果project_id存在，才插入

            for i in result1:
                result2 = pim.project_info(i.project_id)
                for k in result2:
                    systems.append([i.id, i.system_name, i.simple_desc, k.project_name])
                # systems.append([i.id, i.system_name, i.simple_desc, i.project_id])
            print(systems)

                # 遍历system_list 并将其添加到字典中，并对字段赋值
            for j in systems:
                system_dict = {}
                system_dict["id"] = j[0]
                system_dict["systemName"] = j[1]
                system_dict["description"] = j[2]
                system_dict["belongProject"] = j[3]
                desc_list.append(system_dict)
            # 将desc_list 根据项目名进行排序

            desc_list.sort(key = lambda desc_sort:(desc_sort.get("systemName",0)))
            return make_response({"code": "000", "desc": desc_list})

        elif action == 'queryByProjectId':
            """ 根据projectId查询项目下的所有系统
            url: /system/queryByProjectId
            input:
                {"projectId":"14"}
            output:
                {
                  "code": "000",
                  "data": [
                    {
                      "systemId": 10,
                      "systemName": "mock"
                    }
                  ]
                }
            """
            try:
                project_id = data.pop('projectId')
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

            obj = SystemInfoManager.select_by_project_id(project_id)
            system_list = []
            for s in obj:
                system_info_dic = {
                    "systemName": s.system_name,
                    "systemId": s.id,
                }
                system_list.append(system_info_dic)

            return make_response({"code": "000", "data": system_list})

        else:
            return make_response({"code": "100", "desc": "url错误，不存在的接口动作<{action}>".format(action=action)})

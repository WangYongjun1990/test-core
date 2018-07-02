# -*- coding:utf-8 -*-

"""
File Name: `system`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/21 11:44
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
                test_user = data.pop('testUser')
                dev_user = data.pop('devUser')
                publish_app = data.pop('publishApp')
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

            pim = SystemInfoManager()

#判断project_id是否存在

            if pim.is_project_id_exist(project_id):
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
                test_user = data.pop('testUser')
                dev_user = data.pop('devUser')
                publish_app = data.pop('publishApp')
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

            pim = SystemInfoManager()

            # 判断修改数据是否存在

            if pim.is_system_id_exist(id_):
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

            if pim.is_system_id_exist(id_):
                return make_response({"code": "200", "desc": "项目不存在,无法删除"})

            # 根据入参进行数据修改

            pim.delete_system(id_)
            return make_response({"code": "000", "desc": "系统删除成功"})

        elif action == 'detail':
            pass

        elif action == 'list':
            pass

        else:
            return make_response({"code": "100", "desc": "url错误，不存在的接口动作<{action}>".format(action=action)})

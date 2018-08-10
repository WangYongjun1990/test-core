# -*- coding:utf-8 -*-

"""
File Name: `env`.py
Version:
Description:

Author: hanxueyao
Date: 2018/6/21 11:44

增加接口：/env/add
入参格式：
    {
        "envName":"xxx",
        "baseHost":"xxx",
        "dubboZookeeper":"xxx",
        "mqKey":"xxx",
        "dbConnect":"xxx",
        "remoteHost":"xxxx",
        "disconfHost":"xxxx",
        "redisConnect":"xxxx",
        "simpleDesc":"xxxx"(非必填)
    }

修改接口：/env/edit
入参格式:

        {
        "env_Name":"xxx",
        "base_Host":"xxx",
        "dubboZookeeper":"xxx",
        "mqKey":"xxx",
        "dbConnect":"xxx",
        "remoteHost":"xxxx",
        "disconfHost":"xxxx",
        "redisConnect":"xxxx",
        "simpleDesc":"xxxx"(非必填)
    }


删除接口:/env/delete
入参格式：
    {
        “id":xxx
    }

查询接口:/env/list

入参格式:
    {
    }

"""
import json



from flask import Blueprint
from flask_restful import Resource

from mitest.models.mitest_platform import EnvInfo
from mitest.api.comm_log import logger
from mitest.views.wrappers import timer
from mitest.utils.common import get_request_json, make_response
from mitest.api.mysql_manager import EnvInfoManager

env = Blueprint('env_interface', __name__)


class Env(Resource):
    def __init__(self):
        pass

    @timer
    def post(self, action):
        data = get_request_json()

        if action == 'add':
            try:
                env_name = data.pop('envName')
                base_host = data.pop('baseHost')
                dubbo_zookeeper = data.pop('dubboZookeeper')
                mq_key = data.pop('mqKey')
                db_connect = data.pop('dbConnect')
                remote_host = data.pop('remoteHost')
                disconf_host = data.pop('disconfHost')
                redis_connect = data.pop('redisConnect')
                simple_desc = data.pop('simpleDesc',None)
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

            pim = EnvInfoManager()

                # 判断env_name是否存在
            if  pim.is_env_name_exist(env_name):
                return make_response({"code": "201", "desc": "环境配置已存在"})

                # 针对入参进行入库
            pim.insert_env(env_name=env_name, base_host=base_host, dubbo_zookeeper=dubbo_zookeeper, mq_key=mq_key,
                           db_connect=db_connect, remote_host=remote_host, disconf_host= disconf_host, redis_connect=redis_connect, simple_desc=simple_desc)
            return make_response({"code": "000", "desc": "系统增加成功"})


        elif action == 'edit':
            try:
                id_ = data.pop('id')
                env_name = data.pop('envName')
                base_host = data.pop('baseHost')
                dubbo_zookeeper = data.pop('dubboZookeeper')
                mq_key = data.pop('mqKey')
                db_connect = data.pop('dbConnect')
                remote_host = data.pop('remoteHost')
                disconf_host = data.pop('disconfHost')
                redis_connect = data.pop('redisConnect')
                simple_desc = data.pop('simpleDesc')
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

            pim = EnvInfoManager()

# 判断修改数据是否存在

            if not pim.is_env_id_exist(id_):
                return make_response({"code": "200", "desc": "环境ID不存在,无法修改"})

# 根据入参进行数据修改

            pim.update_env(id_, env_name=env_name, base_host=base_host, dubbo_zookeeper=dubbo_zookeeper, mq_key=mq_key,
                           db_connect=db_connect, remote_host=remote_host, disconf_host= disconf_host, redis_connect=redis_connect, simple_desc=simple_desc)
            return make_response({"code": "000", "desc": "环境配置修改成功"})

        elif action == 'delete':
            try:
                id_ = data.pop('id')
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

            pim = EnvInfoManager()

            # 判断修改数据是否存在

            if not pim.is_env_id_exist(id_):
                return make_response({"code": "200", "desc": "环境不存在,无法删除"})

            # 根据入参进行数据修改

            pim.delete_env(id_)
            return make_response({"code": "000", "desc": "环境配置删除成功"})

        elif action == 'detail':
            pass

        elif action == 'list':
            # 查询列表入参可以为空或者输入项目名称
            try:
                env_name = data.pop('envName', None)
                pim = EnvInfoManager()

                # 判断入参有环境名时，是否可以查询
                if env_name:
                    if not pim.is_env_name_exist(env_name):
                        return make_response({"code": "000", "desc": []})

                result1 = pim.env_info(env_name)
                desc_list = []
                envs = []

                # 循环查询env返回所有的env数据，并将其加入list 方便遍历
                for i in result1:
                    envs.append([i.id, i.env_name, i.base_host, i.dubbo_zookeeper, i.mq_key, i.db_connect, i.remote_host, i.disconf_host, i.redis_connect, i.simple_desc])

                print(envs)
                # 遍历project_list 并将其添加到字典中，并对字段赋值
                for j in envs:
                    env_dict = {}
                    env_dict["id"] = j[0]
                    env_dict["envName"] = j[1]
                    env_dict["baseHost"] = j[2]
                    env_dict["dubboZookeeper"] = j[3]
                    env_dict["mqKey"] = j[4]
                    env_dict["dbConnect"] = j[5]
                    env_dict["remoteHost"] = j[6]
                    env_dict["disconfHost"] = j[7]
                    env_dict["redisConnect"] = j[8]
                    env_dict["simpleDesc"] = j[9]
                    desc_list.append(env_dict)
                # 将desc_list 根据项目名进行排序
                desc_list.sort(key=lambda desc_sort: (desc_sort.get("envName", 0)))
                return make_response({"code": "000", "desc":desc_list})
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})

        else:
            return make_response({"code": "100", "desc": "url错误，不存在的接口动作<{action}>".format(action=action)})

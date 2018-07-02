# -*- coding:utf-8 -*-
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

            if pim.is_env_id_exist(id_):
                return make_response({"code": "200", "desc": "环境配置不存在,无法修改"})

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

            if pim.is_env_id_exist(id_):
                return make_response({"code": "200", "desc": "环境不存在,无法删除"})

            # 根据入参进行数据修改

            pim.delete_env(id_)
            return make_response({"code": "000", "desc": "环境配置删除成功"})

        elif action == 'detail':
            pass

        elif action == 'list':
            logger.debug("This is debug information")
            all_envs = EnvInfo.query.all()
            return make_response({"code": "666", "message": u"测试一下，demo all right", "result": all_envs})

        else:
            return make_response({"code": "100", "desc": "url错误，不存在的接口动作<{action}>".format(action=action)})

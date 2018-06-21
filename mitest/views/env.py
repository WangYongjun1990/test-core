# -*- coding:utf-8 -*-
import json

from flask import Blueprint
from flask_restful import Resource

from mitest.models.mitest_platform import EnvInfo
from mitest.api.comm_log import logger
from mitest.views.wrappers import timer
from mitest.utils.common import get_request_json, make_response

env = Blueprint('env_interface', __name__)


class Env(Resource):
    def __init__(self):
        pass

    @timer
    def post(self, action):
        data = get_request_json()

        if action == 'add':
            pass

        elif action == 'edit':
            pass

        elif action == 'delete':
            pass

        elif action == 'detail':
            pass

        elif action == 'list':
            logger.debug("This is debug information")
            all_envs = EnvInfo.query.all()
            return make_response({"code": "666", "message": u"测试一下，demo all right", "result": all_envs})

        else:
            return make_response({"code": "100", "desc": "url错误，不存在的接口动作<{action}>".format(action=action)})

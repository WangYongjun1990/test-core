# -*- coding:utf-8 -*-

from flask import Blueprint
from flask_restful import Resource
from flask import request
from flask import jsonify

from mitest.models.mitest_platform import EnvInfo
from mitest.api.comm_log import logger

env = Blueprint('env_interface', __name__)


class Env(Resource):
    def __init__(self):
        pass

    def get(self):
        all_users = EnvInfo.query.all()
        logger.debug("This is debug information")
        logger.info('all_users:{0} \n type:{1}'.format(all_users, type(all_users)))

        response = jsonify(
            {"code": "666", "message": u"测试一下，demo all right", "result": str(all_users)}
        )

        return response
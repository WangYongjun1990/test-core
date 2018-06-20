# -*- coding:utf-8 -*-

"""
File Name: `db_action`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/13 14:09
"""

from flask import Blueprint
from flask_restful import Resource
from flask import request
from flask import jsonify

from mitest.models.mitest_platform import EnvInfo
from mitest.api.comm_log import logger

# 蓝图
db_action = Blueprint('db_action_interface', __name__)


class DbAction(Resource):
    def __init__(self):
        pass

    def post(self):
        all_users = EnvInfo.query.all()
        logger.debug("This is debug information")
        logger.info('all_users:{0} \n type:{1}'.format(all_users, type(all_users)))

        response = jsonify(
            {"code": "666", "message": u"测试一下，demo all right", "result": str(all_users)}
        )

        return response

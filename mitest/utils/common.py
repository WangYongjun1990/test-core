# -*- coding:utf-8 -*-

"""
File Name: `common`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/21 14:39
"""
import json

from flask import request
from flask import jsonify

from mitest.api.comm_log import logger


def get_request_json():
    data = request.get_json()
    logger.info('<Request> url= {url}, body= {body}'.format(url=request.url, body=json.dumps(data)))
    return data


def make_response(response_dict):
    logger.info("<Response> body= {body}".format(body=json.dumps(response_dict, ensure_ascii=False)))
    return jsonify(response_dict)

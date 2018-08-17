# -*- coding:utf-8 -*-

"""
File Name: `common`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/21 14:39
"""
import json
import re

from flask import request
from flask import jsonify

from mitest.api.comm_log import logger
from mitest.utils.tools import json_dumps
from mitest.config.default import get_config

CONFIG = get_config()


def get_request_json():
    data = request.get_json()
    logger.info('<Request> url= {url}, body= {body}'.format(url=request.url, body=json.dumps(data, ensure_ascii=False)))
    return data


def make_response(response_dict):
    logger.info("<Response> body= {body}".format(body=json.dumps(response_dict, ensure_ascii=False)))
    return jsonify(response_dict)


def read_custom():
    function_name_pattern = r'def ([\w_]+)\('
    function_description_pattern = r'    """ ([\w_]+)'
    custom_type_pattern = r'""" custom ([\w_-]+)'
    custom = {}
    custom_type = None
    function_name = None
    with open(CONFIG.CUSTOM_FILE, mode='r', encoding='utf8') as f:
        for line in f:
            if line.startswith('""" custom '):
                # 自定义函数类型
                custom_type = re.findall(custom_type_pattern, line)[0]
                custom[custom_type] = []
                continue
            elif line.startswith('def '):
                # 自定义函数名称
                function_name = re.findall(function_name_pattern, line)[0]
                custom[custom_type].append({"name": function_name})
                continue
            elif line.startswith('    """ '):
                # 自定义函数描述
                function_description = re.findall(function_description_pattern, line)[0]
                for func in custom[custom_type]:
                    if func['name'] == function_name:
                        func['description'] = function_description
                        break
                continue

    # print(json_dumps(custom))
    return custom


if __name__ == '__main__':
    read_custom()

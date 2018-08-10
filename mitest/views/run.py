# -*- coding:utf-8 -*-

"""
File Name: `run`.py
Version:
Description:

Author: wangyongjun
Date: 2018/8/7 13:44
"""
import json

from flask import Blueprint
from flask_restful import Resource

from mitest.api.comm_log import logger
from mitest.engine.exceptions import LoadCaseError, RunCaseError
from mitest.engine.run_test import run_test
from mitest.views.wrappers import timer
from mitest.utils.common import get_request_json, make_response

run = Blueprint('run_interface', __name__)


class Run(Resource):
    def __init__(self):
        pass

    @timer
    def post(self):
        data = get_request_json()

        try:
            testcase_id_list = data.pop("testcaseList", None)
            testsuite_id_list = data.pop("testsuiteList", None)
            module_id_list = data.pop("moduleList", None)
            system_id_list = data.pop("systemList", None)
            env_name = data["env"]
        except KeyError:
            return make_response({"code": "100", "desc": "入参校验失败"})

        kwargs = {
            "env_name": env_name,
        }
        if testcase_id_list:
            kwargs["testcase_id_list"] = testcase_id_list
        elif testsuite_id_list:
            kwargs["testsuite_id_list"] = testsuite_id_list
        elif module_id_list:
            kwargs["module_id_list"] = module_id_list
        elif system_id_list:
            kwargs["system_id_list"] = system_id_list

        try:
            report_path = run_test(**kwargs)
        except LoadCaseError:
            return make_response({"code": "200", "desc": "组装用例时出错"})
        except RunCaseError:
            return make_response({"code": "200", "desc": "执行用例时出错"})

        return make_response({"code": "000", "desc": "{report_path}".format(report_path=report_path)})
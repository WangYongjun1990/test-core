# -*- coding:utf-8 -*-

"""
File Name: `report`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/21 13:44
"""
import json

from flask import Blueprint
from flask_restful import Resource

from mitest.api.comm_log import logger
from mitest.views.wrappers import timer
from mitest.utils.common import get_request_json, make_response
from mitest.api.mysql_manager import TestReportManager

module = Blueprint('report_interface', __name__)
import mitest.config.sit
from flask import Flask

Flask(__name__).config.from_object(mitest.config.sit)


class Module(Resource):
    def __init__(self):
        pass

    @timer
    def post(self, action):
        data = get_request_json()
        if action == 'queryAutotestDetails':
            try:
                system_id = data["system_id"]
                pageNo = data["pageNo"]
                pageSize = data["pageSize"]
            except KeyError:
                return make_response({"code": "100", "desc": "入参校验失败"})
            res_testreport = TestReportManager.query_testreport(system_id=system_id)
            #组装出参tableData
            list_testreport = list()
            for i in res_testreport:
                dict_testreport = dict()
                dict_testreport["start_at"] = i.start_at
                dict_testreport["duration"] = i.duration
                dict_testreport["status"] = i.status
                dict_testreport["url"] = i.url
                list_testreport.append(dict_testreport)
            #按测试开始时间倒叙展示
            list_testreport.sort(key=lambda x:x["start_at"])
            #分页起始行
            begin = (pageNo - 1) * pageSize
            #分页结束行
            end = pageNo * pageSize
            if (begin > len(res_testreport)):
                return make_response({"code": "200", "desc": "起始行数大于测试报告总条数"})
            if (end < len(res_testreport)):   #若分页结束行小于列表大小，截取到end
                list_testreport_ = list_testreport[begin : end]
            else:   #若分页结束行小于列表大小，截取到列表末尾
                list_testreport_ = list_testreport[begin: len(res_testreport)]
            return make_response({"code": "000","totalNum":len(res_testreport), "tableData":list_testreport_})
        else:
            return make_response({"code": "100", "desc": "url错误，不存在的接口动作<{action}>".format(action=action)})
if __name__ == '__main__':
    Module = Module()
    res = Module.post("queryAutotestDetails")
    print(res)
# -*- coding:utf-8 -*-

"""
File Name: `handle_testcase`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/26 15:26
"""
import json
import re

from mitest.api.mysql_manager import TestcaseInfoManager

variable_pattern = r'\${([\w_]+)}'


def change_variable_format(request):
    """
    e.g.
        "json": {"pageSize": "${pageSize}"} => "json": {"pageSize": "$pageSize"}

    :param request:
    :return:
    """
    variables_list = re.findall(variable_pattern, request)

    for variable in variables_list:
        request = request.replace("${{{variable}}}".format(variable=variable), "${variable}".format(variable=variable),
                                  1)
    return request


def handle_testcase(action, **kwargs):
    """
    :param action:
    :param kwargs:
    :return:
    """
    if action == 'add':
        testcase_name = kwargs.get("name")
        testsuite_id = kwargs.pop("testsuiteId")
        module_id = kwargs.pop("moduleId")
        system_id = kwargs.pop("systemId")

        if "config" not in kwargs:
            kwargs['config'] = {
                "request": {
                    "base_url": "",
                    "headers": {"Content-Type": "application/json;charset=UTF-8"},
                }
            }
        request = json.dumps(kwargs, ensure_ascii=False)

        request = change_variable_format(request)

        TestcaseInfoManager.insert_testcase(
            testcase_name=testcase_name,
            type='1',
            request=request,
            testsuite_id=testsuite_id,
            module_id=module_id,
            system_id=system_id,
        )

    elif action == 'edit':
        pass

    elif action == 'delete':
        testcase_id = kwargs.pop('testcaseId', None)
        if not testcase_id:
            pass

        TestcaseInfoManager.delete_testcase(testcase_id)


if __name__ == '__main__':
    handle_testcase('delete', testcaseId='10')
    input = {
        "testsuiteId": "1",
        "moduleId": "4",
        "systemId": "1",
        "name": "用例名称A",
        "testcases": [
            {
                "name": "步骤-1",
                "request": {
                    "method": "POST",
                    "headers": {
                        "Content-Type": "application/json",
                        "oops": "oops"
                    },
                    "url": "/mock/config/queryMock",
                    "json": {"pageSize": "${pageSize}", "interfaceName": "${interfaceName}", "currentPage": 1, "projectName": "ups"},
                },
                "variables": [
                    {"pageSize": 2},
                    {"interfaceName": "demo_post_json"},
                ],
                "validate": [
                    {"eq": ["content.code", "000"]},
                ],
                "extract": [
                    {"tableData": "content.tableData"},
                ]
            },
        ]
    }
    # handle_testcase('add', **input)

# -*- coding:utf-8 -*-

"""
File Name: `run_test`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/22 下午9:49
"""
import copy
import json
import time

from mitest.httprunner import HttpRunner
from mitest.engine.exceptions import RunCaseError, LoadCaseError
from mitest.engine.load_test import load_test
from mitest.engine.report import perfect_summary, save_report
from mitest.config.default import get_config
from mitest.utils.tools import json_dumps

config = get_config()


def run_test(**kwargs):
    res = load_test(**kwargs)
    testset = res[0]
    test_meta_list = res[1]

    if not testset:
        raise LoadCaseError('没有可执行的用例')

    print("{1} testset:{0}".format(testset, type(testset)))
    tmp = testset[0]
    print(json_dumps(tmp))
    try:
        # summary = run(testset, report_name='testMock')
        kwargs = {
            "failfast": False,
        }
        runner = HttpRunner(**kwargs)
        start_time = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        runner.run(testset)
        perfect_summary(runner.summary, test_meta_list)
        print(runner.summary)
        runner_summary = copy.deepcopy(runner.summary)
        report_path = runner.gen_html_report(
            html_report_name='default',
            html_report_template=config.REPORT_TEMPLATE_PATH
        )
        print('report_path:{}'.format(report_path))
    except Exception:
        raise RunCaseError

    save_report(report_path, runner_summary)
    return report_path


if __name__ == '__main__':
    kwargs = {
        "testcase_id_list": ['16'],
        # "testcase_id_list": ['1', '2', '3'],
        "env_name": "mock",
        # "testsuite_id_list": ['1'],
        # "module_id_list": ['4'],
    }
    run_test(**kwargs)
    # run_test(testcase_id='1', env_ name='mo2ck')
    testset = {
            "name": "myMock",
            "config": {
                "request": {
                    "base_url": "http://99.48.58.241",
                    "headers": {
                        "Content-Type": "application/json;charset=UTF-8"
                    }
                },
                "variables": [
                    {"pageSize": 1},
                    {"currentPage": 1}
                ],
                "parameters": [],
                "name": "testset description"
            },
            "testcases": [
                {
                    "request": {
                        "json": {},
                        "url": "mock/config/queryProject",
                        "headers": {"Content-Type": "application/json"},
                        "method": "POST"
                    },
                    "extract": [
                        {
                            "op": "content.desc.ups.0"
                        }
                    ],
                    "validate": [
                        {
                            "eq": [
                                "status_code",
                                200
                            ]
                        },
                        {
                            "eq": [
                                "headers.Content-Type",
                                "application/json"
                            ]
                        },
                        {
                            "eq": [
                                "content.desc",
                                {"bds": [], "capital": ["businessapi/ops/file/upload/2/xydadcce31a92e8b1c5",
                                                        "mm/credit/getUnderWrittingStatus",
                                                        "mm/credit/getUnderWrittingStatus/2/xydadcce31a92e8b1c5",
                                                        "mm/credit/queryAccountInfo",
                                                        "mm/credit/queryAccountInfo/2/xydadcce31a92e8b1c5",
                                                        "mm/credit/saveUserInfo/2/xydadcce31a92e8b1c5",
                                                        "mm/credit/withdrawDeposit/2"],
                                 "ups": ["demo_get", "demo_post", "demo_post_form", "demo_post_json"]}
                            ]
                        }
                    ],
                    "variables": [],
                    "name": "queryProject"
                },
                {
                    "request": {
                        "json": {
                            "pageSize": "$pageSize",
                            "interfaceName": "demo_post_json",
                            "currentPage": "$currentPage",
                            "projectName": "ups",
                            "op": "$op"
                        },
                        "url": "http://99.48.58.241/mock/config/queryMock",
                        "headers": {},
                        "method": "POST"
                    },
                    "extract": [
                        {
                            "tableData": "content.tableData"
                        }
                    ],
                    "validate": [
                        {
                            "eq": [
                                "status_code",
                                200
                            ]
                        },
                        {
                            "eq": [
                                "headers.Content-Type",
                                "application/json"
                            ]
                        },
                        {
                            "eq": [
                                "content.code",
                                "000"
                            ]
                        }
                    ],
                    "variables": [],
                    "name": "queryMock"
                }
            ]
        }

    # run_test(testset, 'myReport')

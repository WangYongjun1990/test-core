# -*- coding:utf-8 -*-

"""
File Name: `report`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/22 下午9:50
"""


def perfect_summary(summary, test_meta_list):
    # summary['stat']['successes'] = 996
    step_list = []
    for testcase in test_meta_list:
        step_list.extend(testcase['step'])

    print(step_list)

    assert len(step_list) == len(summary['records'])

    for step in summary['records']:
        step_meta = step_list.pop(0)
        step['testcase_name'] = step_meta['testcase_name']
        if 'error_detail' in step_meta:
            pass


if __name__ == '__main__':
    test_meta_list = [
        {
            "id": 1,
            "testcase_name": "nameA",
            "step": [
                {
                    "testcase_name": "nameA",
                    "step_name": "namea",
                    "error_detail": ""
                },
                {
                    "testcase_name": "nameA",
                    "step_name": "nameb",
                    "error_detail": ""
                }
            ]
        },
        {
            "id": 2,
            "testcase_name": "nameB",
            "step": [
                {
                    "testcase_name": "nameB",
                    "step_name": "namec",
                    "error_detail": ""
                },
                {
                    "testcase_name": "nameB",
                    "step_name": "named",
                    "error_detail": ""
                }
            ]
        }
    ]

    perfect_summary({}, test_meta_list)

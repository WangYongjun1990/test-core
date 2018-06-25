# -*- coding:utf-8 -*-

"""
File Name: `load_test`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/22 下午9:48
"""
import json

from mitest.api.mysql_manager import TestcaseInfoManager
from mitest.engine.exceptions import JSONDecodeError, LoadCaseError
from mitest.models.mitest_platform import EnvInfo


def load_test(**kwargs):
    env_name = kwargs.pop('env_name')
    testcase_id = kwargs.pop('testcase_id', None)
    testcase_id_list = kwargs.pop('testcase_id_list', None)

    obj = EnvInfo.query.filter_by(env_name=env_name).first()
    try:
        base_host = obj.base_host
    except AttributeError:
        raise LoadCaseError('No Base Host')

    if testcase_id:
        testset = get_testcase_by_id(testcase_id)

        if 'config' in testset:
            testset['config']['request']['base_url'] = base_host

        return testset

    elif testcase_id_list and isinstance(testcase_id_list, list):
        testset_list = []
        for testcase_id in testcase_id_list:
            testset = get_testcase_by_id(testcase_id)

            if 'config' in testset:
                testset['config']['request']['base_url'] = base_host

            testset_list.append(testset)

        return testset_list


def get_testcase_by_id(testcase_id):
    testcase_info = TestcaseInfoManager.get_testcase(testcase_id)
    try:
        testset_str = testcase_info.request
    except AttributeError:
        raise LoadCaseError('testcase_id:{} Not Found In Database'.format(testcase_id))
    try:
        testset = json.loads(testset_str)
    except JSONDecodeError:
        raise LoadCaseError('Json Load testcase_info.request Error')

    return testset

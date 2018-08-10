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
from mitest.models.mitest_platform import EnvInfo, TestcaseInfo
from mitest.api.comm_log import logger


def load_test(**kwargs):
    """
    加载用例，返回testset字典或testset字典的列表
    :param kwargs:
    :return:
    """
    env_name = kwargs.pop('env_name')
    testcase_id = kwargs.pop('testcase_id', None)
    testcase_id_list = kwargs.pop('testcase_id_list', None)
    testsuite_id_list = kwargs.pop('testsuite_id_list', None)
    module_id_list = kwargs.pop('module_id_list', None)
    system_id_list = kwargs.pop('system_id_list', None)

    obj = EnvInfo.query.filter_by(env_name=env_name).first()
    try:
        base_host = obj.base_host
    except AttributeError:
        raise LoadCaseError('No Base Host')

    test_meta_list = []
    if testcase_id:
        obj = TestcaseInfo.query.filter_by(id=testcase_id).first()
        testset = get_testset_from_obj(obj)
        testset = add_base_host(testset, base_host)
        meta_data = get_meta(obj, testset)
        test_meta_list.append(meta_data)

        return [[testset], test_meta_list]

    elif testcase_id_list and isinstance(testcase_id_list, list):
        testset_list = []
        for testcase_id in testcase_id_list:
            obj = TestcaseInfo.query.filter_by(id=testcase_id).first()
            if not obj:
                continue
            testset = get_testset_from_obj(obj)
            testset = add_base_host(testset, base_host)
            testset_list.append(testset)
            meta_data = get_meta(obj, testset)
            test_meta_list.append(meta_data)

        return [testset_list, test_meta_list]

    elif testsuite_id_list and isinstance(testsuite_id_list, list):
        testset_list = []
        for testsuite_id in testsuite_id_list:
            obj_list = TestcaseInfo.query.filter_by(testsuite_id=testsuite_id).all()

            for obj in obj_list:
                testset = get_testset_from_obj(obj)
                testset = add_base_host(testset, base_host)
                testset_list.append(testset)
                meta_data = get_meta(obj, testset)
                test_meta_list.append(meta_data)

        return [testset_list, test_meta_list]

    elif module_id_list and isinstance(module_id_list, list):
        testset_list = []
        for module_id in module_id_list:
            obj_list = TestcaseInfo.query.filter_by(module_id=module_id).all()

            for obj in obj_list:
                testset = get_testset_from_obj(obj)
                testset = add_base_host(testset, base_host)
                testset_list.append(testset)

        return [testset_list, test_meta_list]

    elif system_id_list and isinstance(system_id_list, list):
        testset_list = []
        for system_id in system_id_list:
            obj_list = TestcaseInfo.query.filter_by(system_id=system_id).all()

            for obj in obj_list:
                testset = get_testset_from_obj(obj)
                testset = add_base_host(testset, base_host)
                testset_list.append(testset)

        return [testset_list, test_meta_list]


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


def add_base_host(testset, base_host):
    """
    给testset增加base_host
    :param testset:
    :param base_host:
    :return:
    """
    if 'config' in testset:
        testset['config']['request']['base_url'] = base_host
    return testset


def get_testset_from_obj(obj):
    """
    从数据库对象obj中获取request值，并转成dict格式
    :param obj:
    :return:
    """
    testset_str = obj.request
    try:
        return json.loads(testset_str)
    except JSONDecodeError:
        raise LoadCaseError('Json Load testcase_info.request Error')


def get_meta(obj, testset):
    meta_dict = {'id': obj.id, 'testcase_name': obj.testcase_name, 'step': []}
    for step in testset['testcases']:
        meta_dict['step'].append({'testcase_name': obj.testcase_name, 'step_name': step['name']})

    return meta_dict



# -*- coding:utf-8 -*-

"""
File Name: `mysql_manager`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/21 15:37
"""

from mitest import db
from mitest.models.mitest_platform import EnvInfo, ProjectInfo, SystemInfo, TestsuiteInfo, TestcaseInfo, ModuleInfo


class EnvInfoManager(object):
    @staticmethod
    def insert_env(**kwargs):
        obj = EnvInfo(**kwargs)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def update_env(id_, **kwargs):
        obj = EnvInfo.query.filter_by(id=id_).first()
        obj.env_name = kwargs.pop('env_name')
        obj.base_host = kwargs.pop('base_host', None)
        obj.dubbo_zookeeper = kwargs.pop('dubbo_zookeeper', None)
        obj.mq_key = kwargs.pop('mq_key', None)
        obj.db_connect = kwargs.pop('db_connect', None)
        obj.remote_host = kwargs.pop('remote_host', None)
        obj.disconf_host = kwargs.pop('disconf_host', None)
        obj.redis_connect = kwargs.pop('redis_connect', None)
        obj.simple_desc = kwargs.pop('simple_desc', None)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def delete_env(id_):
        obj = EnvInfo.query.filter_by(id=id_).first()
        db.session.delete(obj)
        db.session.commit()


class ProjectInfoManager(object):
    @staticmethod
    def insert_project(**kwargs):
        obj = ProjectInfo(**kwargs)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def update_project(id_, **kwargs):
        obj = ProjectInfo.query.filter_by(id=id_).first()
        obj.project_name = kwargs.pop('project_name')
        obj.simple_desc = kwargs.pop('simple_desc', None)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def delete_project(id_):
        obj = ProjectInfo.query.filter_by(id=id_).first()
        db.session.delete(obj)
        db.session.commit()

    @staticmethod
    def is_project_name_exist(project_name):
        obj = ProjectInfo.query.filter_by(project_name=project_name).first()
        if obj:
            return True
        else:
            return False


class SystemInfoManager(object):
    @staticmethod
    def insert_system(**kwargs):
        obj = SystemInfo(**kwargs)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def update_system(id_, **kwargs):
        obj = SystemInfo.query.filter_by(id=id_).first()
        obj.system_name = kwargs.pop('system_name')
        obj.test_user = kwargs.pop('test_user', None)
        obj.dev_user = kwargs.pop('dev_user', None)
        obj.publish_app = kwargs.pop('publish_app', None)
        obj.simple_desc = kwargs.pop('simple_desc', None)
        obj.project_id = kwargs.pop('project_id', None)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def delete_system(id_):
        obj = SystemInfo.query.filter_by(id=id_).first()
        db.session.delete(obj)
        db.session.commit()


class ModuleInfoManager(object):
    @staticmethod
    def insert_module(**kwargs):
        obj = ModuleInfo(**kwargs)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def update_module(id_, **kwargs):
        obj = ModuleInfo.query.filter_by(id=id_).first()
        obj.module_name = kwargs.pop('module_name')
        obj.test_user = kwargs.pop('test_user', None)
        obj.simple_desc = kwargs.pop('simple_desc', None)
        obj.system_id = kwargs.pop('system_id', None)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def delete_module(id_):
        obj = ModuleInfo.query.filter_by(id=id_).first()
        db.session.delete(obj)
        db.session.commit()


class TestsuiteInfoManager(object):
    @staticmethod
    def insert_testsuite(**kwargs):
        obj = TestsuiteInfo(**kwargs)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def update_testsuite(id_, **kwargs):
        obj = TestsuiteInfo.query.filter_by(id=id_).first()
        obj.testsuite_name = kwargs.pop('testsuite_name')
        obj.simple_desc = kwargs.pop('simple_desc', None)
        obj.module_id = kwargs.pop('module_id', None)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def delete_testsuite(id_):
        obj = TestsuiteInfo.query.filter_by(id=id_).first()
        db.session.delete(obj)
        db.session.commit()


class TestcaseInfoManager(object):
    @staticmethod
    def insert_testcase(**kwargs):
        obj = TestcaseInfo(**kwargs)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def update_testcase(id_, **kwargs):
        obj = TestcaseInfo.query.filter_by(id=id_).first()
        obj.testcase_name = kwargs.pop('testcase_name')
        obj.type = kwargs.pop('type')
        obj.include = kwargs.pop('include', None)
        obj.request = kwargs.pop('request')
        obj.testsuite_id = kwargs.pop('testsuite_id', None)
        obj.module_id = kwargs.pop('module_id', None)
        obj.system_id = kwargs.pop('system_id', None)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def delete_testcase(id_):
        obj = TestcaseInfo.query.filter_by(id=id_).first()
        db.session.delete(obj)
        db.session.commit()
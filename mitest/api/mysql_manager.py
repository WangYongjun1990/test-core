# -*- coding:utf-8 -*-

"""
File Name: `mysql_manager`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/21 15:37
"""
from mitest import db
from mitest.models.mitest_platform import (
    EnvInfo, ProjectInfo, SystemInfo, TestsuiteInfo, TestcaseInfo, ModuleInfo, TestReport
)


class EnvInfoManager(object):
    @staticmethod
    def insert_env(**kwargs):
        obj = EnvInfo(**kwargs)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def update_env(id_, **kwargs):
        obj = EnvInfo.query.filter_by(id=id_).first()
        for column in kwargs:
            obj = obj_set_value(obj, column, kwargs[column])
        # obj.env_name = kwargs.pop('env_name')
        # obj = obj_set_value(obj, 'base_host', kwargs.pop('base_host', None))
        # obj = obj_set_value(obj, 'dubbo_zookeeper', kwargs.pop('dubbo_zookeeper', None))
        # obj = obj_set_value(obj, 'mq_key', kwargs.pop('mq_key', None))
        # obj = obj_set_value(obj, 'db_connect', kwargs.pop('db_connect', None))
        # obj = obj_set_value(obj, 'remote_host', kwargs.pop('remote_host', None))
        # obj = obj_set_value(obj, 'disconf_host', kwargs.pop('disconf_host', None))
        # obj = obj_set_value(obj, 'simple_desc', kwargs.pop('simple_desc', None))
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def delete_env(id_):
        obj = EnvInfo.query.filter_by(id=id_).first()
        db.session.delete(obj)
        db.session.commit()

    @staticmethod
    def env_info(env_name=None):
        if env_name:
            obj = EnvInfo.query.filter_by(env_name=env_name)
        else:
            obj = EnvInfo.query.all()

        return obj

    @staticmethod
    def is_env_id_exist(id):
        obj = EnvInfo.query.filter_by(id=id).first()
        if obj:
            return True
        else:
            return False

    @staticmethod
    def is_env_name_exist(name):
        obj = EnvInfo.query.filter_by(env_name=name).first()
        if obj:
            return True
        else:
            return False


class ProjectInfoManager(object):
    @staticmethod
    def insert_project(**kwargs):
        obj = ProjectInfo(**kwargs)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def update_project(id_, **kwargs):
        obj = ProjectInfo.query.filter_by(id=id_).first()
        for column in kwargs:
            obj = obj_set_value(obj, column, kwargs[column])
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def delete_project(id_):
        obj = ProjectInfo.query.filter_by(id=id_).first()
        db.session.delete(obj)
        db.session.commit()

    @staticmethod
    def is_project_name_exist(project_name):
        project_name = '%' + project_name + '%'
        obj = ProjectInfo.query.filter(ProjectInfo.project_name.like(project_name)).first()
        if obj:
            return True
        else:
            return False

    @staticmethod
    def is_project_name_exist_for_update(project_name):
        obj = ProjectInfo.query.filter_by(project_name=project_name).first()
        if obj:
            return True
        else:
            return False

    @staticmethod
    def is_project_name_exist_union(id, project_name):
        obj = ProjectInfo.query.filter_by(project_name=project_name, id=id).first()
        if obj:
            return True
        else:
            return False

    @staticmethod
    def is_project_id_exist(id):
        obj = ProjectInfo.query.filter_by(id=id).first()
        if obj:
            return True
        else:
            return False

    @staticmethod
    def project_info(project_name):
        if project_name == "":
            obj = ProjectInfo.query.all()
        else:
            project_name = '%' + project_name + '%'
            obj = ProjectInfo.query.filter(ProjectInfo.project_name.like(project_name)).all()

        return obj

    @staticmethod
    def system_info(id_):

        obj = SystemInfo.query.filter_by(project_id=id_).all()

        return obj

    @staticmethod
    def select_id_by(project_name):
        obj = ProjectInfo.query.filter_by(project_name=project_name).first()

        return obj.id


class SystemInfoManager(object):
    @staticmethod
    def insert_system(**kwargs):
        obj = SystemInfo(**kwargs)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def update_system(id_, **kwargs):
        obj = SystemInfo.query.filter_by(id=id_).first()
        for column in kwargs:
            obj = obj_set_value(obj, column, kwargs[column])
        # obj.system_name = kwargs.pop('system_name')
        # obj.test_user = kwargs.pop('test_user', None)
        # obj.dev_user = kwargs.pop('dev_user', None)
        # obj.publish_app = kwargs.pop('publish_app', None)
        # obj.simple_desc = kwargs.pop('simple_desc', None)
        # obj.project_id = kwargs.pop('project_id', None)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def delete_system(id_):
        obj = SystemInfo.query.filter_by(id=id_).first()
        db.session.delete(obj)
        db.session.commit()

    @staticmethod
    def is_system_name_exist(system_name):
        obj = SystemInfo.query.filter_by(system_name=system_name).first()
        if obj:
            return True
        else:
            return False

    @staticmethod
    def is_project_id_exist(project_id):
        obj = ProjectInfo.query.filter_by(id=project_id).first()
        if obj:
            return True
        else:
            return False

    @staticmethod
    def is_system_id_exist(id):
        obj = SystemInfo.query.filter_by(id=id).first()
        if obj:
            return True
        else:
            return False

    @staticmethod
    def system_info(system_name):
        if system_name == "":
            obj = SystemInfo.query.all()
        else:
            system_name = '%' + system_name + '%'
            obj = SystemInfo.query.filter(SystemInfo.system_name.like(system_name)).all()

        return obj

    @staticmethod
    def project_info(id_):
        obj = ProjectInfo.query.filter_by(id=id_).all()
        return obj

    @staticmethod
    def select_by_project_id(project_id):
        obj = SystemInfo.query.filter_by(project_id=project_id).all()
        return obj


class ModuleInfoManager(object):
    @staticmethod
    def insert_module(**kwargs):
        obj = ModuleInfo(**kwargs)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def update_module(id_, **kwargs):
        obj = ModuleInfo.query.filter_by(id=id_).first()
        for column in kwargs:
            obj = obj_set_value(obj, column, kwargs[column])
        # obj.module_name = kwargs.pop('module_name')
        # obj.test_user = kwargs.pop('test_user', None)
        # obj.simple_desc = kwargs.pop('simple_desc', None)
        # obj.system_id = kwargs.pop('system_id', None)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def delete_module(id_):
        obj = ModuleInfo.query.filter_by(id=id_).first()
        db.session.delete(obj)
        db.session.commit()

    @staticmethod
    def query_module(system_id, module_name):
        obj = ModuleInfo.query.filter_by(system_id=system_id, module_name=module_name).all()
        return obj

    @staticmethod
    def query_module_id(id):
        obj = ModuleInfo.query.filter_by(id=id).all()
        return obj

    @staticmethod
    def query_all_module(system_id):
        obj = ModuleInfo.query.filter_by(system_id=system_id).all()
        return obj


class TestsuiteInfoManager(object):
    @staticmethod
    def insert_testsuite(**kwargs):
        obj = TestsuiteInfo(**kwargs)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def update_testsuite(id_, **kwargs):
        obj = TestsuiteInfo.query.filter_by(id=id_).first()
        for column in kwargs:
            obj = obj_set_value(obj, column, kwargs[column])
        # obj.testsuite_name = kwargs.pop('testsuite_name')
        # obj.simple_desc = kwargs.pop('simple_desc', None)
        # obj.module_id = kwargs.pop('module_id', None)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def delete_testsuite(id_):
        obj = TestsuiteInfo.query.filter_by(id=id_).first()
        db.session.delete(obj)
        db.session.commit()

    @staticmethod
    def query_all_testsuite(module_id):
        obj = TestsuiteInfo.query.filter_by(module_id=module_id).all()
        return obj

    @staticmethod
    def query_testsuite_by_id(id_):
        obj = TestsuiteInfo.query.filter_by(id=id_).first()
        return obj


class TestcaseInfoManager(object):
    @staticmethod
    def insert_testcase(**kwargs):
        obj = TestcaseInfo(**kwargs)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def update_testcase(id_, **kwargs):
        obj = TestcaseInfo.query.filter_by(id=id_).first()
        for column in kwargs:
            obj = obj_set_value(obj, column, kwargs[column])
        # obj.testcase_name = kwargs.pop('testcase_name')
        # obj.type = kwargs.pop('type')
        # obj.include = kwargs.pop('include', None)
        # obj.request = kwargs.pop('request')
        # obj.testsuite_id = kwargs.pop('testsuite_id', None)
        # obj.module_id = kwargs.pop('module_id', None)
        # obj.system_id = kwargs.pop('system_id', None)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def delete_testcase(id_):
        obj = TestcaseInfo.query.filter_by(id=id_).first()
        if obj:
            db.session.delete(obj)
            db.session.commit()

    @staticmethod
    def get_testcase(id_):
        obj = TestcaseInfo.query.filter_by(id=id_).first()
        return obj


class TestReportManager(object):
    @staticmethod
    def insert_testreport(**kwargs):
        obj = TestReport(**kwargs)
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def query_testreport(system_id):
        obj = TestReport.query.filter_by(system_id=system_id).all()
        return obj


def obj_set_value(obj, attr, value):
    if value is not None and hasattr(obj, attr):
        setattr(obj, attr, value)
    return obj


if __name__ == '__main__':
    # obj_set_value()
    pass

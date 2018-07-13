# -*- coding:utf-8 -*-

"""
File Name: `mitest_platform`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/19 17:41
"""

from mitest import db


class EnvInfo(db.Model):
    __tablename__ = 'env_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=db.func.now())
    update_time = db.Column(db.DateTime, onupdate=db.func.now())
    env_name = db.Column(db.String(50), nullable=False, unique=True)
    base_host = db.Column(db.String(50))
    dubbo_zookeeper = db.Column(db.String(50))
    mq_key = db.Column(db.String(100))
    db_connect = db.Column(db.String(200))
    remote_host = db.Column(db.String(50))
    disconf_host = db.Column(db.String(50))
    redis_connect = db.Column(db.String(200))
    simple_desc = db.Column(db.String(50))

    def __repr__(self):
        return '<EnvInfo %r, id %r>' % (self.env_name, self.id)


class TestReport(db.Model):
    __tablename__ = 'test_report'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=db.func.now())
    update_time = db.Column(db.DateTime, onupdate=db.func.now())
    start_at = db.Column(db.String(50))
    duration = db.Column(db.String(50))
    status = db.Column(db.String(50))
    run_type = db.Column(db.Integer)
    report = db.Column(db.Text(4294000000), nullable=False)
    url = db.Column(db.String(150))
    system_id = db.Column(db.Integer, db.ForeignKey('system_info.id'))
    url = db.Column(db.String(150))
    system = db.relationship('SystemInfo', backref=db.backref('test_reports'))

    def __repr__(self):
        return '<TestReport %r, id %r>' % (self.env_name, self.id)


class ProjectInfo(db.Model):
    __tablename__ = 'project_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=db.func.now())
    update_time = db.Column(db.DateTime, onupdate=db.func.now())
    project_name = db.Column(db.String(50), nullable=False, unique=True)
    simple_desc = db.Column(db.String(100))

    def __repr__(self):
        return '<ProjectInfo %r, id %r>' % (self.project_name, self.id)


class SystemInfo(db.Model):
    __tablename__ = 'system_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=db.func.now())
    update_time = db.Column(db.DateTime, onupdate=db.func.now())
    system_name = db.Column(db.String(50), nullable=False)
    test_user = db.Column(db.String(50))
    dev_user = db.Column(db.String(50))
    publish_app = db.Column(db.String(50))
    simple_desc = db.Column(db.String(100))
    project_id = db.Column(db.Integer, db.ForeignKey('project_info.id'))
    project = db.relationship('ProjectInfo', backref=db.backref('systems'))

    def __repr__(self):
        return '<SystemInfo %r, id %r>' % (self.system_name, self.id)


class ModuleInfo(db.Model):
    __tablename__ = 'module_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=db.func.now())
    update_time = db.Column(db.DateTime, onupdate=db.func.now())
    module_name = db.Column(db.String(80), nullable=False)
    test_user = db.Column(db.String(50))
    simple_desc = db.Column(db.String(100))
    system_id = db.Column(db.Integer, db.ForeignKey('system_info.id'))
    system = db.relationship('SystemInfo', backref=db.backref('modules'))

    def __repr__(self):
        return '<ModuleInfo %r, id %r>' % (self.module_name, self.id)


class TestsuiteInfo(db.Model):
    __tablename__ = 'testsuite_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=db.func.now())
    update_time = db.Column(db.DateTime, onupdate=db.func.now())
    testsuite_name = db.Column(db.String(80), nullable=False)
    simple_desc = db.Column(db.String(100))
    module_id = db.Column(db.Integer, db.ForeignKey('module_info.id'))
    module = db.relationship('ModuleInfo', backref=db.backref('testsuites'))

    def __repr__(self):
        return '<TestsuiteInfo %r, id %r>' % (self.testsuite_name, self.id)


class TestcaseInfo(db.Model):
    __tablename__ = 'testcase_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=db.func.now())
    update_time = db.Column(db.DateTime, onupdate=db.func.now())
    testcase_name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.Integer, default=0, nullable=False)
    include = db.Column(db.String(400))
    request = db.Column(db.Text, nullable=False)
    testsuite_id = db.Column(db.Integer, db.ForeignKey('testsuite_info.id'))
    module_id = db.Column(db.Integer, db.ForeignKey('module_info.id'))
    system_id = db.Column(db.Integer, db.ForeignKey('system_info.id'))
    testsuite = db.relationship('TestsuiteInfo', backref=db.backref('testcases'))
    module = db.relationship('ModuleInfo', backref=db.backref('testcases'))
    system = db.relationship('SystemInfo', backref=db.backref('testcases'))

    def __repr__(self):
        return '<TestcaseInfo %r, id %r>' % (self.testcase_name, self.id)
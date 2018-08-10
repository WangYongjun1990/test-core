# -*- coding:utf-8 -*-

"""
File Name: `__init__`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/13 14:07
"""

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from mitest.config.load_config import load_config

app = Flask(__name__)

current_config = load_config("SIT")
app.config.from_object(current_config)

# 创建1个SQLAlchemy实例
db = SQLAlchemy(app)

from .views import (
    env, Env,
    project, Project,
    system, System,
    module, Module,
    testsuite, Testsuite,
    testcase, Testcase,
    run, Run,
)

app.register_blueprint(env)
app.register_blueprint(project)
app.register_blueprint(system)
app.register_blueprint(module)
app.register_blueprint(testsuite)
app.register_blueprint(testcase)
app.register_blueprint(run)

view = Api(app)
view.add_resource(Env, '/env/<action>')
view.add_resource(Project, '/project/<action>')
view.add_resource(System, '/system/<action>')
view.add_resource(Module, '/module/<action>')
view.add_resource(Testsuite, '/testsuite/<action>')
view.add_resource(Testcase, '/testcase/<action>')
view.add_resource(Run, '/run')

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

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


from .views import db_action, DbAction
from .views import env, Env

app.register_blueprint(db_action)
app.register_blueprint(env)

view = Api(app)
view.add_resource(DbAction, '/db')
view.add_resource(Env, '/env/<action>')

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
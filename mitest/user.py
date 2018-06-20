# -*- coding:utf-8 -*-

"""
File Name: `user`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/12 11:41
"""
import json


from my_flask import db
from my_flask.models.mitest_platform import User, ProjectInfo, SystemInfo


def insert_user(**kwargs):
    new_obj = User(**kwargs)
    # new_obj = User(username=kwargs.get('username'),
    #                email=kwargs.get('email'),
    #                password=kwargs.get('password'))
    db.session.add(new_obj)
    db.session.commit()


def query_user(username):
    all_users = User.query.all()
    print('all_users:{0} \n type:{1}'.format(all_users, type(all_users)))

    user = User.query.filter_by(username=username).first()
    print('user:{0} \n type:{1}'.format(user, type(user)))

    if user:
        print(user.email)
        print(type(user.email))

        # dict_ = json.loads(user.email)
        # print(dict_)
        # print(type(dict_))
        #
        # print(user.id)


def update_user(**kwargs):
    user = User.query.filter_by(id=kwargs.pop('id')).first()
    dict_ = {"a": "123", "b": "我是中文31"}
    user.email = json.dumps(dict_, separators=(',', ':'), sort_keys=True, ensure_ascii=False)
    user.password = kwargs.pop('password')
    user.username = kwargs.pop('username')
    # user.email = json.dumps(dict_, indent=4, separators=(',', ': '), sort_keys=True, ensure_ascii=False)
    db.session.add(user)
    db.session.commit()


def delete_user(username):
    user = User.query.filter_by(username=username).first()
    db.session.delete(user)
    db.session.commit()


def insert_project(**kwargs):
    new_obj = ProjectInfo(**kwargs)
    db.session.add(new_obj)
    db.session.commit()


def insert_system(**kwargs):
    new_obj = SystemInfo(**kwargs)
    db.session.add(new_obj)
    db.session.commit()


if __name__ == '__main__':
    # query_user('用户E')
    # update_user(id=1, username='username哈哈', password='000999')
    # insert_user(username='用户B', email='23的1@21.com', password='16666d')
    # query_user('用户A')
    project = ProjectInfo.query.filter_by(project_name='宝生').first()
    print(project.id)
    # insert_system(system_name='wallet', project_id=project.id)
    # system = SystemInfo.query.filter_by(system_name='wallet').first()
    # print(system.project_id)

    print(project.systems)

    for system in project.systems:
        print('-' * 10)
        print(system.system_name)

    # insert_system(system_name='user-core', project=project)

    system_wallet = SystemInfo.query.filter_by(id='2').first()
    print(system_wallet.project)




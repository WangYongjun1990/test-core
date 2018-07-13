# -*- coding:utf-8 -*-

"""
File Name: `user`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/12 11:41
"""
import json
import time
import random

#from mitest import db
#from mitest.models.mitest_platform import User, ProjectInfo, SystemInfo


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


def gen_timestamp(time_flag, count):
    two_month_ago = 1525276800000
    one_month_ago = 1527955200000
    one_week_ago = 1530028800000
    one_day_ago = 1531065600000
    one_hour_aga = 1531208640000

    now = int(1000 * time.time())

    with open('data.txt', mode='w') as data_file:
        for _ in range(count):
            if time_flag == '2m':
                delta = random.randint(two_month_ago, now)
            elif time_flag == '2m+':
                delta = random.randint(two_month_ago, one_month_ago)
            elif time_flag == '1m':
                delta = random.randint(one_month_ago, now)
            elif time_flag == '1w':
                delta = random.randint(one_week_ago, now)
            elif time_flag == '1d':
                delta = random.randint(one_day_ago, now)
            elif time_flag == '1h':
                delta = random.randint(one_hour_aga, now)
            print(delta)
            data_file.write(str(delta)+'\n')

if __name__ == '__main__':
    gen_timestamp('1h', 150000)

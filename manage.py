# -*- coding:utf-8 -*-

"""
File Name: `manage`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/13 14:06
"""

from mitest import manager


if __name__ == '__main__':
    manager.run()


"""

# 启动Flask服务命令
python3 manage.py runserver -h 0.0.0.0 -p 7000 -d

# 升级数据库命令
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade

"""
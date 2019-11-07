#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
--------------------------------------------
# Author: hsh
# Name: SETTING.py

--------------------------------------------
"""


class __Setting:
            
    MYSQL_MAX_OVERFLOW = int()  # 64
    REDIS_HOST = str()  # 192.168.1.188
    MONGO_USERNAME = None  # None
    REDIS_PORT = int()  # 6379
    MONGO_PORT = int()  # 27017
    MYSQL_POOL_RECYCLE = int()  # 3600
    LISTEN_PORT = int()  # 7998
    MONGO_HOST = str()  # 192.168.1.188
    MYSQL_POOL_SIZE = int()  # 64
    DEBUG_METHOD = int()  # 1
    MYSQL_URL = str()  # mysql+pymysql://root:mysql@192.168.1.188/flask_frame_db
    TEST_IS_CHANGE = int()  # 0
    REDIS_PASSWORD = None  # None
    MONGO_PASSWORD = None  # None
    REDIS_DB = int()  # 0
    MAX_REDIS_CONNECTION = None  # None

SETTING = __Setting()
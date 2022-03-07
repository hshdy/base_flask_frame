#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
--------------------------------------------
# Author: hsh
# Name: SETTING.py

--------------------------------------------
"""


class __Setting:
            
    DEBUG_METHOD = int()  # 1
    LISTEN_PORT = int()  # 7998
    TEST_IS_CHANGE = int()  # 0
    MYSQL_MAX_OVERFLOW = int()  # 64
    MYSQL_POOL_RECYCLE = int()  # 3600
    MYSQL_POOL_SIZE = int()  # 64
    MYSQL_URL = str()  # mysql+pymysql://root:mysql@127.0.0.1/flask_frame_db
    MONGO_PASSWORD = None  # None
    MONGO_HOST = str()  # 127.0.0.1
    MONGO_USERNAME = None  # None
    MONGO_PORT = int()  # 27017
    REDIS_HOST = str()  # 127.0.0.1
    REDIS_PORT = int()  # 6379
    REDIS_DB = int()  # 0
    REDIS_PASSWORD = None  # None
    MAX_REDIS_CONNECTION = None  # None

SETTING = __Setting()
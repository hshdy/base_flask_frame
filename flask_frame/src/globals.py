# _*_coding:utf-8 _*_
# author: hsh
# file name: globals.py
# data: 2019/8/26 15:10
from logger.logger_service import logger


class __Global:
    __app = None
    __api = None
    __mysql_wrapper = None
    __redis_conn = None
    __etcd_wrapper = None
    __settings = None

    def set_flask_app(self, app):
        logger.debug('set flask app to global')
        self.__app = app

    def get_flask_app(self):
        logger.debug('get flask app form global')
        return self.__app

    def set_flask_api(self, api):
        self.__api = api

    def get_flask_api(self):
        return self.__api

    def set_mysql_wrapper(self, mysql_wrapper):
        self.__mysql_wrapper = mysql_wrapper

    def get_mysql_wrapper(self):
        return self.__mysql_wrapper

    def set_redis_connect(self, redis_conn):
        self.__redis_conn = redis_conn

    def get_redis_connect(self):
        return self.__redis_conn

    def set_etcd_wrapper(self, etcd_wrapper):
        self.__etcd_wrapper = etcd_wrapper

    def get_ectd_wrapper(self):
        return self.__etcd_wrapper

    def set_settings(self, settings_dict):
        self.__settings = settings_dict

    def get_settings(self):
        return self.__settings


GLOBAL = __Global()

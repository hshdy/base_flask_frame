# _*_coding:utf-8 _*_
# author: hsh
# file name: globals.py
# data: 2019/8/26 15:10
from logger.logger_service import logger


class Global:
    __app = None
    __api = None
    __mysql_wrapper = None

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


GLOBAL = Global()

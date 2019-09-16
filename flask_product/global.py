# _*_coding:utf-8 _*_
# author: hsh
# file name: global.py
# data: 2019/8/26 15:10
from logger.logger_service import logger


class Global():
    _app = None

    def set_flask_app(self, app):
        logger('set flask app to global')
        self._app = app

    def get_flask_app(self):
        logger('get flask app form global')
        return self._app

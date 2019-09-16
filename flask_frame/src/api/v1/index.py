# _*_coding:utf-8 _*_
# author: hsh
# file name: index.py
# data: 2019/8/26 15:18
from flask import current_app
from flask_restful import Resource

from logger.logger_service import logger


class Index(Resource):
    def get(self):
        current_app
        logger.info('enter into index view function')

        return 'index page'

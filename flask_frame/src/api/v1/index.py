# _*_coding:utf-8 _*_
# author: hsh
# file name: index.py
# data: 2019/8/26 15:18
from flask import jsonify
from flask import request
from flask_restful import Resource

from globals import GLOBAL
from logger.logger_service import logger
from utils.response_data import success


class Index(Resource):
    def get(self):
        logger.info("enter into index api.request method is {}".format(request.method))
        SETTING = GLOBAL.get_settings()
        logger.info("listen port is {}".format(SETTING.LISTEN_PORT))
        logger.info('enter into index view function')

        test_is_change = SETTING.TEST_IS_CHANGE
        logger.info("test_is_change={}".format(test_is_change))

        data = success()
        return jsonify(data)

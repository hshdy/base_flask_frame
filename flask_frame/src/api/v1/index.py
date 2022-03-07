# _*_coding:utf-8 _*_
# author: hsh
# file name: index.py
# data: 2019/8/26 15:18
from flask import request
from flask_restful import Resource

from globals import GLOBAL
from logger.logger_service import logger
from src.utils.parameter_decorator import Validate
from utils.api import biz_success


class Index(Resource):

    @Validate.check_params(["pid"], "args")
    def get(self):
        logger.info("enter into index api.request method is {}".format(request.method))
        SETTING = GLOBAL.get_settings()
        logger.info("listen port is {}".format(SETTING.LISTEN_PORT))
        logger.info('enter into index view function')

        test_is_change = SETTING.TEST_IS_CHANGE
        logger.info("test_is_change={}".format(test_is_change))

        data = {
            "demo": 'demo1'
        }
        return biz_success(data)

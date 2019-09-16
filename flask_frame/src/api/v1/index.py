# _*_coding:utf-8 _*_
# author: hsh
# file name: index.py
# data: 2019/8/26 15:18
from flask import current_app, request
from flask_restful import Resource

from logger.logger_service import logger


class Index(Resource):
    def get(self):
        logger.info("enter into index api.request method is {}".format(request.method))
        listen_port = current_app.config.get("CONFIG_TYPE").get("dev").LISTEN_PORT
        logger.info("listen port is {}".format(listen_port))
        logger.info('enter into index view function')

        return 'index page'

# _*_coding:utf-8 _*_
# author: hsh
# file name: initialization.py
# data: 2019/8/26 15:01
from flask import Flask
from flask_restful import Api

import settings
from api.v1 import loading_rout
from globals import GLOBAL
from logger.logger_service import logger
from  settings import SETTING


def init_base():
    logger.info('start init base server')

    # init_mysql()
    # init_mongo()

    logger.info('finish base server')


def init_web_service():
    logger.debug('start init flask web service')

    app = Flask(__name__)
    api = Api(app)

    GLOBAL.set_flask_app(app)
    GLOBAL.set_flask_api(api)
    loading_rout()
    # setting app config
    app.config.from_object(settings.BaseConfig)

    app.run("0.0.0.0", SETTING.LISTEN_PORT, debug=False)


def init():
    init_base()
    init_web_service()

# _*_coding:utf-8 _*_
# author: hsh
# file name: initialization.py
# data: 2019/8/26 15:01
from flask import Flask
from flask_restful import Api

import settings
from api.v1 import loading_rout
from api.v1.requests_hook import RequestHook
from globals import GLOBAL
from logger.logger_service import logger
from mapper.mysql_mapper import MysqlWrapper
from module.mysql_module.table_module import Base
from  settings import SETTING


def init_mysql():
    mysql_wrapper = MysqlWrapper()
    mysql_wrapper.connect_mysql()
    GLOBAL.set_mysql_wrapper(mysql_wrapper)
    mysql_wrapper.create_tables(Base)


def init_base():
    logger.info('start init base server')
    try:
        init_mysql()
    except Exception as e:
        logger.exception(e)
    # init_mongo()

    logger.info('finish base server')


def init_web_service():
    logger.debug('start init flask web service')

    app = Flask(__name__)
    api = Api(app)

    GLOBAL.set_flask_app(app)
    GLOBAL.set_flask_api(api)

    loading_rout()
    RequestHook().init_hook()
    # setting app config
    app.config.from_object(settings.BaseConfig)

    logger.info(app.url_map)
    app.run("0.0.0.0", SETTING.LISTEN_PORT, debug=False)


def init():
    init_base()
    init_web_service()

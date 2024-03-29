# _*_coding:utf-8 _*_
# author: hsh
# file name: initialization.py
# data: 2019/8/26 15:01
import os

from flask import Flask
from flask_restful import Api

from api.v1 import loading_rout
from api.v1.requests_hook import RequestHook
from globals import GLOBAL
from logger.logger_service import logger
from models.mysql_module.table_module import Base
from wrapper.etcd_wrapper import EtcdWrapper
from wrapper.load_config import LocalConfigManager
from wrapper.mysql_wrapper import MysqlWrapper
from wrapper.redis_wrapper import RedisWrapper


def init_config():
    service = LocalConfigManager()
    service.read_config()
    service.select_config()


def init_etcd():
    etcd_wrapper_server = EtcdWrapper(host=os.environ.get('ETCD_SERVICE_SERVICE_HOST', '127.0.0.1'),
                                      port=int(os.environ.get('ETCD_SERVICE_SERVICE_PORT', '2379')))
    # etcd_wrapper.connect_etcd_cluster()
    etcd_client = etcd_wrapper_server.connect_etcd_client()
    GLOBAL.set_etcd_wrapper(etcd_client)
    logger.info('initialize ETCD successfully.')


def init_mysql():
    mysql_wrapper = MysqlWrapper()
    mysql_wrapper.connect_mysql()
    GLOBAL.set_mysql_wrapper(mysql_wrapper)
    mysql_wrapper.create_tables(Base)


def init_redis():
    SETTING = GLOBAL.get_settings()

    redis_wrapper = RedisWrapper()

    if SETTING.REDIS_PASSWORD and len(SETTING.REDIS_PASSWORD) > 4:
        redis_wrapper = redis_wrapper.connect_redis(
            host=SETTING.REDIS_HOST,
            port=SETTING.REDIS_PORT,
            db=SETTING.REDIS_DB,
            password=SETTING.REDIS_PASSWORD,
            max_connections=SETTING.MAX_REDIS_CONNECTION)
    else:
        redis_wrapper = redis_wrapper.connect_redis(
            host=SETTING.REDIS_HOST,
            port=SETTING.REDIS_PORT,
            db=SETTING.REDIS_DB,
            max_connections=SETTING.MAX_REDIS_CONNECTION)
    GLOBAL.set_redis_connect(redis_wrapper)

def init_base():
    logger.info('start init base services')
    try:
        init_config()
        # init_etcd()
        init_mysql()
        init_redis()
    except Exception as e:
        logger.exception(e)
    # init_mongo()

    logger.info('finish base services')


def init_web_service():
    logger.debug('start init flask web service')

    app = Flask(__name__)
    api = Api(app)

    GLOBAL.set_flask_app(app)
    GLOBAL.set_flask_api(api)
    SETTING = GLOBAL.get_settings()

    loading_rout()
    RequestHook().init_hook()
    # setting app config
    # app.config.from_object(settings.BaseConfig)

    logger.info(app.url_map)
    app.run(host="0.0.0.0", port=SETTING.LISTEN_PORT, debug=False)


def init():
    init_base()
    init_web_service()

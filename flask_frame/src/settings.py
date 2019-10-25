#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
--------------------------------------------
# Author: hsh
# Name: setting
# DATE: 2019/9/16-14:19
--------------------------------------------
"""

from logger.logger_service import logger


class BaseConfig(object):
    """
    get flask current config use: 
        if config in BaseConfig  property
            current_app.config.get("<config_name>")
        else use 
            current_app.config.get("CONFIG_TYPE").get(<target_config_type>).get("<config_name>")
    """
    # base config
    ENV = 'development'  # let flask into development. value only “production” and “development”
    NNN = 1
    AAA = 0

    class TestConfig:
        # Test environment configuration
        AAA = 111
        LISTEN_PORT = '9999'
        CURRENT = 'is Test config'

        URL_MYSQL = 'mysql+pymysql://XXX:XXX@192.168.0.117/XXXX'
        SQL_ECHO_SHOW = False
        SYNC_INFO_INTERVAL = 86400.0

    class DevConfig:
        # Development environment configuration
        AAA = 222
        LISTEN_PORT = '8888'
        CURRENT = 'is Development config'

        URL_MYSQL = 'mysql+pymysql://root:mysql@192.168.1.188/flask_frame_db'
        SQL_ECHO_SHOW = False
        SYNC_INFO_INTERVAL = 86400.0

    class ProConfig:
        # Product environment configuration
        AAA = 333
        LISTEN_PORT = '7777'
        CURRENT = 'is Product config'

        URL_MYSQL = 'mysql://XXX:XXX@192.168.0.59/XXXX'
        SQL_ECHO_SHOW = False
        SYNC_INFO_INTERVAL = 86400.0

    # current_app.config.get("CONFIG_TYPE").get("dev")
    CONFIG_TYPE = {
        "test": TestConfig,
        "dev": DevConfig,
        "pro": ProConfig,
    }

    def get_config(self, target_config_type):
        config = self.CONFIG_TYPE.get(target_config_type)
        logger.info("current config {}".format(config.CURRENT))
        return config


SETTING = BaseConfig().get_config('dev')

if __name__ == '__main__':
    a = SETTING.AAA
    print("a={}".format(a))

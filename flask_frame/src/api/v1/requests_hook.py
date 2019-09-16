#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
--------------------------------------------
# Author: hsh
# Name: requests_hook
# DATE: 2019/9/16-16:41
--------------------------------------------
"""
from globals import GLOBAL
from logger.logger_service import logger


class RequestHook:
    def init_hook(self):
        app = GLOBAL.get_flask_app()

        @app.before_first_request
        def bf_first_request():
            logger.info("into before first request")

        @app.before_request
        def bf_request():
            logger.info("enter into before request")

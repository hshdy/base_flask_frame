#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
--------------------------------------------
# Author: hsh
# Name: handler_mysql
# DATE: 2019/10/18-17:16
--------------------------------------------
"""
from flask import request
from flask_restful import Resource

from globals import GLOBAL
from logger.logger_service import logger
from module.mysql_module.table_module import UserInfo


class HandlerMysqlDemo(Resource):
    def get(self):
        logger.info("enter into index api.request method is {}".format(request.method))
        mysql_wrapper = GLOBAL.get_mysql_wrapper()
        with mysql_wrapper.session_scope() as session:
            session.add(UserInfo('10002', 'usa', '0002'))

            # session.add_all([UserInfo('10001','us','0001')])
        return 'index page'

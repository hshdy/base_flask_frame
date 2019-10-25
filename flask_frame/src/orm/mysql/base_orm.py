#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
--------------------------------------------
# Author: hsh
# Name: base_orm
# DATE: 2019/10/25-18:40
--------------------------------------------
"""
from globals import GLOBAL
from logger.logger_service import logger


def query_data():
    pass


def create_data():
    pass


def delete_data():
    pass


def update_data():
    pass


def upset_data(table_obj, filter_data, update_data, mysql_wrapper=None):
    if not mysql_wrapper:
        mysql_wrapper = GLOBAL.get_mysql_wrapper()
    with mysql_wrapper.session_scope() as session:

        query_result = session.query(table_obj).filter(*filter_data).first()
        if query_result:
            session.query(table_obj).filter(*filter_data).update(update_data)
            logger.info("success update one.update={}".format(update_data))
        else:
            session.add(table_obj(**update_data))
            logger.info("success add one.update_data={}".format(update_data))

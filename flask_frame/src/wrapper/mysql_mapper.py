#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
--------------------------------------------
# Author: hsh
# Name: mysql_mapper
# DATE: 2019/9/16-17:16
--------------------------------------------
"""
import contextlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from __const import CONST
from globals import GLOBAL
from logger.logger_service import logger


class MysqlWrapper:
    def __init__(self):
        self.session_maker = None
        self.engine = None
        self.session = None
        self.scope_session = None

    def create_tables(self, Base):
        try:
            logger.info('creating sql tables.')
            Base.metadata.create_all(self.engine)
        except Exception as e:
            logger.error('create tables failed {}'.format(str(e)))

    def connect_mysql(self):
        try:
            SETTING = GLOBAL.get_settings()
            self.engine = create_engine('{}?charset=utf8'.format(SETTING.MYSQL_URL),
                                        encoding=CONST.CODE_UTF8, echo=CONST.SQL_ECHO_SHOW)
            session_maker = sessionmaker(bind=self.engine)
            self.scope_session = scoped_session(session_maker)
        except Exception as e:
            logger.exception(str(e))
            raise e

    @contextlib.contextmanager
    def session_scope(self):
        try:
            self.session = self.scope_session()
            yield self.session
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.scope_session.remove()

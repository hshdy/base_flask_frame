#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
--------------------------------------------
# Author: hsh
# Name: table_module
# DATE: 2019/10/25-18:34
--------------------------------------------
"""
from datetime import datetime

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserInfo(Base):
    __tablename__ = 'user_info'
    id = Column(Integer, primary_key=True, autoincrement=True)

    sid = Column(String(64), index=True, nullable=False, unique=True)
    seller_id = Column(String(64), index=True, nullable=False, unique=True)
    create_date = Column(DateTime(), default=datetime.now)
    update_date = Column(DateTime(), default=datetime.now)

    def __init__(self, sid, site, seller_id):
        self.sid = sid
        self.site = site
        self.seller_id = seller_id


# # todo： 当模型类拆分到 其他文件，无法创建成功。
class ProductInfo(Base):
    __tablename__ = 'product_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user_info.id'), default=None)
    doc = Column(String(64), index=True, nullable=False, unique=True)


is_active = Column(Integer, default=True)
create_date = Column(DateTime(), default=datetime.now)
update_date = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

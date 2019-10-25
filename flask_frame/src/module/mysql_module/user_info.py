#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
--------------------------------------------
# Author: hsh
# Name: user_info
# DATE: 2019/9/24-17:46
--------------------------------------------
"""
# from datetime import datetime
#
# from sqlalchemy import Column, String, Integer
# from sqlalchemy import DateTime
#
# from module.mysql_module.table_module import Base
#
#
# class UserInfo(Base):
#     __tablename__ = 'user_info'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#
#     sid = Column(String(64), index=True, nullable=False, unique=True)
#     seller_id = Column(String(64), index=True, nullable=False, unique=True)
#     create_date = Column(DateTime(), default=datetime.now)
#     update_date = Column(DateTime(), default=datetime.now)
#
#     def __init__(self, sid, site, seller_id):
#         self.sid = sid
#         self.site = site
#         self.seller_id = seller_id
#
#         # # todo： 当模型类拆分到 其他文件，无法创建成功。
#         # class ProductInfo(Base):
#         #     __tablename__ = 'product_info'
#         #     id = Column(Integer, primary_key=True, autoincrement=True)
#         #     user_id = Column(Integer, ForeignKey('user_info.id'), default=None)
#         #     doc = Column(String(64), index=True, nullable=False, unique=True)
#
#         # is_active = Column(Integer, default=True)
#         # create_date = Column(DateTime(), default=datetime.now)
#         # update_date = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

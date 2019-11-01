# #! /usr/bin/env python
# # -*- coding:utf-8 -*-
# """
# --------------------------------------------
# # Author: hsh
# # Name: product_info
# # DATE: 2019/9/24-18:45
# --------------------------------------------
# """
# from datetime import datetime
#
# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy import DateTime
#
# from wrapper.mysql_mapper import Base
#
#
# class ProductInfo(Base):
#     __tablename__ = 'product_info'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey('user_info.id'), default=None)
#     doc = Column(String(64), index=True, nullable=False, unique=True)
#
#     is_active = Column(Integer, default=True)
#     create_date = Column(DateTime(), default=datetime.now)
#     update_date = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
#
#     def __init__(self, sid, email, fk_ses_info_id):
#         self.sid = sid
#         self.email = email
#         self.fk_ses_info_id = fk_ses_info_id

# _*_coding:utf-8 _*_
# author: hsh
# file name: const.py
# data: 2019/8/26 14:51
from logger.logger_service import logger


class Const(object):
    def __new__(cls, *args, **kwargs):
        logger.error("forbid create new const object")
        raise Exception('forbid create new const object')

    SYSTEM_NAME = 'system_name'
    SUB_SYSTEM = 'sub_system'


CONST = Const()

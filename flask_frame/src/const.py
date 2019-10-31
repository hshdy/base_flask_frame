# _*_coding:utf-8 _*_
# author: hsh
# file name: const.py
# data: 2019/8/26 14:51
from logger.logger_service import logger


class Const(object):
    def __setattr__(self, *_):
        raise ValueError('Trying to change a constant value')

    SYSTEM_NAME = 'system_name'
    SUB_SYSTEM = 'sub_system'
    DEBUG_METHOD = "debug_method"
    ETCD_RECONNECT_WAIT_TIME = 3

    RESULT = 'result'
    STATUS = 'status'
    SUCCESS = 'success'
    FAILURE = 'failure'
    ERROR_CODE = 'error_code'
    REASON = 'reason'

    CODE_UTF8 = 'utf-8'
    SQL_ECHO_SHOW = False
CONST = Const()

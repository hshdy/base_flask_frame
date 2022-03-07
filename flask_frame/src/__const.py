# _*_coding:utf-8 _*_
# author: hsh
# file name: const.py
# data: 2019/8/26 14:51


class __Const(object):
    def __setattr__(self, *_):
        raise ValueError('Trying to change a constant value')

    SYSTEM_NAME = 'system_name'
    SUB_SYSTEM = 'sub_system'
    DEBUG_METHOD = "debug_method"
    ETCD_RECONNECT_WAIT_TIME = 3

    # 业务状态码
    BIZ_CODE_OK = 0
    BIZ_CODE_FAIL = 1

    RESULT = 'result'
    STATUS = 'status'
    SUCCESS = 'success'
    FAILURE = 'failure'
    ERROR_CODE = 'error_code'
    REASON = 'reason'

    CODE_UTF8 = 'utf-8'
    SQL_ECHO_SHOW = False

    # Common Const
    DEFAULT_PAGE = 1
    DEFAULT_PER_PAGE = 10


CONST = __Const()

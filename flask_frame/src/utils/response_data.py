#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
--------------------------------------------
# Author: hsh
# Name: response_data
# DATE: 19-10-31-下午2:45
--------------------------------------------
"""
from __const import CONST
from logger.logger_service import logger


def get_dict(*args, **kwargs):
    if not args and not kwargs:
        return {}
    if len(args) == 1 and not kwargs and isinstance(args[0], dict):
        return args[0]
    if kwargs and not args:
        return kwargs

    raise ValueError('neither a dict nor a **kwargs')


def success(*args, **kwargs) -> dict:
    result = {
        CONST.STATUS: CONST.SUCCESS
    }
    result.update(get_dict(*args, **kwargs))
    return result


def failure(error_code=-1, reason=None, *args, **kwargs) -> dict:
    result = {
        CONST.STATUS: CONST.FAILURE,
        CONST.ERROR_CODE: error_code,
        CONST.REASON: reason
    }
    result.update(get_dict(*args, **kwargs))
    logger.error(result)
    return result

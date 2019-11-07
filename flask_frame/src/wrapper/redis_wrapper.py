#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
--------------------------------------------
# Author: hsh
# Name: redis_wrapper
# DATE: 19-11-7-下午3:34
--------------------------------------------
"""
import redis

from logger.logger_service import logger


class RedisWrapper:
    redis_conn = None

    def connect_redis(self, **redis_kwargs):
        try:
            self.redis_conn = redis.Redis(**redis_kwargs)
            logger.debug("Connected to redis: {}:{} db is {}".format(
                redis_kwargs.get("host"),
                redis_kwargs.get("port"),
                redis_kwargs.get("db"),
            ))
            return self.redis_conn
        except Exception as e:
            logger.exception(str(e))
            raise e

    def get_redis_conn(self):
        return self.redis_conn

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: __hsh__
import logging
import os
import time
from logging.handlers import RotatingFileHandler


class Logger(object):
    # 日志级别关系映射
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(self, level):
        """
        初始化
        """
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        fmt = '[%(asctime)s]'
        fmt += '-[%(levelname)s]'
        fmt += '-[%(process)d]'
        fmt += '-[%(threadName)s]'
        fmt += '-[%(thread)d]'
        fmt += '-[%(filename)s:%(lineno)s]'
        fmt += ' # %(message)s'

        today = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        if not self.logger.handlers or self.logger.handlers[0].baseFilename.find(today) < 0:
            self.logger.handlers = []

            path = os.path.abspath(
                os.path.join(os.path.dirname((os.path.abspath(__file__))), "logfile"))
            if not os.path.exists(path):
                os.makedirs(path)

            log_filename = os.path.join(path, '{time}.log'.format(time=today))

            file_handler = RotatingFileHandler(log_filename, maxBytes=10240, encoding='utf-8')
            file_handler.setFormatter(logging.Formatter(fmt))
            self.logger.addHandler(file_handler)

            # 创建一个handler用于输出控制台
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter(fmt))

            console_handler.setLevel(logging.DEBUG)
            self.logger.addHandler(console_handler)
            # file_handler.close()

    def getLogger(self):
        """
        获取初始化后的Logger
        :return:
        """
        return self.logger


logger = Logger(level='debug').getLogger()

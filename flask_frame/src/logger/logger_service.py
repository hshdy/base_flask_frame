#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: __hsh__
import logging
import os
from logging import handlers


class Logger(object):
    # 日志级别关系映射
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(self, filename, level='info', when='D', backCount=3,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        os.makedirs('./log', exist_ok=True)

        self.logger = logging.getLogger(filename)

        fmt = '[%(asctime)s]'
        fmt += '-[%(levelname)s]'
        fmt += '-[%(process)d]'
        fmt += '-[%(threadName)s]'
        fmt += '-[%(thread)d]'
        fmt += '-[%(filename)s:%(lineno)s]'
        fmt += ' # %(message)s'
        formatter = logging.Formatter(fmt)

        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setFormatter(formatter)  # 设置屏幕上显示的格式
        handler = logging.handlers.RotatingFileHandler(
            filename, maxBytes=1 * 1024 * 1024, backupCount=1)

        handler.setFormatter(formatter)
        # 设置后缀名称，跟strftime的格式一样

        # th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,
        #                                        encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
        # # 实例化TimedRotatingFileHandler
        # # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # # S 秒
        # # M 分
        # # H 小时、
        # # D 天、
        # # W 每星期（interval==0时代表星期一）
        # # midnight 每天凌晨
        # th.setFormatter(format_str)  # 设置文件里写入的格式
        self.logger.addHandler(sh)  # 把对象加到logger里
        self.logger.addHandler(handler)

    def getLogger(self):
        """
        获取初始化后的Logger
        :return:
        """
        return self.logger

logger = Logger('./logger/log.log', level='debug').getLogger()

#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
--------------------------------------------
# Author: hsh
# Name: etcd_wrapper
# DATE: 19-10-29-下午3:03
--------------------------------------------
"""
import time

import etcd

from const import CONST
from logger.logger_service import logger


class EtcdWrapper:
    def __init__(self, host, port):
        self.etcd_client = None
        self.etcd_host = host
        self.etcd_port = port

    def connect_etcd_cluster(self, connect_leader=False):
        while True:
            try:
                self.etcd_client = etcd.Client(
                    host=self.etcd_host, port=self.etcd_port, allow_reconnect=True, read_timeout=30)

                logger.info(
                    'Connected to ETCD cluster: {}:{}'.format(self.etcd_host, self.etcd_port))

                if connect_leader:
                    leader = self.etcd_client.leader['clientURLs']
                    logger.debug('leader: {}'.format(leader))
                    if leader is None:
                        return

                    leader = leader[0].split(':')[1][2:]
                    logger.info('reconnect to leader: {}'.format(leader))
                    self.etcd_client = etcd.Client(
                        host=leader, port=self.etcd_port, allow_reconnect=True, read_timeout=10)

            except etcd.EtcdException:
                time.sleep(CONST.ETCD_RECONNECT_WAIT_TIME)
                logger.info('reconnect...')
                continue

            break

    def connect_etcd_client(self):
        while True:
            try:
                self.etcd_client = etcd.Client(
                    host=self.etcd_host, port=self.etcd_port, allow_reconnect=True, read_timeout=10)

                logger.info(
                    'Connected to ETCD cluster: {}:{}'.format(self.etcd_host, self.etcd_port))
                return self.etcd_client
            except etcd.EtcdException:
                time.sleep(CONST.ETCD_RECONNECT_WAIT_TIME)
                logger.info('reconnect...')
                continue

    def read_etcd_config_data(self):

        config_dict = dict()
        try:
            config_object = self.etcd_client.read('/{}'.format(CONST.SYSTEM_NAME), recursive=True)
            for child in config_object.children:
                key_path = child.key
                key = key_path.split('/')[-1]
                value = child.value

                config_dict[key.upper()] = value

            return config_dict
        except Exception as e:
            logger.error('read_etcd_config_data error')
            logger.error(e)

        return config_dict

    def create(self, key, value):
        try:
            self.etcd_client.read(key)
        except etcd.EtcdKeyNotFound:
            self.etcd_client.write(key, value)

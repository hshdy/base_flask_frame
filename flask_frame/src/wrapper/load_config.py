#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
--------------------------------------------
# Author: hsh
# Name: load_local_config
# DATE: 19-10-29-下午3:41
--------------------------------------------
"""
import os
import threading
import time

import yaml

from const import CONST
from globals import GLOBAL
from logger.logger_service import logger
from wrapper.etcd_wrapper import EtcdWrapper
from wrapper.settings_file_wapper import SettingsFileWrapper


class LocalConfigManager():
    __config_dict = dict()
    __yaml_dict = dict()
    __yaml_chain_info_list = list()

    def __init__(self):
        self.local_config_path = os.path.join(os.getcwd(), "config.yaml")

    @staticmethod
    def __get_config_dict(yaml_dict):
        system_name_dict = yaml_dict.get(CONST.SYSTEM_NAME)
        config_dict = dict()
        # todo： 优化处理，递归解析，当前没递归处理
        for info in system_name_dict:
            for key in system_name_dict[info]:
                if isinstance(system_name_dict[info][key], dict):
                    for son_key in system_name_dict[info][key]:
                        config_dict[son_key.upper()] = system_name_dict[info][key][son_key]
                else:
                    config_dict[key.upper()] = system_name_dict[info][key]

        return config_dict

    @staticmethod
    def __get_yaml_chain_info_list(yaml_dict: dict):
        yaml_chain_list = []
        for first_key in yaml_dict:
            for sec_key in yaml_dict[first_key]:
                for three_key in yaml_dict[first_key][sec_key]:
                    if isinstance(yaml_dict[first_key][sec_key][three_key], dict):
                        for four_key in yaml_dict[first_key][sec_key][three_key]:
                            yaml_chain_list.append({"/{}/{}/{}/{}".format(first_key, sec_key, three_key, four_key):
                                                        yaml_dict[first_key][sec_key][three_key][four_key]})
                    else:
                        yaml_chain_list.append({"/{}/{}/{}".format(first_key, sec_key, three_key):
                                                    yaml_dict[first_key][sec_key][three_key]})

        return yaml_chain_list

    def read_config(self):
        try:
            with open(self.local_config_path, 'r', encoding='utf-8') as f:
                cfg = f.read()
                self.__yaml_dict = yaml.load(cfg)
                self.__config_dict = self.__get_config_dict(self.__yaml_dict)
                self.__yaml_chain_info_list = self.__get_yaml_chain_info_list(self.__yaml_dict)

        except Exception as e:
            logger.error("load local config failed")
            logger.error(e)

    def select_config(self):
        settings_server = SettingsFileWrapper()
        if not self.__config_dict:
            raise Exception("load config failed! not config data")

        config_method = os.environ.get('debug_method')
        if config_method == 1:
            logger.info('use LOCAL config')
            settings_server.generate_settings_file(self.__config_dict)
            GLOBAL.set_settings(type("SETTING", (), self.__config_dict))
        else:
            config_method = self.__yaml_dict.get(CONST.SYSTEM_NAME).get(CONST.SUB_SYSTEM).get(CONST.DEBUG_METHOD)
            if config_method == 1:
                logger.info('use LOCAL config')
                settings_server.generate_settings_file(self.__config_dict)
                GLOBAL.set_settings(type("SETTING", (), self.__config_dict))
            else:
                logger.info('load ETCD config')
                etcd_wrapper_server = EtcdWrapper(host=os.environ.get('ETCD_SERVICE_SERVICE_HOST', '127.0.0.1'),
                                                  port=int(os.environ.get('ETCD_SERVICE_SERVICE_PORT', '2379')))
                # etcd_wrapper.connect_etcd_cluster()
                etcd_wrapper_server.connect_etcd_client()

                self.reset_etcd_config(etcd_wrapper_server)

                config_dict = etcd_wrapper_server.read_etcd_config_data()
                settings_server.generate_settings_file(config_dict)
                GLOBAL.set_settings(type("SETTING", (), config_dict))

                t = threading.Thread(target=self.load_config_by_etcd, args=(settings_server,), name="read_etcd_loop")
                t.start()

    def load_config_by_etcd(self, settings_server):
        while True:
            try:
                time.sleep(180)
                logger.debug('load ETCD config')
                etcd_wrapper_server = EtcdWrapper(host=os.environ.get('ETCD_SERVICE_SERVICE_HOST', '127.0.0.1'),
                                                  port=int(os.environ.get('ETCD_SERVICE_SERVICE_PORT', '2379')))
                # etcd_wrapper.connect_etcd_cluster()
                etcd_wrapper_server.connect_etcd_client()

                self.reset_etcd_config(etcd_wrapper_server)

                config_dict = etcd_wrapper_server.read_etcd_config_data()
                settings_server.generate_settings_file(config_dict)
                GLOBAL.set_settings(type("SETTING", (), config_dict))
                logger.debug('reload ETCD config success! ')

            except Exception as e:
                logger.error(e)
                time.sleep(5)

    def reset_etcd_config(self, etcd_wrapper_server):
        for info in self.__yaml_chain_info_list:
            for key in info:
                value = info[key]
                etcd_wrapper_server.create(key, value)

    def get_config_data(self):
        while True:
            if self.__config_dict:
                return self.__config_dict
            else:
                self.read_config()

            time.sleep(1)

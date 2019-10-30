#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
--------------------------------------------
# Author: hsh
# Name: settings_file_mapper
# DATE: 19-10-29-下午5:26
--------------------------------------------
"""


class SettingsFileWrapper:
    def __init__(self):
        pass

    @staticmethod
    def __generate_file_head():
        with open("./setting.py", 'w+') as f:
            f.write('''#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
--------------------------------------------
# Author: hsh
# Name: SETTING.py

--------------------------------------------
"""


class __Setting:
            ''')

    @staticmethod
    def __generate_body(config_dict):
        for key in config_dict.keys():
            value = config_dict[key]

            if isinstance(value, str):
                value_tpye = "str()"

            elif isinstance(value, int):
                value_tpye = "int()"
            else:
                value_tpye = "None"

            with open("./setting.py", 'a') as f:
                f.write("""\n    {} = {}  # {}""".format(key.upper(), value_tpye, config_dict[key]))

    @staticmethod
    def __generate_button():
        with open("./setting.py", 'a') as f:
            f.write("""\n\nSETTING = __Setting()""")

    def generate_settings_file(self, config_dict):
        self.__generate_file_head()
        self.__generate_body(config_dict)
        self.__generate_button()
        __import__("setting")

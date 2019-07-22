#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 15:52
# @Author  : fans
# @File    : yaml_util.py
# @Software: PyCharm Community Edition
import yaml
import os
class yaml_util:
    @staticmethod
    def read_all(file_name):
        with open(file_name, 'r', encoding='UTF-8') as f:
            file_content = f.read()
            res = yaml.safe_load(file_content)
            return res

    @staticmethod
    def read(file_name,section,option=None):
        with open(file_name, 'r', encoding='UTF-8') as f:
            file_content = f.read()
            res = yaml.safe_load(file_content)
            if option :
                return  res[section][option]
            else:
                return res[section]

    @staticmethod
    def write(file_name,data,mode='w'):
        with open(file_name, mode, encoding='UTF-8') as f:
            yaml.dump(data, f)


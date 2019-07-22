# -*- coding:utf-8 _*-
import configparser
import os
from common import constants

class ConfigLoader:

    def __init__(self):
        # 创建实例
        self.conf = configparser.ConfigParser()
        # 加载配置文件
        file_name = os.path.join(constants.configs_dir, 'global.conf')
        self.conf.read(filenames=file_name,encoding='utf-8')
        self.db_type = self.get('db', 'type')
        if self.getboolean('switch','on'):
            online = os.path.join(constants.configs_dir, 'online.conf')
            self.conf.read(filenames=online,encoding='utf-8')
        else:
            test = os.path.join(constants.configs_dir, 'test.conf')
            self.conf.read(filenames=test,encoding='utf-8')


    def get(self, section, option): # 返回str类型的值
        # 根据section，option 来取到配置的值
        return self.conf.get(section, option)

    def getboolean(self, section, option): # 返回str类型的值
        # 根据section，option 来取到配置的值
        return self.conf.getboolean(section, option)

    def getint(self, section, option): # 返回str类型的值
        # 根据section，option 来取到配置的值
        return self.conf.getint(section, option)

    def getfloat(self, section, option): # 返回float类型的值
        # 根据section，option 来取到配置的值
        return self.conf.getfloat(section, option)

    def hasoption(self, section ,option):
        return self.conf.has_option(section ,option)

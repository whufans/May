# -*- coding:utf-8 _*-
from  configparser import ConfigParser
import os
from common import constants

class ConfigLoader(ConfigParser):

    def __init__(self):
        super().__init__()
        # 加载配置文件
        file_name = os.path.join(constants.configs_dir, 'global.conf')
        self.read(file_name,encoding='utf-8')
        self.db_type = self.get('db', 'type')
        if self.getboolean('switch','on'):
            online = os.path.join(constants.configs_dir, 'online.conf')
            self.read(filenames=online,encoding='utf-8')
            self.file_name = online
        else:
            test = os.path.join(constants.configs_dir, 'test.conf')
            self.read(filenames=test,encoding='utf-8')
            self.file_name = test

    def get_section(self,section):
        return   dict(self.items(section))


if __name__ == '__main__':
    conf =ConfigLoader()
    print(conf.get_section('basic'))
    print(conf.has_option('Oracle','pwd'))


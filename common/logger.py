#!/usr/bin/env python
# -*- coding: utf-8 -*-
import  logging,time,os,HTMLTestRunnerNew
from common import constants
from common.config import  ConfigLoader
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler
logger = logging.getLogger('api_test')
level = ConfigLoader().get('log','level')
logger.setLevel(level)
def  get_current_day():
    return time.strftime('%Y%m%d', time.localtime(time.time()))

def get_logs_dir():
    logs_dir=os.path.join(constants.logs_dir,get_current_day())
    if not os.path.isdir(logs_dir):
        os.makedirs(logs_dir)
    return logs_dir

def set_handler(levels):
    if levels == 'error': # 判断如果是error就添加error的handler
        logger.addHandler(MyLog.error_handle)
    else: # 其他添加到infohandler
        logger.addHandler(MyLog.handler)
    logger.addHandler(MyLog.ch)  # 全部输出到console
    logger.addHandler(MyLog.report_handler)  # 全部输出到report


def remove_handler(levels):
    if levels == 'error':
        logger.removeHandler(MyLog.error_handle)
    else:
        logger.removeHandler(MyLog.handler)
    logger.removeHandler(MyLog.ch)
    logger.addHandler(MyLog.report_handler)

class MyLog:
    log_dir = get_logs_dir()
    # 指定输出文件
    log_file = os.path.join(log_dir, 'info.log')
    error_file = os.path.join(log_dir, 'error.log')
    # 设置日志输出格式asctime levelname  message pathname filename
    formatter=logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s")
    # 指定输出渠道
    # 控制台输出
    ch = logging.StreamHandler()
    ch.setLevel('DEBUG')
    ch.setFormatter(formatter)
    # INFO文件输出 自己扩展日志回滚
    handler = RotatingFileHandler(filename=log_file, mode='a', maxBytes=100000000, backupCount=20, encoding='UTF-8')
    handler.setLevel('INFO')
    handler.setFormatter(formatter)
    # 错误文件输出 自己扩展日志回滚
    error_handle = logging.FileHandler(filename=error_file, encoding='utf-8')
    error_handle.setLevel('ERROR')
    error_handle.setFormatter(formatter)
    # 报表日志输出
    report_handler = logging.StreamHandler(HTMLTestRunnerNew.stdout_redirector)
    report_handler.setLevel('INFO')
    report_handler.setFormatter(formatter)
    @staticmethod
    def debug(msg):
        set_handler('debug')
        logger.debug(msg)
        remove_handler('debug')
    @staticmethod
    def info(msg):
        set_handler('info')
        logger.info(msg)
        remove_handler('info')
    @staticmethod
    def error(msg):
        set_handler('error')
        logger.error(msg, exc_info=True)  # 同时输出异常信息
        remove_handler('error')




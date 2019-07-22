# -*- coding:utf-8 _*-
import pymysql
from common.config import ConfigLoader

class MysqlUtil:

    def __init__(self):
        config = ConfigLoader()
        host = config.get('mysql', 'host')
        port = config.getint('mysql', 'port')  # port 是一个数值
        user = config.get('mysql', 'usr')
        password = config.get('mysql', 'pwd')
        # 异常处理
        self.mysql = pymysql.connect(host=host, user=user, password=password,
                                     port=port, cursorclass=pymysql.cursors.DictCursor)

    def fetch_one(self, sql):  # 查询一条数据并返回
        cursor = self.mysql.cursor()
        cursor.execute(sql)  # 根据sql 进行查询
        return cursor.fetchone()  #

    def fetch_all(self, sql):  # 查询多条数据并返回
        cursor = self.mysql.cursor()

        cursor.execute(sql)  # 根据sql 进行查询
        return cursor.fetchall()  # ((),())

    def close(self):
        self.mysql.close()

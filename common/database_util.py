#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 10:26
# @Author  : fans
# @File    : database_util.py
# @Software: PyCharm Community Edition
# -*- coding:utf-8 _*-
import pymysql
import cx_Oracle
import pymssql
import pymongo
from common.config import ConfigLoader
class Db_Util:

    def __init__(self):
        config = ConfigLoader()
        db_type = config.db_type
        host = config.get(db_type, 'host')
        port = config.getint(db_type, 'port')  # port 是一个数值
        user = config.get(db_type, 'usr')
        password = config.get(db_type, 'pwd')
        if  config.hasoption(db_type, 'database'):
            database = config.get(db_type, 'database')
        # 异常处理
        if db_type.lower()=='mysql':
            self.db = pymysql.connect(host=host, user=user, password=password,
                                     port=port, database = database ,cursorclass=pymysql.cursors.DictCursor)
        elif db_type.lower()=='oracle':
            SID = config.get(db_type, 'SID')
            self.db = cx_Oracle.connect("{}/{}@{}:{}/{}".format(user,password,host,port,SID))
        elif db_type.lower()=='sqlserver':
            self.db = pymssql.connect(host = host,user = user,password = password, database = database )

    def execute(self,sql):
        cursor = self.db.cursor()
        cursor.execute(sql)
        self.db.commit()

    def fetch_one(self, sql):  # 查询一条数据并返回
        cursor = self.db.cursor()
        cursor.execute(sql)  # 根据sql 进行查询
        return cursor.fetchone()  #

    def fetch_all(self, sql):  # 查询多条数据并返回
        cursor = self.db.cursor()

        cursor.execute(sql)  # 根据sql 进行查询
        return cursor.fetchall()  # ((),())

    def close(self):
        self.db.close()

if __name__ == '__main__':
    db = Db_Util()
    res = db.execute("insert  into kucun values ('E',4000)")
    db.close()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 14:45
# @Author  : fans
# @File    : mongodb_util.py
# @Software: PyCharm Community Edition
import pymongo
from pymongo import MongoClient
from common.config import ConfigLoader

class MongoDb_Util(object):

    def __init__(self):
        config = ConfigLoader()
        db_type = config.db_type
        host = config.get(db_type, 'host')
        port = config.getint(db_type, 'port')
        database = config.get(db_type, 'database')
        self.client = MongoClient(host, port)
        self.db = self.client[database]
        # self.content = self.db.contents

    def set_collection(self,collection):
        self.collection = self.db[collection]

    def insert_one(self, data):
        """直接使用insert() 可以插入一条和插入多条 不推荐 明确区分比较好"""
        res = self.collection.insert_one(data)
        return res.inserted_id

    def insert_many(self, data_list):
        res = self.collection.insert_many(data_list)
        return res.inserted_ids

    def find_one(self, data, data_field={}):
        if len(data_field):
            res = self.collection.find_one(data, data_field)
        else:
            res = self.collection.find_one(data)
        return res

    def find_many(self, data, data_field={}):
        """ data_field 是指输出 操作者需要的字段"""
        if len(data_field):
            res = self.collection.find(data, data_field)
        else:
            res = self.collection.find(data)
        return res

    def update_one(self, data_condition, data_set):
        """修改一条数据"""
        res = self.collection.update_one(data_condition, data_set)
        return res

    def update_many(self, data_condition, data_set):
        """ 修改多条数据 """
        res = self.collection.update_many(data_condition, data_set)
        return res

    def replace_one(self, data_condition, data_set):
        """ 完全替换掉 这一条数据， 只是 _id 不变"""
        res = self.collection.replace_one(data_condition, data_set)
        return res

    def delete_many(self, data):
        res = self.collection.delete_many(data)
        return res

    def delete_one(self, data):
        res = self.collection.delete_one(data)
        return res


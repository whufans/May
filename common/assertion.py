#!/usr/bin/env python
import json
import operator

class  My_assertion:
    @staticmethod
    def my_assert(expect_res,actual_res):
        try:
            if str(actual_res).find(str(expect_res))>=0:
                return  True
            if expect_res==actual_res:
                return  True
            return  False
        except Exception as e:
            raise   e

    @staticmethod
    def is_contain(expect_res, actual_res):  # 判断str_one是否包含于str_two
        flag = None
        try:
            if str(actual_res).find(str(expect_res))>=0:
                flag = True
        except Exception as e:
            raise e
        return flag

    # 判断两个字典是否相等


    @staticmethod
    def is_equal_list(list_one, list_two):
        return operator.eq(list_one, list_two)



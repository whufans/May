#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 8:50
# @Author  : fans
# @File    : testjson.py
# @Software: PyCharm Community Edition
import os
# def file_name(file_dir):
#     for root, dirs, files in os.walk(file_dir):
        #print(root)  # 当前目录路径
        #print(dirs)  # 当前路径下所有子目录
        #print(files)  # 当前路径下所有非目录子文件
def transfer(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            path = "{}\\{}".format(dir, file)
            with open(path,"r",encoding="utf-8") as file1:
                result=file1.read()
            result=result.replace("\n","")
            str=""
            for i in result:
                if ord(i)!=160:
                    str+=i
            with open(path, "w", encoding="utf-8") as file2:
                file2.write(str)
if __name__ == '__main__':
    transfer("E:\\testcase")




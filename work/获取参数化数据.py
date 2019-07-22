#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 8:50
# @Author  : fans
# @File    : testjson.py
# @Software: PyCharm Community Edition
import os,json,jsonpath,re
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

def  get_Res(dir,type):
    for root, dirs, files in os.walk(dir):
        for file in files:
            path = "{}\\{}".format(dir, file)
            with open(path, 'r+', encoding='UTF-8') as file1:
                result = file1.read()
                jsonRes = json.loads(result)
                if type=='elle':
                    elleResult = jsonpath.jsonpath(jsonRes, expr='$..elleResult')
                    for i in elleResult:
                        print(i)
                elif type=='ocr':
                    ocrResult = jsonpath.jsonpath(jsonRes, expr='$..ocrResult')
                    for i in ocrResult:
                        print(i)

def  get_Res_re(dir,pattern):
    for root, dirs, files in os.walk(dir):
        for file in files:
            path = "{}\\{}".format(dir, file)
            with open(path, 'r+', encoding='UTF-8') as file1:
                result = file1.read()
                searchObj = pattern.findall(result)
                print(len(searchObj))
                for i in searchObj:
                    print(i)

if __name__ == '__main__':
    # get_Res('E:\\xntestdatas',type='ocr')
    # get_Res('E:\\xntestdatas',type='elle')
    pattern1 = re.compile(r'"elleResult":"(.*?)"')
    pattern2 = re.compile(r'"ocrResult":"(.*?)"')
    path = 'E:\\test\\catalina.txt'
    with open(path, 'r+', encoding='UTF-8') as file1:
        result = file1.read()
        searchObj = pattern1.findall(result)
        print(len(searchObj))
        for i in searchObj:
            print(i)









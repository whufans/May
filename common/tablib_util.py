#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/15 16:35
# @Author  : fans
# @File    : tablib_util.py
# @Software: PyCharm Community Edition
import tablib
headers = ['url','method','expected']
datas = [['heea','get','suc'],
         ['heeaas','post','fail']]
data = tablib.Dataset(*datas,headers=headers,title='tablib测试')
# print(data)
# with open('demo.xls','wb') as  f:
#     f.write(data.xls)
#
# with open('demo.xlsx','wb') as  f:
#     f.write(data.xlsx)

# data2 = tablib.Dataset(*datas,headers=headers,title='tablib测试2')
# book = tablib.Databook([data,data2])
# with open('demo.xls','wb') as  f:
#     f.write(book.xls)
with open('demo.xlsx','rb') as f:
    data = tablib.import_set(f.read(),'xlsx')
    print(data[0][0])
    print(data.title)
    print(data.headers)
    print(data.get_col(0))
    data.append(1,[['asd','sff','ff']])
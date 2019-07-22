#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 8:45
# @Author  : fans
# @File    : BVTapi.py
# @Software: PyCharm Community Edition
with open('a.txt', "r", encoding="utf-8") as file1:
	result = file1.read()
result = result.replace("\n", "")
result = result.replace("\t", "")
result = result.replace(" ", "")
str = ""
for i in result:
	if ord(i) != 160:
		str += i
str=str.replace(' ','')
str = str.replace('\\n','')
print(str)

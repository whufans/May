#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/24 13:42
# @Author  : fans
# @File    : test.py
# @Software: PyCharm Community Edition
'''
count = 3
account = {'user1':'123456','user2':'123456','user3':'123456','root':'123456'}
account_try = {}
while count>0:
    username = input('请输入账号:').strip()
    password = input('请输入密码:').strip()
    with open('a.txt', 'r+', encoding='UTF-8') as f:
        black_user=[i.replace('\n','') for i in f.readlines()]
        print(black_user,type(black_user))
        if  username in black_user:
            print('账号{}被锁定'.format(username))
        else:
            if  username in account and password ==account[username]:
                print('登陆成功!')  # 登陆成功需跳出循环
                break
            else:
                count -= 1
                print('登陆失败,还剩{}次机会'.format(count))
                account_try[username]=count
                if count ==0  and username in account:
                    f.writelines(username)

class Animal:
    def __init__(self,name,gender):
        self._name=name
        self.__gender=gender
    @property
    def name(self):
        return  self._name
    @name.setter
    def name(self,name):
        self._name=name
    @property
    def gender(self):
        return  self.__gender

d={'k1':'v1','k2':[1,2,3],('k','3'):{1,2,3}}
# 请用程序实现：
#   1）输出上述字典中value为列表的key
#   2）如果字典中的key是一个元祖,请输出对应的value值。
#   3）d[('k','3')]对应的value是一个什么数据类型
list1=[i for i in d if  type(d[i])==list]
list2=[d[i] for i in d if  isinstance(i,tuple)]
print(list1,list2 )
# 5. 判断质数
# 6. 分解质因数
# 8. 求a和b的最大公约数
# 9. 生成6位数的数字随机验证码
# dic={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
# print(sorted(dic,key=lambda  dic:dic.keys))
import re,json
# s = ["123@134.com","qfw@163.com","ewg@1633.com"]
# for i in s:
#     res = re.findall('.*@163.com$',i)
#     if res:
#         print(res)
# s="info:xiaoZhang 33 shandong"
# s = re.split(r':| ',s)
# print(s)
# import openpyxl
# import re
# with open('a.txt',mode='r+',encoding='UTF-8') as f:
#     info = f.read()
#     res1 = re.findall(r'"elleResult":".*{fdfs_url}/G1/M00(.*?)"',info)
#     res2 = re.findall(r'"ocrResult":".*{fdfs_url}/G1/M00(.*?)"',info)
#     l1 = res1 + res2
#     for i in l1:
#         print(i)
'''
# from enum import Enum
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)
# print(Month.Jan.value)
"""
import requests
import os
def uploadImage(upload_url,filepath):
    filename = os.path.basename(filepath)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    files = {"file": ("1.jpg",open(filepath, 'rb'),"image/jpeg") }
    data = {"dossierNo": "awecf12",
        "caseNo": "awefaf12",
        "sort": 1,
        "isAppend": 1,
        "isFirst": 1 }
    response = requests.post(upload_url, headers=headers, data=data, files=files)
    return response.json()
    """
def func(a):
    flag =1 if a>0 else -1
    a = str(abs(a))[::-1]
    a=int(a)
    if a<pow(2,31)-1:
        return  flag*a
    return  0

print(func(-22757334))
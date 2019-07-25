#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 15:46
# @Author  : fans
# @File    : debugtalk.py
# @Software: PyCharm Community Edition
import hashlib
import hmac
import random
import string
import time
import uuid

SECRET_KEY = "DebugTalk"

# 生成指定位长度的随机字符串
def gen_random_string(str_len):
    random_char_list = []
    for _ in range(str_len):
        random_char = random.choice(string.ascii_letters + string.digits)
        random_char_list.append(random_char)

    random_string = ''.join(random_char_list)
    return random_string

# 生成UUID
def uid(flag=True):
    id = uuid.uuid1()
    id = str(id)
    if flag:
        id = str(id).replace('-', '')
        return id.replace('-','')
    return id

# 获取毫秒级时间戳
def  times():
    timestmap = time.time()
    timestmap = int(round(timestmap * 1000))
    return timestmap

#签名算法，获取签名
def get_sign(*args):
    content = ''.join(args).encode('ascii')
    sign_key = SECRET_KEY.encode('ascii')
    sign = hmac.new(sign_key, content, hashlib.sha1).hexdigest()
    return sign

if __name__ == '__main__':
    print(uid(False))
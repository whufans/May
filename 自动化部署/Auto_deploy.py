#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 9:20
# @Author  : fans
# @File    : Auto_deploy.py
# @Software: PyCharm Community Edition
from fabric.api import *
import fabric
# 设置目标主机
env.hosts = ['root@172.31.46.37:22']
# 设置多台主机用户名及密码
# env.passwords = { 'root@172.31.46.37:22': 'iflytek@206'}
# env.user = 'python'  # 多台主机用户名密码相同可以只写一次
env.password = 'iflytek@206'

# 打包
@runs_once  # 该装饰器表示只执行一次，没有的话默认每台主机都执行一次
def task_tar():  # 该场景本地文件打包本身就只需要执行一次
    with lcd('/home/python/test'):
        local('tar zcvf test.tar.gz test.py')

# 上传
@task()
def task_upload():
    run('mkdir -p /home/zhenfantest')
    # put('/home/python/test/test.tar.gz', '/home/python/temp/test.tar.gz')

def remote_info():
    with cd('/home'):
        run('ll ')

# 验证md5
def task_md5():
    # 计算本地的md5
    local_md5 = local('md5sum /home/python/test/test.tar.gz', capture=True).split('  ')[0]
    # 计算远程主机md5
    remote_md5 = run('md5sum /home/python/temp/test.tar.gz').split('  ')[0]
    print(local_md5)
    print(remote_md5)
    if remote_md5 == local_md5:
        print('上传成功')
    else:
        print('上传出错')


# 解包并执行
def task_exc():
    with cd('/home/python/temp'):
        run('tar zxvf test.tar.gz')
        run('python3 test.py')

# 调度
@task
def start():
    task_tar()
    task_upload()
    task_md5()
    task_exc()


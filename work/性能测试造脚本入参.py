#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 16:11
# @Author  : fans
# @File    : test1.py
# @Software: PyCharm Community Edition
def get_input(typeNum, eviNum):
    init_value = ''
    m = typeNum + 1
    n = eviNum + 1
    for i in range(1, m):
        init_value += '"$(code{0})":[ '.format(i)
        for j in range(1, n):
            num = (i - 1) * eviNum + j
            if (i == typeNum) and (j == eviNum):
                init_value += '("contResult": "http://172.31.234.149:88//G1/M00/0C/0F/rB_qlVy4U3eAWDwrAAAFzyHQhdc.engine","elleResult": "$(elleResult{0})","evidenceId": "$(num1)-$(num2)-$(num3)-$(num4)-$(num5)0{0}","name": "搜查笔录","ocrResult": "$(ocrResult{0})")]'.format(num)
            elif i != typeNum and j == eviNum:
                init_value += '("contResult": "http://172.31.234.149:88//G1/M00/0C/0F/rB_qlVy4U3eAWDwrAAAFzyHQhdc.engine","elleResult": "$(elleResult{0})","evidenceId": "$(num1)-$(num2)-$(num3)-$(num4)-$(num5)0{0}","name": "搜查笔录","ocrResult": "$(ocrResult{0})")],'.format(num)
            else:
                init_value += '("contResult": "http://172.31.234.149:88//G1/M00/0C/0F/rB_qlVy4U3eAWDwrAAAFzyHQhdc.engine","elleResult": "$(elleResult{0})","evidenceId": "$(num1)-$(num2)-$(num3)-$(num4)-$(num5)0{0}","name": "搜查笔录","ocrResult": "$(ocrResult{0})"),'.format(num)
    init_value = '("Archive": ("caseCause": "1101","caseId": "aefae","EvidenceTypes": (' + init_value + '),"caseType": "11"))'
    init_value = init_value.replace('(', '{')
    init_value = init_value.replace(')', '}')
    print(init_value)


if __name__ == '__main__':
    get_input(28, 7)

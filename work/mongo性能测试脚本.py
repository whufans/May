#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 10:18
# @Author  : fans
# @File    : mongo性能测试脚本.py
# @Software: PyCharm Community Edition
def get_input(typeNum, eviNum):
    init_value = ''
    m = typeNum + 1
    n = eviNum + 1
    for i in range(1, m):
        init_value += '"0$(code{0})":[ '.format(i)
        for j in range(1, n):
            num = (i - 1) * eviNum + j
            if (i == typeNum) and (j == eviNum):
                init_value += '("attachments": [("attPath": "http://192.168.84.171:88/G1/M00/0A/E2/wKhUq10ineqAbhsfAAR-ZtcH4ZQ641.jpg","attName": "image0000002A.jpg")],"contResult": "$(evidenceId{0})/contResultFromMongo","elleResult": "$(evidenceId{0})/elleResultFromMongo","evidenceId": "$(evidenceId{0})","name": "搜查笔录","ocrResult": "$(evidenceId{0})/ocrResultFromMongo")]'.format(num)
            elif i != typeNum and j == eviNum:
                init_value += '("attachments": [("attPath": "http://192.168.84.171:88/G1/M00/0A/E2/wKhUq10ineqAbhsfAAR-ZtcH4ZQ641.jpg","attName": "image0000002A.jpg")],"contResult": "$(evidenceId{0})/contResultFromMongo","elleResult": "$(evidenceId{0})/elleResultFromMongo","evidenceId": "$(evidenceId{0})","name": "搜查笔录","ocrResult": "$(evidenceId{0})/ocrResultFromMongo")],'.format(num)
            else:
                init_value += '("attachments": [("attPath": "http://192.168.84.171:88/G1/M00/0A/E2/wKhUq10ineqAbhsfAAR-ZtcH4ZQ641.jpg","attName": "image0000002A.jpg")],"contResult": "$(evidenceId{0})/contResultFromMongo","elleResult": "$(evidenceId{0})/elleResultFromMongo","evidenceId": "$(evidenceId{0})","name": "搜查笔录","ocrResult": "$(evidenceId{0})/ocrResultFromMongo"),'.format(num)
    init_value = '("Archive": ("caseCause": "940300","caseId": "aefae","EvidenceTypes": (' + init_value + '),"caseType": "0101"))'
    init_value = init_value.replace('(', '{')
    init_value = init_value.replace(')', '}')
    print(init_value)


if __name__ == '__main__':
    get_input(25, 2)

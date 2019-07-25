#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/24 13:42
# @Author  : fans
# @File    : test.py
# @Software: PyCharm Community Edition
from common.basic_data import Extract,Context
import pyjson
import jsonpath
jsonobj ={"code":"1","message":"检验完成！","total":0,"rows":[{"caseId":"ewfaeswf","flawList":[{"ruleId":"c35663e265104eb58346c7846e7de9b4","conditionId":"ebb5112e9b1d4a68a022ce73e4ed6197","conResult":"缺失辨认人签名、注明日期","conMessage":"判断辨认笔录是否缺失辨认人签名、注明日期","page":[2],"location":[{"w":1646,"x":0,"h":1169,"y":1169}]}],"evidenceId":"1a5d514d-e4d7-49db-b130-a6212d4a00d5"},{"caseId":"ewfaeswf","flawList":[{"ruleId":"80cf27691b014f6990fd04e9e5940e21","conditionId":"e3fcf4b02768491aa128b8a4a973b82f","conResult":"缺失辨认人捺印","conMessage":"判断辨认笔录是否缺失辨认人捺印","page":[2],"location":[{"w":1646,"x":0,"h":1169,"y":1169}]}],"evidenceId":"1a5d514d-e4d7-49db-b130-a6212d4a00d5"}]}
# code = jsonpath.jsonpath(jsonobj,'$..rows[0].flawList')
# print(code,type(code))
info =  {"caseCause": "$..total","caseId":"code"}
pyjson.compare()
for k, v in info.items():
    info[k] = jsonpath.jsonpath(jsonobj, v)[0]
    print(info)
print(info)


# Extract.json_extract(jsonobj=jsonobj, info=info)
# for item in info.keys():
#     res1 = getattr(Context,item)
#     print(res1)











# -*- coding:utf-8 _*-
import re
import jsonpath
from common.config import ConfigLoader

class DoRegex:
    @staticmethod
    def replace(target, pattern= '\$\{(.*?)\}', flags=0): # 查找并且替换
        pattern = re.compile(pattern,flags)
        while pattern.search(target):  # 找到一个就返回match
            m = pattern.search(target)
            key = m.group(1)  # 取第一个分组里面的字符，也就是我们需要的key
            from common.basic_data import Context
            user = getattr(Context, key)
            target = pattern.sub(str(user), target, count=1)
        return target

class Extract:
    @staticmethod
    def json_extract(target, jsonobj):
        for k, v in target.items():
            from common.basic_data import Context
            target[k] = jsonpath.jsonpath(jsonobj, v)[0]
            setattr(Context, k, target[k])

    @staticmethod
    def re_extract(target,res, pattern, group='$1$', flags=0):
        pattern = re.compile(pattern, flags)
        extract_res = pattern.findall(target)
        group_pattern = '\$(.*?)\$'
        group_pattern = re.compile(group_pattern)
        group = re.findall(group_pattern, group)
        group = [int(i) for i in group]
        for i in  group:
            a = []
            for item in extract_res:
                a.append(item[i-1])
            setattr(Context, '{}_g{}'.format(res,i), str(a))



class Context:
    config = ConfigLoader()
    # 测试数据
    normal_user = config.get('basic', 'normal_user')
    normal_pwd = config.get('basic', 'normal_pwd')
    caseCause = config.get('basic', 'normal_member_id')
    # 管理员数据
    admin_user = config.get('basic', 'admin_user')
    admin_pwd = config.get('basic', 'admin_pwd')
    # 借款人测试数据
    loan_member_id = config.get('basic', 'loan_member_id')

if __name__ == '__main__':
    # target = '{"Archive":{"caseCause":"1101","caseId":"zsgzesg","EvidenceTypes":{"220301":[{"contResult":"http://172.31.234.149:88//G1/M00/0C/0F/rB_qlVy4U3eAWDwrAAAFzyHQhdc.engine","elleResult":"http://172.31.234.149:88//G1/M00/0C/0F/rB_qlVy4U3eADQ6DAAAAEoCbJx8.engine","evidenceId":"1649b7fa-c4fe-4a04-b7f2-3d597bc4c364","name":"证据一","ocrResult":"http://172.31.234.149:88//G1/M00/0C/0F/rB_qlVy4U3eAEuCSAAGGCpTJRL4.engine"},{"contResult":"http://172.31.234.149:88//G1/M00/0C/0F/rB_qlVy4U3eAWDwrAAAFzyHQhdc.engine","elleResult":"http://172.31.234.149:88/G1/M00/08/AC/rB_qlVy1cyyAP9sHAAAAEoCbJx8.engine","evidenceId":"1649b7fa-c4fe-4a04-b7f2-3d597bc4c365","name":"证据二","ocrResult":"http://172.31.234.149:88/G1/M00/0C/76/rB_qlVy5gM-ADj9dAAOMu_N3n_I.engine"}],"220501":[{"contResult":"http://172.31.234.149:88//G1/M00/0C/0F/rB_qlVy4U3eAKeDFAAACCHRF93Q.engine","elleResult":"http://172.31.234.149:88//G1/M00/0C/0F/rB_qlVy4U3eAa5anAAAAEoCbJx8.engine","evidenceId":"ad278629-c7f7-4467-8cba-3ff7577bb4f0","name":"证据三","ocrResult":"http://172.31.234.149:88//G1/M00/0C/0F/rB_qlVy4U3eAPPQGAABx-KB4H7M.engine"}]},"caseType":"11"}}'
    # s = {'name': {'"contResult":"(.*?)"', 1, 1, 0}}
    # pattern =  r'([a-z]+) ([a-z]+)'
    # flag = re.I
    # target = 'Hello World Wide Web'
    # s = Extract.re_extract(target=target,res ='kk',pattern=pattern,group='$1$$2$', flags=flag)
    # print(getattr(Context,'kk_g1'))
    # print(getattr(Context,'kk_g2'))
    print(Context.__dict__)


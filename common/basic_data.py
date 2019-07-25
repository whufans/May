# -*- coding:utf-8 _*-
import re
import jsonpath
from common.config import ConfigLoader

class DoRegex:
    @staticmethod
    def replace(target): # 查找并且替换
        pattern = '\$\{(.*?)\}'
        while re.search(pattern, target):  # 找到一个就返回match
            m = re.search(pattern, target)
            key = m.group(1)  # 取第一个分组里面的字符，也就是我们需要的key
            from common.basic_data import Context
            user = getattr(Context, key)
            target = re.sub(pattern, str(user), target, count=1)
        return target

class Extract:
    @staticmethod
    def json_extract(jsonobj, info):
        for k, v in info.items():
            from common.basic_data import Context
            info[k] = jsonpath.jsonpath(jsonobj, v)[0]
            setattr(Context, k, info[k])

class Context:
    config = ConfigLoader()
    # 测试数据
    normal_user = config.get('basic', 'normal_user')
    normal_pwd = config.get('basic', 'normal_pwd')
    normal_member_id = config.get('basic', 'normal_member_id')
    # 管理员数据
    admin_user = config.get('basic', 'admin_user')
    admin_pwd = config.get('basic', 'admin_pwd')
    # 借款人测试数据
    loan_member_id = config.get('basic', 'loan_member_id')
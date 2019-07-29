# -*- coding:utf-8 _*-
import json
import requests
from common.config import ConfigLoader

class Request:

    def __init__(self, method, url, data=None, cookies=None, headers=None, is_json=False, **kwargs):
        try:
            config = ConfigLoader()
            url_pre = config.get('api', 'url_pre')
            url = url_pre + url  # 拼接请求地址
            method = method.lower()
            if isinstance(data,dict) or isinstance(data,str):
                if isinstance(data,dict):
                    data = data
                elif isinstance(data,str):
                    try:
                        data = json.loads(data)
                    except Exception as e:
                        print(e)
                        data = eval(data)
            else:
                print("{}格式不正确".format(data))
            if method == 'get':
                self.resp = requests.get(url=url, params=data, cookies=cookies, headers=headers, **kwargs)
            elif method == 'post':
                if  is_json:
                    self.resp = requests.post(url=url, json=data, cookies=cookies, headers=headers, **kwargs)
                else :
                    self.resp = requests.post(url=url, data=data, cookies=cookies, headers=headers, **kwargs)
            elif method == 'delete':
                self.resp = requests.delete(url=url, data=data, cookies=cookies, headers=headers, **kwargs)
            else:
                self.resp = None
                print("{}请求方式错误".format(method))
        except Exception as e:
            raise e

    def get_status_code(self):  # 返回响应码
        return self.resp.status_code

    def get_text(self):  # 返回str类型的响应体
        return self.resp.text

    def get_json(self):  # 返回dict类型的响应体
        res_json = self.resp.json()
        # 通过json.dumps函数将字典转换成格式化后的字符串
        # res_str = json.dumps(res_dict, ensure_ascii=False, indent=4)
        # print('response: ', res_str)  # 打印响应
        return res_json

    def get_cookies(self, key=None):  # 返回cookies
        if key is not None:
            return self.resp.cookies[key]
        else:
            return self.resp.cookies


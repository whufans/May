# -*- coding:utf-8 _*-
import json
import requests
from common.config import ConfigLoader

class Request:

    def __init__(self, method, url, data=None, cookies=None, headers=None):
        try:
            config = ConfigLoader()
            url_pre = config.get('api', 'url_pre')
            url = url_pre + url  # 拼接请求地址
            print(url)
            if method == 'get':
                self.resp = requests.get(url=url, params=data, cookies=cookies, headers=headers)
            elif method == 'post':
                self.resp = requests.post(url=url, json=data, cookies=cookies, headers=headers)
            elif method == 'delete':
                self.resp = requests.delete(url=url, data=data, cookies=cookies, headers=headers)
        except Exception as e:
            raise e

    def get_status_code(self):  # 返回响应码
        return self.resp.status_code

    def get_text(self):  # 返回str类型的响应体
        return self.resp.text

    def get_json(self):  # 返回dict类型的响应体
        res_dict = self.resp.json()
        # 通过json.dumps函数将字典转换成格式化后的字符串
        res_str = json.dumps(res_dict, ensure_ascii=False, indent=4)
        print('response: ', res_str)  # 打印响应
        return res_str

    def get_cookies(self, key=None):  # 返回cookies
        if key is not None:
            return self.resp.cookies[key]
        else:
            return self.resp.cookies
if __name__ == '__main__':
    r = Request('post','/evidence-check/check/checkInput',{"Archive":{"caseCause":"1101","caseId":"awacdea","EvidenceTypes":{"220301":[{"contResult":"http://172.31.98.187:88/G1/M00/31/D0/rB9iu10UFcqASCnQAAAIxUN8_ck.engine","elleResult":"http://172.31.98.187:88/G1/M00/31/D0/rB9iu10UFcqAXNXoAAADo4skYMQ.engine","evidenceId":"5c2772a2-cd5f-48f4-9d7d-a25dc40b8f1c","name":"现场辨认笔录","ocrResult":"http://172.31.98.187:88/G1/M00/31/D0/rB9iu10UFcqAfyeGAAJ640lT0ic.engine","otherKey":"控"}],"220501":[{"contResult":"http://172.31.98.187:88/G1/M00/31/D0/rB9iu10UFcqAKMPdAAAH28h_mbs.engine","elleResult":"http://172.31.98.187:88/G1/M00/31/D0/rB9iu10UFcqALFrDAAAE-pCRmWo.engine","evidenceId":"8ae6b595-f196-4e14-9dd6-2258bf185aae","name":"现场辨认笔录","ocrResult":"http://172.31.98.187:88/G1/M00/31/D0/rB9iu10UFcqAINjRAAIj9s3HtzY.engine","otherKey":"11"}],"220001":[{"contResult":"http://172.31.98.187:88/G1/M00/31/D0/rB9iu10UFcqAW2lUAAABUMWmkVc.engine","elleResult":"http://172.31.98.187:88/G1/M00/31/D0/rB9iu10UFcqAGR1NAAAAEoCbJx8.engine","evidenceId":"4479da8c-5d74-4818-a6c5-4a733a9f2986","name":"图片证据","ocrResult":"http://172.31.98.187:88/G1/M00/31/D0/rB9iu10UFcqAYdhfAABrCcHrmCE.engine","otherKey":"控告"}]},"caseType":"11"}})
    print(r.get_json())

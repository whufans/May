# -*- coding:utf-8 _*-
import json
import unittest
from ddt import ddt, data
from common import constants
from common.do_excel import DoExcel
from common.request import Request
from common.logger import MyLog
from common.assertion import My_assertion
from common.basic_data import Extract,Context,DoRegex

do_excel = DoExcel(constants.case_file)  # 实例化一个DoExcel对象
sheet_name = 'login'
cases = do_excel.get_cases(sheet_name)

@ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        print('测试准备')

    @data(*cases)
    def test_login(self, case):
        case.data = DoRegex.replace(case.data)
        data = json.loads(case.data)
        MyLog.info('测试用例名称：{0}'.format(case.title))
        MyLog.info('测试用例数据：{0}'.format(case.data))
        resp = Request(method=case.method, url=case.url, data=data)  # 通过封装的Request类来完成接口的调用
        MyLog.info('status_code:{0}'.format(resp.get_status_code()))  # 打印响应码
        resp_str = resp.get_json()  # 获取请求响应，字典
        MyLog.info('测试用例预期结果：{0}'.format(case.expected))
        MyLog.info('测试用例响应结果：{0}'.format(resp_str))
        try:
            # self.assertTrue(My_assertion.my_assert(eval(case.expected),resp_str))
            self.assertEqual(eval(case.expected),resp_str)
            MyLog.info('测试成功')
            do_excel.write_back_by_case_id(sheet_name=sheet_name, case_id=case.case_id, actual=str(resp_str),result='PASS')
            if  case.extract:
                extract_info =  json.loads(case.extract)
                Extract.json_extract(jsonobj=resp_str, info=extract_info)
        except AssertionError as e:
            MyLog.error('测试失败')
            do_excel.write_back_by_case_id(sheet_name=sheet_name, case_id=case.case_id,actual=resp.get_json(),result='FAIL')
            raise   e

    def tearDown(self):
        print('测试清除')


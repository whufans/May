# -*- coding:utf-8 _*-
import unittest
import HTMLTestRunnerNew
from common import constants
# suite = unittest.TestSuite()  # 测试用例集合
# loader = unittest.TestLoader()  # 加载用例
# suite.addTest(loader.loadTestsFromTestCase(TestLogin))
# suite.addTest(loader.loadTestsFromModule(test_register))

# 自动查找testcases目录下，以test开头的.py文件里面的测试类
discover = unittest.defaultTestLoader.discover(constants.testcases_dir, pattern="test*.py", top_level_dir=None)
print(constants.reports_html)
with open(constants.reports_html, 'wb+') as file:
    # 执行用例
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title='证据校验平台接口测试报告',
                                              description='测试结果',
                                              tester='范震')
    runner.run(discover)  # 执行查找到的用例

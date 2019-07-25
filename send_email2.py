#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 18:48
# @Author  : fans
# @File    : send_email2.py
# @Software: PyCharm Community Edition
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common import constants
import HTMLTestRunnerNew
from email.header import Header
import unittest
import time

class sendEmail:
    def send_email(self, sender, pwd, receivers, html_path):
        # 创建一个带附件的实例
        with open(html_path,encoding='UTF-8') as f:
            mail_msg = f.read()

        now = time.strftime('%Y%m%d')  # 获取时间戳
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receivers
        subject = "接口自动化测试报告"+now
        message['Subject'] = Header(subject, 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText('这是Python 邮件发送测试……', 'plain', 'utf-8'))
        message.attach(MIMEText(mail_msg, 'html', 'utf-8'))

        # 构造附件1，传送当前目录下的 test.txt 文件
        att1 = MIMEText(open(html_path, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="report.html"'
        message.attach(att1)

        # 构造附件2，传送当前目录下的 runoob.txt 文件
        # att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
        # att2["Content-Type"] = 'application/octet-stream'
        # att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
        # message.attach(att2)

        try:
            s = smtplib.SMTP_SSL("mail.iflytek.com", timeout=30)  # 连接smtp邮件服务器,端口默认是25
            s.login(sender, pwd)  # 登陆服务器
            s.sendmail(sender, receivers.split(','), message.as_string())  # 发送邮件
            s.close()
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")

if __name__ == '__main__':
    new_report = constants.reports_html
    discover = unittest.defaultTestLoader.discover(constants.testcases_dir, pattern="test*.py", top_level_dir=None)
    with open(new_report, 'wb+') as file:
        # 执行用例
        runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                               verbosity=2,
                                               title='证据校验平台接口测试报告',
                                               description='测试结果',
                                               tester='范震')
        runner.run(discover)  # 执行查找到的用例

    sender = 'zhenfan@iflytek.com'
    pwd = "Whu13579!"
    receivers = 'zhenfan@iflytek.com,1696669410@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    sendEmail().send_email(sender, pwd, receivers, new_report)
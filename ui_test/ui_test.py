#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 8:44
# @Author  : fans
# @File    : ui_test.py
# @Software: PyCharm Community Edition
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument('disable-infobars')
driver =  webdriver.Chrome(chrome_options = options)
driver.get('https://www.baidu.com')
driver.maximize_window()
window_handles = driver.window_handles
driver.find_element_by_id('kw').send_keys('bing')
driver.find_element_by_id('su').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
print(len(window_handles))
WebDriverWait(driver,10,0.5).until(EC.new_window_is_opened(window_handles))
window_handles = driver.window_handles
print(len(window_handles))
driver.switch_to.window(window_handles[-1])
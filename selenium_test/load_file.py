# -*- coding: utf-8 -*-

from selenium import webdriver
import os
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)

# HTML文件地址
file_path = 'file:///' + os.path.abspath('E:/WorkItem/TestItem/dyplm-2TestCase/dyplmlit_testcase/HtmlCase/upfile.html')
# 获取HTML文件
driver.get(file_path)
sleep(2)

# 定位上传按钮，添加本地文件
driver.find_element_by_name("file").send_keys('E:/XMindCrack.jar')
sleep(3)

driver.quit()
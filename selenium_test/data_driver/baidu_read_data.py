# -*- coding: utf-8 -*-
"""
数据驱动测试
文件数据
"""

from selenium import webdriver
import os
from time import sleep

# 以只读方式打开文件
source = open("E:/WorkItem/TestItem/dyplm-2TestCase/dyplmlit_testcase/Data/search_data.txt")
values = source.readlines()  # 逐行读取文件内容
source.close()

for search_data in values:
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(search_data)
    sleep(2)
    driver.find_element_by_id("su").click()
    sleep(4)
    driver.quit()
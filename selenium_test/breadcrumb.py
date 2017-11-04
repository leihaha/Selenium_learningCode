# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
import os
"""
使用层级定位
"""

driver = webdriver.Chrome()
file_path = "file:///" + os.path.abspath(
    "E:\\WorkItem\\TestItem\\dyplm-2TestCase\\dyplmlit_testcase\\HtmlCase\\breadcrumb.html")
driver.get(file_path)
sleep(1)

navs = driver.find_element_by_class_name("breadcrumb").find_elements_by_tag_name("a")
for nav in navs:
    print(nav.text)
sleep(2)

# 获取当前层级
# 由于页面上可能有很多class命名重合的元素
# 使用层级定位最为保险
print(driver.find_element_by_class_name("breadcrumb").find_element_by_class_name("active").text)
# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
import os
"""
货物测试对象的属性
"""

driver = webdriver.Chrome()
file_path = "file:///" + os.path.abspath("E:/"
                                         "WorkItem/TestItem/dyplm-2TestCase/dyplmlit_testcase/HtmlCase/attribute.html")
driver.get(file_path)
sleep(2)

link = driver.find_element_by_id("tooltip")
sleep(1)

# 获取tooltip的内容
print(link.get_attribute("title"))

# 获取该链接的text
print(link.text)

driver.quit()
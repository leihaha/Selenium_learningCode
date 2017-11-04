# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
import os
"""
获取分页
查看当前所在页面
"""
driver = webdriver.Chrome()
file_path = "file:///" + os.path.abspath(
    "E:/WorkItem/TestItem/dyplm-2TestCase/dyplmlit_testcase/HtmlCase/pagination.html")
driver.get(file_path)
sleep(1)

# 获取所有分页的数量
# 注意要去掉上一个和下一个 -2
total_pages = len(driver.find_element_by_class_name("pagination").find_elements_by_tag_name("li")) - 2
print("total page is %s" % total_pages)
sleep(2)

# 获取当前页面的url以及当前页面是第几页
current_page = driver.find_element_by_class_name("pagination").find_element_by_class_name("active")
print("current page is %s" % current_page.text)
sleep(2)

driver.quit()
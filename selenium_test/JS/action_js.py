# -*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath("E:/WorkItem/TestItem/dyplm-2TestCase/dyplmlit_testcase/HtmlCase/js.html")
driver.get(file_path)
sleep(6)

# 通过JS隐藏选中的元素
# 方法一
driver.execute_script('$("#tooltip").fadeOut();')
sleep(3)

# 方法二
button = driver.find_element_by_class_name('btn')
driver.execute_script('$(arguments[0]).fadeOut()', button)
sleep(4)

driver.quit()
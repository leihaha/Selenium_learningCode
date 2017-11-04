# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
import os

"""
获取测试对象的状态：
    是否显示：element.is_displayed()
    是否存在：find_element_by_xxx()
    是否被选中：一般是判断表单元素，element.is_select()
    是否enable：element.is_enable()
"""

driver = webdriver.Chrome()
file_path = "file:///" + os.path.abspath("E:/WorkItem/TestItem/dyplm-2TestCase/dyplmlit_testcase/HtmlCase/status.html")
driver.get(file_path)
sleep(2)

text_field = driver.find_element_by_name("user")
print(text_field.is_displayed())
sleep(1)

# 由于button使用CSS方法去disabled（并不是真正的disable）
# 如果直接使用enabled()方法去判断button，返回的是true
# 此时需要判断其class里面是否有disabled值来判断该元素是否处于disabled
print(driver.find_element_by_class_name("btn").is_enabled())

# 隐藏text_field
driver.execute_script('$(arguments[0]).hide()', text_field)
print(text_field.is_displayed())
sleep(1)

# 选择radio
radio = driver.find_element_by_name("radio")
radio.click()
radio.is_selected()
sleep(1)

# 判断元素是否存在
try:
    driver.find_element_by_name("none")
except:
    print("element is not exist")
sleep(1)

driver.quit()
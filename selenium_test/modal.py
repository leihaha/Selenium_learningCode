# -*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep
import os
"""
处理对话框（弹出框）
"""

if 'HTTP_PROXY' in os.environ:
    del os.environ['HTTP_PROXY']

driver = webdriver.Firefox()
driver.implicitly_wait(10)
file_path = 'file:///' + os.path.abspath('E:/WorkItem/TestItem/dyplm-2TestCase/dyplmlit_testcase/HtmlCase/modal.html')
driver.get(file_path)
sleep(10)

# 打开对话框
driver.find_element_by_id('show_modal').click()
sleep(3)

# 点击对话框中的链接
# 由于对话框中的元素被蒙版多遮挡，直接点击会报 Element is not click的错误
# 使用js模拟click

link = driver.find_element_by_id("myModal").find_element_by_id('click')
driver.execute_script('$(arguments[0]).click()', link)
sleep(3)

# 关闭对话框
buttons = driver.find_element_by_class_name('modal-footer').find_elements_by_tag_name('button')
buttons[0].click()
sleep(3)

driver.quit()
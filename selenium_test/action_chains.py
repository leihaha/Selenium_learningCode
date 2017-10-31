# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

"""
    ActionChains类提供鼠标操作的常用方法
    perform() 执行所有ActionChains中存储的行为
    context_click() 右击
    double_click()  双击
    drag_and_drop(element, target) 托动
    move_to_element() 悬停
"""

# 定位到要悬停的元素
sleep(5)
above = driver.find_element_by_link_text("设置")
# 对定位到的元素执行鼠标悬停操作
sleep(5)
ActionChains(driver).move_to_element(above).click().perform()


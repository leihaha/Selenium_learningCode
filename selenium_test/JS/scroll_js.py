# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

"""
设置浏览器窗口大小：set_window_size(num,num)
"""
# 浏览器窗口最大化
driver.maximize_window()
sleep(2)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(3)

"""
window.scrollTo(左边距，上边距)
"""
# 通过JavaScript设置浏览器窗口的滚动条位置
js = "window.scrollTo(100,450);"
driver.execute_script(js)
sleep(3)

driver.quit()
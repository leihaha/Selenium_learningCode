# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
"""
处理多窗口
"""

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://www.baidu.com")


# 获取百度搜索窗口句柄
search_windows = driver.current_window_handle

# sleep(2)
driver.find_element_by_css_selector("a.lb:nth-child(7)").click()
sleep(2)
driver.find_element_by_css_selector("#TANGRAM__PSP_10__submitWrapper > a.pass-reglink").click()
# sleep(2)
# 获取当前所有打开的窗口的句柄
all_handle = driver.window_handles

# 进入注册窗口
for handle in all_handle:
    if handle != search_windows:
        driver.switch_to.window(handle)
        print("now register window!")
        sleep(3)
        driver.find_element_by_name("userName").send_keys("username")
        driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__password"]').send_keys("password")
        sleep(3)
driver.quit()
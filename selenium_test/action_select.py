# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import selenium.webdriver.support.ui as ui
"""
鼠标悬停
选择下拉选项
"""

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

sleep(3)
# 鼠标悬停至“设置”链接
setting = driver.find_element_by_css_selector("#u1 > a.pf")
print(setting.text)
setting.click()

# 打开搜索设置
driver.find_element_by_css_selector("#wrapper > div.bdpfmenu > a.setpref").click()
sleep(2)

# 显示搜索条数
sel = driver.find_element_by_xpath('//*[@id="nr"]')
Select(sel).select_by_value("50")
sleep(2)

driver.quit()
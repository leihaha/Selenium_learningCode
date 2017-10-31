# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver =  webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.implicitly_wait(10)

sleep(2)
# 鼠标悬停至“设置”链接
setting = driver.find_element_by_xpath('//*[@id="u1"]/a[8]')
sleep(2)
ActionChains(driver).move_to_element(setting).perform()

sleep(5)
# 打开搜索设置
driver.find_element_by_link_text("搜索设置").click()

sleep(3)
# 保存设置
driver.find_element_by_xpath('//*[@id="gxszButton"]/a[1]').click()

sleep(3)
# 接收警告框
driver.switch_to.alert.accept()

"""
警告框方法：
    text：返回文字信息
    accept(): 接受现有警告框
    dismiss(): 解散现有警告框
    send_keys(keysToSend): 发送文本至警告框 
"""

driver.quit()
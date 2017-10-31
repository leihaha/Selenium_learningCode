# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

print("Before search==========")

# 获取当前页面的标题
now_title = driver.title
print(now_title)

# 获取当前页面的url
now_url = driver.current_url
print(now_url)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

print("Afore search==========")

now_title = driver.title
print(now_title)

now_url = driver.current_url
print(now_url)

# 获取文本信息
nums = driver.find_element_by_class_name("nums").text
print(nums)

driver.quit()
# -*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
sleep(2)

# 给搜索输入框标红
js = 'var q=document.getElementById(\"kw\"); q.style.border=\"5px solid red\";'

# 调用js
driver.execute_script(js)
sleep(5)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

driver.quit()
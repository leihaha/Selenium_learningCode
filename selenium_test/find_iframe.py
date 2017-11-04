# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
"""
iframe操作
switch_to.frame(),官方说使用name属性，实际操作证明id也可以
"""

driver = webdriver.Chrome()
driver.get("http://www.126.com")
driver.implicitly_wait(10)

sleep(3)
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="x-URS-iframe"]'))


sleep(5)
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("giorgialei@126.com")
sleep(5)
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("lqj1393460778")
sleep(3)
driver.find_element_by_id("dologin").click()

driver.switch_to.default_content()
sleep(2)

driver.quit()

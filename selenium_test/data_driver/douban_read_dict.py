# -*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep
import os
from PythonCode import source_dict

for user, passw in source_dict.zidian().items():
    driver = webdriver.Chrome()
    driver.get("http://www.douban.com")
    sleep(3)

    driver.find_element_by_id("form_email").clear()
    driver.find_element_by_id("form_email").send_keys(user)
    sleep(2)
    driver.find_element_by_id("form_password").clear()
    driver.find_element_by_id("form_password").send_keys(passw)
    sleep(2)
    driver.find_element_by_xpath('//*[@id="lzform"]/fieldset/div[3]/input').click()
    sleep(5)

    driver.close()
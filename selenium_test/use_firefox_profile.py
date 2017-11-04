# -*- coding: utf-8 -*-

from selenium import webdriver
"""
使用Firefox的profile文件
可以使用该文件记住密码
免去登录步骤
"""
# 在selenium中指定使用已存在的Firefox profile文件，以实现一段时间的免登陆功能
# Firefox的profile文件记录了书签、记住的password、cookie等数据
# profile文件可以通过在运行输入框中输入%APPDATA%\Mozilla\Firefox\Profiles\获取

# 传入profile所在的绝对路径
profile = webdriver.FirefoxProfile('C:\Users\cr\AppData\Roaming\Mozilla\Firefox\Profiles\pioeozkh.default')
driver = webdriver.Firefox(profile)
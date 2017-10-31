# -*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep

"""
操作cookie方法：
    get_cookies():获取所有cookie信息
    get_cookie(name)：获取某个cookie
    add_cookie(cookie_dict): 添加cookie
    delete_cookie(name,optionsString):删除cookie信息
    delete_all_cookies(): 删除所有cookie信息
"""

driver = webdriver.Chrome()
driver.get("http://www.youdao.com")

# 获得cookie信息
cookie = driver.get_cookies()
# 打印
print(cookie)

"""
cookie数据是以字典的形式进行存放
"""

# 向cookie的name和value中添加会话信息
driver.add_cookie({'name':'key-aaa', 'value': 'value-bbb'})

# 遍历cookies中的name和value信息并打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))

driver.quit()
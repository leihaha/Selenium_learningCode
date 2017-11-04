# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 引入Keys包
from time import sleep
"""
键盘按键、组合键操作
"""

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

above = driver.find_element_by_id("kw")

# 在搜索框输入内容
action1 = above.send_keys("seleniumm")
sleep(2)

# 删除最后的m,通过send_keys()调用按键
action2 = above.send_keys(Keys.BACK_SPACE)
sleep(2)

# 输入一个空格
action3 = above.send_keys(Keys.SPACE)
action4 = above.send_keys("教程")
sleep(2)

# 组合键Ctrl+a 全选
action5 = above.send_keys(Keys.CONTROL, 'a')
sleep(2)
# Ctrl+x 剪切
action6 = above.send_keys(Keys.CONTROL, 'x')
sleep(2)
# Ctrl+v 复制
action7 = above.send_keys(Keys.CONTROL, 'v')
sleep(2)
# 回车
action8 = above.send_keys(Keys.ENTER)
sleep(2)
driver.quit()
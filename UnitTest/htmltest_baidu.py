# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, re
from time import sleep
import HtmlTestRunner


class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        sleep(5)
        driver.maximize_window()
        sleep(3)
        # 通过JavaScript设置浏览器窗口的滚动条位置
        js = "window.scrollTo(100,450);"
        driver.execute_script(js)
        sleep(3)
        driver.find_element_by_xpath(".//*[@id='8']/h3/a").click()
        sleep(5)
        driver.close()

    def test_baidu_set(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        sleep(3)
        driver.find_element_by_xpath(".//*[@id='u1']/a[8]").click()
        sleep(2)
        driver.find_element_by_link_text(u"搜索设置").click()
        sleep(3)
        Select(driver.find_element_by_id("nr")).select_by_visible_text(u"每页显示20条")
        driver.find_element_by_link_text(u"保存设置").click()
        sleep(3)
        driver.switch_to.alert.accept()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='E:/WorkItem/TestItem/dyplm-2TestCase/dyplmlit_testcase/'))

    """
    testunit = unittest.TestSuite()  # 定义一个单元测试容器
    testunit.addTest(Baidu("test_baidu_search"))
    testunit.addTest(Baidu("test_baidu_set"))

    runner = HtmlTestRunner.HTMLTestRunner(
        output="E:/WorkItem/TestItem/dyplm-2TestCase/dyplmlit_testcase/",  # 定义报告所写入的文件
        report_title='My Report')

    runner.run(testunit)
    """

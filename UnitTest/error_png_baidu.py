# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from time import sleep
"""
捕获错误截图
"""


class Baidu(unittest.TestCase):
    def setUp(self):
        """
        setUp设置初始化部分
        在测试用例执行前，这个方法中的函数将先被调用
        """
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"
        # 脚本运行时错误的信息将被打印到这个列表中
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_baidu(self):
        """
        需要执行的测试脚本
        :return:
        """
        driver = self.driver
        driver.get(self.base_url + "/")

        # 捕获错误截图示例
        try:
            driver.find_element_by_id("kwdddd").send_keys("selenium")
        except:
            driver.get_screenshot_as_file(
                "E:\\WorkItem\\TestItem\\dyplm-2TestCase\\dyplmlit_testcase\\error_png\\kw.png")

        driver.find_element_by_id("su").click()
        sleep(5)

    def tearDown(self):
        """
        tearDown方法在每个测试方法执行后调用
        在此做所有清理工具，如退出浏览器
        :return:
        """
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)  # 对前面verificationErrors方法获得的列表进行比较


if __name__ == "__main__":
    unittest.main()

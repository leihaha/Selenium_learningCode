# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from time import sleep


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
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        sleep(5)
        driver.find_element_by_xpath(".//*[@id='8']/h3/a").click()
        sleep(3)
    """
    is_element_present函数用于查找页面元素是否存在
    判断元素是否存在一般都在testcase中，此函数用处不大
        def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True
    """

    def is_alert_present(self):
        """
        对弹窗异常的处理
        :return:
        """
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException:
            return False
        return True

    def close_alert_and_get_its_text(self):
        """
        关闭警告以及对得到文本框的处理
        :return:
        """
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

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

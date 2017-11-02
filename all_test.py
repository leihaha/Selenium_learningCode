# -*- coding: utf-8 -*-

"""
使用测试套件运行多个测试用例脚本
"""

import unittest, doctest
from UnitTest import unit_selenium_baidu, error_png_baidu, htmltest_baidu
import HtmlTestRunner

suite = doctest.DocTestSuite()

# 罗列要执行的文件
suite.addTest(unittest.makeSuite(unit_selenium_baidu.Baidu))
suite.addTest(unittest.makeSuite(error_png_baidu.Baidu))
suite.addTest(unittest.makeSuite(htmltest_baidu.Baidu))

# unittest.TextTestRunner().run(suite)

runner = HtmlTestRunner.HTMLTestRunner(output='E:/WorkItem/TestItem/dyplm-2TestCase/dyplmlit_testcase/')
runner.run(suite)
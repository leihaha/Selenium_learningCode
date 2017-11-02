# -*- coding: utf-8 -*-

from PythonCode.widget import Widget
import unittest


# 执行测试的类
# 所有执行测试的类都继承于TestCase类
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()

    # 测试getsize()方法的测试用例
    def testSize(self):
        self.assertEqual(self.widget.getsize(), (40, 40))

    # 测试resize()方法的测试用例
    def testResize(self):
        self.widget.resize(100, 100)
        self.assertEqual(self.widget.getsize(), (100,100))

    def tearDown(self):
        self.widget.dispose()
        self.widget = None


# 构造测试集
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testSize"))
    suite.addTest(WidgetTestCase("testResize"))
    return suite
"""
构造测试集
def suite():
    return unittest.makeSuite(WidgetTestCase, "test")
"""

if __name__ == "__main__":
    unittest.main(defaultTest="suite")


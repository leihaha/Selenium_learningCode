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
        self.assertEqual(self.widget.getsize(), (100, 100))

    def tearDown(self):
        self.widget.dispose()
        self.widget = None
"""
使用main全局方法将一个单元测试模块编程可以直接运行的测试脚本
main()方法使用TestLoader类来搜索所有包含在该模块中的测试方法并自动执行它们
"""
if __name__ == "__main__":
    unittest.main()   # 必须按约定以test开头命名所有测试方法


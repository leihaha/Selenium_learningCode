# -*- coding: utf-8 -*-

"""
被测试类：widget.py
使用unittest测试框架
测试类：auto.py
"""

class Widget:
    def __init__(self, size=(40, 40)):
        self._size = size

    def getsize(self):
        return self._size

    def resize(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("illegal size")
        self._size = (width, height)

    def dispose(self):
        pass
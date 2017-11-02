# -*- coding: utf-8 -*-

"""
通过改脚本控制UnitTest下的所有测试用例
执行所有测试用例，并将脚本的执行结果输出到一个log文件中
"""

import os

# 列出用例文件夹下的所有用例文件
caselist = os.listdir('E:\\WorkItem\\TestItem\\dyplm-2TestCase\\dyplmlit_testcase\\UnitTest')
for a in caselist:
    s = a.split('.')[1:][0]
    if s == 'py':
        # 执行DOS命令并将结果保存到log.txt中
        os.system('E:\\WorkItem\\TestItem\\dyplm-2TestCase\\dyplmlit_testcase\\UnitTest\\%s 1>>log.txt 2>&1'%a)
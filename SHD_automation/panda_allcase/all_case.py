#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2018/1/13 17:07
import HTMLTestRunner
import unittest
import os
# 用例路径
import time

case_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 报告存放路径
report_path = os.path.join('/Users/yuchengtao/PycharmProjects/shenghuidai/SHD_automation/panda_baogao')
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
    print(discover)
    return discover

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    # runner.run(all_case())
    curtime = time.strftime ('%Y%m%d%H%M%S', time.localtime ())
    report_paths = report_path + curtime + '.html'
    report_set = open (report_paths, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner (stream = report_set, title = '自动化测试报告', description = '胜辉贷各用例执行情况：')
    runner.run (all_case ())
    report_set.close ()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2018/1/13 17:07
import HTMLTestRunner
from SHD_automation.panda_log.log import *
import unittest
import os
import time

# 用例路径
case_path = os.path.join('../panda_case')

# 报告存放路径
report_path = os.path.join('../panda_baogao/')

def All_case():
    """
    :return: 执行所有以test开头的.py文件
    """
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
    return discover

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    curtime = time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime ())
    report_paths = report_path + curtime + '.html'
    report_set = open (report_paths, 'wb')
    # noinspection LongLine
    baogao_info = '内容包括:一.首页1.首页的投资攻略模块2.新手指引模块3.每日签到模块4.邀请好友模块带完成5.帮助中心二.发现模块1.平台数据2.安全保障3.积分商城4.活动中心三.账户模块1.除【提现，充值】外的所以功能'
    logging.info(f"报告详情：{baogao_info}")
    runner = HTMLTestRunner.HTMLTestRunner (stream = report_set, title = '自动化测试报告', description = baogao_info)
    runner.run (All_case())
    report_set.close ()
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

def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
    return discover

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    curtime = time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime ())
    report_paths = report_path + curtime + '.html'
    report_set = open (report_paths, 'wb')
    # noinspection LongLine
    baogao_info = '内容包括：\n 一.首页\n1.首页的投资攻略模块\n2.新手指引模块\n3.每日签到模块\n4.邀请好友模块带完成\n5.帮助中心\n二.发现模块\n1.平台数据\n2.安全保障\n3.积分商城\n4.活动中心\n三.账户模块\n1.除【提现，充值】外的所以功能'
    logging.info(f"报告详情：{baogao_info}")
    runner = HTMLTestRunner.HTMLTestRunner (stream = report_set, title = '自动化测试报告', description = baogao_info)
    runner.run (all_case ())
    report_set.close ()
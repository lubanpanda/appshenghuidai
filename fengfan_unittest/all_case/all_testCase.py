 # coding:utf-8
import  unittest,requests,HTMLTestRunner,time,os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from fengfan_unittest.feng_test_method.method import *
from appiumtext import webdriver
def allCase():
    #待执行用例的目录
    case_dir=r'../feng_test_case'
    #构造测试集合
    #suite=unittest.TestSuite()
    #获取到一个list集合
    discover = unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)
    #pattern————匹配脚本名称规则，test*.py是匹配所有test开头的所有脚本
    #top_level_dir 这个是顶层目录的名称 ，一般为空就可以了
    # for test_suite in discover:
    #     for test_case in test_suite:
    #         suite.addTests(test_case)
    return  discover
#pathCode = 'C:\\Users\\feng\Desktop\python01\\fengfan_unittest\\feng_test_result\\'
#cuitime=time.strftime('%Y%m%d%H%M%S',time.localtime())
#report_path = pathCode+cuitime+'.html'
#report_set = open(report_path, 'wb')
#runner = HTMLTestRunner.HTMLTestRunner(stream=report_set,title=u'自动化测试报告',description=u'用例执行情况：')
if __name__=="__main__":
    pathCode = 'C:\\Users\\feng\Desktop\python01\\fengfan_unittest\\feng_test_result\\'
    curtime=time.strftime('%Y%m%d%H%M%S',time.localtime())
    report_path = pathCode+curtime+'.html'
    report_set = open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=report_set,title=u'自动化测试报告',description=u'用例执行情况：')
    runner.run(allCase())
    report_set.close()


# coding:utf-8
import  redis
from selenium import webdriver
import time
import random
import  os
from appium.webdriver.common.touch_action import TouchAction #导入Touch Action类   这个是支持手势操作
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlrd
import copy
from  fengfan_unittest import startAPP
from selenium.webdriver.support import *
#from pyocr import pyocr
from PIL import Image
import traceback
import logging
from fengfan_unittest.feng_test_log.feng_test_logmethod import *
from fengfan_unittest.feng_test_conf.feng_test_env.feng_test_config import *




class startMethod(object):

    '''封装ID获取元素'''
    def action_Id(self,id,text):
        if text=='obtain':
            pro = '获取元素：'
            self.logger.info(u'>>>%s%s' % (pro, id))
            return self.driver.find_element_by_id(id)
        else:
            if text=='click':
                pro = '点击控件获取：'
                self.logger.info(u'>>>%s%s' % (pro, id))
                return self.driver.find_element_by_id(id).click()
            else:
                pro = '输入内容为：'
                self.logger.info(u'>>>定位控件%s,%s%s' % (id,pro,text))
                return self.driver.find_element_by_id(id).set_text(text)

    '''方法包装_通过当前页面:classname+text定位控件并完成输入'''
    def dianJi_ClassText_ShuRu(self,driver, className, text, txtUsername):
        allClassNames = driver.find_elements_by_class_name(className)  # 定义所有该className下所有控件为 allclassname
        for allClassName in allClassNames:
            print(allClassName.text)
            if text in allClassName.text:  # 当text的值属于  遍历出来当中的一个text值时，则为我们需要的值
                allClassName.set_text(txtUsername)
                break

    '''封装一个根据clsaa+text的方法点击控件 '''
    def dianJi_classText(self,driver, className, text):
        clickClassName = driver.find_elements_by_class_name(className)
        for clickclassNameOne in clickClassName:
            if text in clickclassNameOne.text:
                clickclassNameOne.click()
                break

    '''封装一个根据class+text的方法获取元素'''
    def huoQu_classText(self,className, text):
        clickClassName = self.driver.find_elements_by_class_name(className)
        for clickclassNameOne in clickClassName:
            if text in clickclassNameOne.text:
                print(text)
                print(clickclassNameOne)
                self.logger.info(text)
                break
            else:
                self.logger.info('sjoj')

    '''封装一个获取className的方法（className唯一）'''
    def huoQu_className(self,className):

        return self.driver.find_element_by_class_name(className)

    '''封装一个滑动当前页面查找元素方法'''
    def scroll_resourceId(self,driver, classNameCode, textCode):
        driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().resourceId("%s")).scrollIntoView(new UiSelector().text("%s"))' % (
            classNameCode, textCode))

    '''封装一个滑动当前页面class+text查看元素方法'''
    def scroll_classText(self, classNameCode, textCode):
        self.driver.find_element_by_android_uiautomator((
                                                        'new UiScrollable(new UiSelector().className("%s")).scrollIntoView(new UiSelector().text("%s"))' % (
                                                        classNameCode, textCode)))
    '''封装退出鹿管家APP方法'''
    def backLogin(self):
        time.sleep(10)
        self.driver.tap([(1, 160)])
        time.sleep(1)
        self.driver.find_element_by_id('com.yce.deerstewardphone:id/btn_me').click()
        self.driver.find_element_by_id('com.yce.deerstewardphone:id/lay_setting').click()
        self.driver.find_element_by_id('com.yce.deerstewardphone:id/lay_logout').click()
        self.driver.find_element_by_id('com.yce.deerstewardphone:id/btn_conform').click()

    '''封装获取toast方法'''
    def find_toast(self,message):
        try:
            WebDriverWait(self,30,0.1).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, message)))
            self.logger.info(message)

        except:
            print(traceback.print_exc())
            self.logger.info("false")
    def loginCode(self,user): #封装登陆方法
        startMethod.action_Id(self,login['账号id'],user)
        startMethod.action_Id(self,login['验证码id'],'click')
        time.sleep(2)
        code=titleMethod.redisCode(self,'192.168.1.171','6379','5','yc_test',user)
        startMethod.action_Id(self,login['密码id'],code)
        startMethod.action_Id(self,login['登录id'],'click')
        self.logger.info('初始化登陆成功')
        self.driver.implicitly_wait(10)

class myMethod(object):

    '''封装一个随机生成电话号码的方法,默认方法首位字母为1，其余十位随机'''
    def randomTel(self):
        i = 1
        listUsername = ['1']
        while i <= 10:
            Usernamecode = str(random.choice(range(10)))
            listUsername.append(Usernamecode)
            i += 1
        return ''.join(listUsername)
    '''等待定位元素'''
    def wait_time(self,resourceid,waitTime=None):
        try:
            if waitTime==None:
                waitTime=10
            WebDriverWait(waitTime).until(lambda driver:driver.find_element_by_id(resourceid))
            self.logger.info(u'>>>检测到{},页面未跳转成功'.format(resourceid))
        except Exception as f:
            print(f)
            self.logger.info(u'>>>未检测到{},页面跳转成功'.format(resourceid))
    '''读取excl表格内容'''

class titleMethod(object):
    '''excelb表格读取'''
    def duQu_Exlce(self,a,b):
        exlce_Name = xlrd.open_workbook(r'C:\Users\feng\Desktop\python01\fengfan_unittest\feng_exlce_case\denglu_excel.xls')  # 打开excel文件格式为xlsx有的是xls
        table = exlce_Name.sheet_by_name(u'登录')
        cell_a1 = table.cell(a,b).value  # a代表行——从零开始   b代表列 从零开始
        return cell_a1
        self.logger.info(u'>>>获取excel表格内容：{}'.format(cell_a1))

    '''复制表格写入excel'''
    def xieRu_Exlce(a, b, sheet_name, value, filePath):  # excel 写入
        excel_Name = xlrd.open_workbook('C:/Users/feng/Desktop/excel_case/denglu_excel.xls',
                                        formatting_info=True)  # 打开excel表格
        table = excel_Name.sheet_by_name(sheet_name)  # 选择sheet页
        exlce_NameCode = copy(excel_Name)  # 复制一个excel
        tableCode = exlce_NameCode.get_sheet(0)  # 找到复制后的 sheet页 ——备注：excel_Name.sheet_by_name无法write！get——sheet可以write
        tableCode.write(a, b, value)  # 写入
        exlce_NameCode.save(filePath)  # 保存新的excel


    '''封装一个传入服务器地址host，port端口号,db第几个表,redisPassword密码'''
    def redisCode(self,host,port,db,redisPassword,Usernamecode):
        pool=redis.ConnectionPool(host=host,port=port,db=db,password=redisPassword)
        r = redis.StrictRedis(connection_pool=pool)
        a=Usernamecode
        b='register_user_code_'
        return r.get(b+a).decode('utf-8')
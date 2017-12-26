import unittest,time
from fengfan_unittest.startAPP import *
from fengfan_unittest.feng_test_method.method import *
import  unittest,requests,HTMLTestRunner
from fengfan_unittest.feng_test_conf.feng_test_env.feng_test_config import *

a = time.strftime('%d%H%M%S', time.localtime())
newUser = '135' + a
oldUser = '13590283182'
class  Blood(unittest.TestCase,object):
    def setUp(self):
        start_App.__init__(self)
        start_App.setUp(self)

    def tearDown(self):
        start_App.tearDown(self)


    def test_blood_01(self):
        '''验证新用户登录是否获取到完善资料自动创建家庭群'''
        startMethod.loginCode(self,newUser)
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath(newUserLogin['立即使用xpath']))
            WebDriverWait(self,10).until(lambda driver: startMethod.action_Id(self,newUserLogin['名医视讯id'],'obtain'))

            self.logger.info('>>>新用户登录之后，获取到"立即使用并完善信息"和"名医视讯"')
        except:
            self.assertEqual(1,2,msg=u'未获取到元素，新用户登录未进去完善信息界面！')

    def test_blood_02(self):
        '''验证新用户创建家庭群'''
        self.driver.find_element_by_xpath(newUserLogin['立即使用xpath']).click()
        time.sleep(5)
        names='测试'+time.strftime('%H%M%S',time.localtime())
        startMethod.action_Id(self,perfect['家庭群名id'],names)
        startMethod.action_Id(self,perfect['用户名id'],names)
        startMethod.action_Id(self,perfect['男id'],'click')
        startMethod.action_Id(self,perfect['身高id'],'175')
        startMethod.action_Id(self,perfect['体重id'],'65')
        startMethod.action_Id(self,perfect['出生年月日id'],'click')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("android:id/numberpicker_input").text(u"2017")')
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("android:id/numberpicker_input").text(u"10")')
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("android:id/numberpicker_input").text(u"11")')
        startMethod.action_Id(self,'android:id/button1','click')




if __name__=='__main__':
    unittest.main()



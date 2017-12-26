# coding:utf-8
from fengfan_unittest.startAPP import *
from fengfan_unittest.feng_test_method.method import *
import  unittest,requests,HTMLTestRunner
from fengfan_unittest.feng_test_conf.feng_test_env.feng_test_config import *
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Test_login(unittest.TestCase,object):
    def setUp(self):
        start_App.__init__(self)
        start_App.setUp(self)
    def tearDown(self):
        start_App.tearDown(self)
    def test01(self):
        '''账号未空点击获取验证码'''
        startMethod.action_Id(self,login['验证码id'],'click')
        try:
            a=startMethod.action_Id(self,login['验证码文字id'],'obtain').text

            self.logger.info('账号为空点击获取验证码，无响应符合预期')
        except:
            self.assertEqual(a, u'获取验证码', msg='未输入手机号码可以点击验证码')

    def test02(self):
        '''账号为空点击登录'''
        startMethod.action_Id(self,login['登录id'],'click')
        try:
            WebDriverWait(self,10).until(lambda driver:startMethod.action_Id(self,login['登录id'],'obtain'))
            self.logger.info('获取到登录id，未登录成功，符合预期')
        except:
            self.assertEqual(1,2,msg='直接点击登录，可以登录成功')

    def test03(self):
        '''输入小于11位手机号码，点击获取验证码'''
        startMethod.action_Id(self,login['账号id'],titleMethod.duQu_Exlce(self,2,2))
        self.logger.info('获取输入手机账号：%s'%titleMethod.duQu_Exlce(self,2,2))
        #点击获取验证码
        startMethod.action_Id(self,login['验证码id'],'click')

        a=startMethod.action_Id(self,login['验证码文字id'],'obtain').text
        self.logger.info('获取输入小于11位手机号码之后，点击获取验证码后的验证码文字id：%s'%a)
        self.assertEqual(a,'获取验证码',msg='输入小于11位手机验证码，可以点击获取获取验证码成功，不符合预期')

    def test04(self):
        '''输入小于11位手机号码，点击获取验证码后点击登录'''
        startMethod.action_Id(self,login['账号id'],titleMethod.duQu_Exlce(self,2,2))
        self.logger.info('获取输入手机账号：%s'%titleMethod.duQu_Exlce(self,2,2))
        startMethod.action_Id(self, login['登录id'], 'click')  # 点击登录
        try:
            WebDriverWait(self,10).until(lambda driver:startMethod.action_Id(self,login['登录id'],'obtain'))
            self.logger.info('直接输入小于十一位验证码点击登录之后，任然可以获取到登录id，符合预期')
        except:
            self.assertEqueal(1,2,msg='输入小于11位手机号，直接点击登录，未检测到登录id，不符合预期')

    def test05(self):
        '''验证账号小于11位，输入错误验证码'''
        startMethod.action_Id(self,login['账号id'],titleMethod.duQu_Exlce(self,2,2))
        startMethod.action_Id(self,login['密码id'],titleMethod.duQu_Exlce(self,3,3))
        startMethod.action_Id(self,login['登录id'],'click')
        try:
            WebDriverWait(self,10).until(lambda driver:startMethod.action_Id(self,login['登录id'],'obtain'))
            self.logger.info('输入低于11位手机号码，错误验证码，登录不成功，符合预期')
        except:
            self.assertEqual(1,2,msg='输入低于11位手机验证码，错误验证码，登录成功，不符合预期')

    def test06(self):
        '''验证账号大于11位,输入正确验证码'''
        startMethod.action_Id(self, login['账号id'], titleMethod.duQu_Exlce(self,3,2))
        #获取前11位手机号码!
        text=startMethod.action_Id(self,login['账号id'],'obtain').text
        self.logger.info('获取验证码手机号码为：%s'%text)
        #点击获取验证码
        startMethod.action_Id(self,login['验证码id'],'click')
        time.sleep(2)
        code=titleMethod.redisCode(self,'192.168.1.171','6379','5','yc_test',text)
        self.logger.info('获取验证码为%s'%code)
        startMethod.action_Id(self,login['密码id'],code)
        self.logger.info('输入验证码%s'%code)
        #点击登录
        startMethod.action_Id(self,login['登录id'],'click')
        time.sleep(3)
        try:
            WebDriverWait(self,10).until(lambda driver:startMethod.action_Id(self,login['登录id'],'obtain'))
            self.assertEqual(1,2, msg='验证账号大于11位,输入正确验证码，未登录成功，不符合预期')
        except:

            self.logger.info('输入超过11位手机号码正确的验证码点击登录——登录成功，符合预期')
            startMethod.backLogin(self)

    def test07(self):
        '''验证账号大于11位，输入错误验证码'''
        startMethod.action_Id(self, login['账号id'], titleMethod.duQu_Exlce(self, 3, 2))
        startMethod.action_Id(self,login['账号id'],titleMethod.duQu_Exlce(self,3,3))
        startMethod.action_Id(self,login['登录id'],'click')
        try:
            startMethod.action_Id(self,login['登录id'],'obtain')
            self.logger.info('输入大于11位手机号码，输入错误验证码，登陆不成功，符合预期')
        except:
            self.assertEqual(1,2,msg='输入大于11位手机号码，输入错误验证码，可以登陆成功，不符合预期')
    def test08(self):
        '''输入大于11位手机号码，不输入验证码点击登录'''
        startMethod.action_Id(self, login['账号id'], titleMethod.duQu_Exlce(self, 4, 2))

        startMethod.action_Id(self, login['登录id'], 'click')
        try:
            startMethod.action_Id(self,login['登录id'],'obtain')
            self.logger.info('输入大于11位手机号码，不输入验证码，登陆不成功，符合预期')
        except:
            self.assertEqual(1,2,msg='输入大于11位手机号码，不输入验证码，可以登陆成功，不符合预期')
    def test09(self):
        '''验证码重新获取验证码'''
        startMethod.action_Id(self,login['账号id'],titleMethod.duQu_Exlce(self,5,2))
        # 获取前11位手机号码
        text = startMethod.action_Id(self, login['账号id'], 'obtain').text
        #点击获取验证码
        startMethod.action_Id(self,login['验证码id'],'click')
        time.sleep(2)
        #获取验证码的值
        redis01=titleMethod.redisCode(self,'192.168.1.171','6379','5','yc_test',text)
        time.sleep(2)
        #获取验证码文字
        a=startMethod.action_Id(self,login['验证码文字id'],'obtain').text
        self.logger.info('获取验证码文字为：%s'%a)
        self.assertEqual(a,u'重新获取',msg='点击获取验证码之后没有倒计时一分钟之内重新获取验证码，不符合预期')
        time.sleep(61)
        self.logger.info('等待一分钟之后，从新获取验证码——————————')
        startMethod.action_Id(self, login['验证码id'], 'click')
        self.logger.info('重新点击获取验证码——')
        time.sleep(2)
        a = startMethod.action_Id(self, login['验证码文字id'], 'obtain').text
        redis02 = titleMethod.redisCode(self, '192.168.1.171', '6379', '5', 'yc_test',text)
        self.assertEqual(a, u'重新获取', msg='点击获取验证码之后没有倒计时一分钟之内重新获取验证码，不符合预期')
        self.assertNotEqual(redis01,redis02,msg='同一个号码连续获取验证码，验证码无变化！') #判断两次验证码是否相等
        self.logger.info('第一次获取验证码为：%s，第二次获取验证码为：%s'%(redis01,redis02))


if __name__=='__main__':
    unittest.main()
    # suite=unittest.TestSuite()
    # suite.addTest(Test_login('test_1_case'))
    # suite.addTest(Test_login('test_2_case'))
    # pathCode = 'C:\\Users\\feng\Desktop\python01\\fengfan_unittest\\feng_test_result\\'
    # curtime=time.strftime('%Y%m%d%H%M%S',time.localtime())
    # report_path = pathCode+curtime+'.html'
    # report_set = open(report_path, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=report_set,title=u'自动化测试报告',description=u'用例执行情况：')
    # runner.run(suite)
    # report_set.close()




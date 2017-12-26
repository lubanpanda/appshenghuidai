from  appiumtext import webdriver
from fengfan_unittest.feng_test_conf.feng_test_env.feng_test_config import config
import logging
from fengfan_unittest.feng_test_method.method import *

class start_App(object):
    def __init__(self):
        Log()
        self.logger = logging.getLogger()

    def setUp(self):

        desired_caps = {}
        desired_caps['platformName'] = config['platformName']
        desired_caps['plarformVersion'] = config['plarformVersion']
        desired_caps['deviceName'] = config['deviceName']
        desired_caps['app'] = config['app']
        desired_caps['appPackage'] = config['appPackage']
        desired_caps['appActivity']=config['appActivity']
        desired_caps['noReset'] = config['noReset']
        desired_caps['unicodekeyboard'] = config['unicodekeyboard']
        desired_caps['resetKeyboart'] = config['resetKeyboart']
        desired_caps['automationName'] = config['automationName']
        desired_caps['newCommandTimeout'] =config['newCommandTimeout']
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
    def tearDown(self):
        self.driver.quit()

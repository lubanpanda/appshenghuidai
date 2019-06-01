#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  84305510@qq.com
import os
import random
import sys
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from SHD_automation.device_info.device import *
from SHD_automation.panda_log.log import *


# noinspection PyUnresolvedReferences,PyPep8Naming
class My_method(object):
    def My_id(self, yuansu_id, text, shuxing=None, sleep_time=0):
        """
        :param yuansu_id: 元素ID
        :param text: 操作对象
        :param shuxing: 获取text内容或其他控件信息
        :param sleep_time: 睡眠时间
        :return: 获取ID元素或者其他熟悉操作
        """
        if text == '获取元素':
            pro = '获取元素>>>：'
            logging.info(u'%s%s' % (pro, yuansu_id))
            return self.driver.find_element_by_id(yuansu_id), time.sleep(sleep_time)
        else:
            if text == 'click':
                pro = '点击控件获取>>>'
                logging.info(u'%s%s' % (pro, yuansu_id))
                return self.driver.find_element_by_id(yuansu_id).click(), time.sleep(sleep_time)
            elif text == '获取内容':
                pro = '获取控件里的text内容>>>'
                logging.info('%s%s' % (pro, yuansu_id))
                return self.driver.find_element_by_id(yuansu_id).text, time.sleep(sleep_time)
            elif text == '属性':
                pro = '获取控件id的其他属性>>>：'
                logging.info(u'%s%s' % (pro, yuansu_id))
                return self.driver.find_element_by_id(yuansu_id).get_attribute(shuxing), time.sleep(sleep_time)
            else:
                pro = '输入内容为>>>：'
                logging.info(u'定位控件%s,%s%s' % (yuansu_id, pro, text))
                return self.driver.find_element_by_id(yuansu_id).clear(), self.driver.find_element_by_id(
                    yuansu_id).send_keys(str(text)), time.sleep(sleep_time)

    def my_accessibility_id_dianji(self, accessibility_id, sleep_time=0):
        """
        :param accessibility_id:
        :param sleep_time:
        :return: 通过accessibility id查找元素
        """
        proo = 'accessibility id查找元素>>>'
        logging.info(f'{proo}{accessibility_id}')
        return self.device.find_element_by_accessibility_id(accessibility_id).click(), time.sleep(sleep_time)

    def my_class_name_shuru(self, className, text, txtUsername):
        """
        :param className: 元素
        :param text: text内容
        :param txtUsername: 输入内容
        :return: 方法包装_通过当前页面:classname+text定位控件并完成输入
        """
        allClassNames = self.driver.find_elements_by_class_name(className)  # 定义所有该className下所有控件为 allclassname
        for allClassName in allClassNames:
            print(allClassName.text)
            if text in allClassName.text:  # 当text的值属于  遍历出来当中的一个text值时，则为我们需要的值
                allClassName.set_text(txtUsername)
                break

    def my_class_name_id_dianji(self, classname, list_id, text, shuxing=None, sleep_time=1):
        """
        :param classname: class名字
        :param list_id: 索引的数值
        :param text: 自己输入的操作方法
        :param shuxing: 查看text或其他参数可用
        :param sleep_time: 默认的睡眠时间
        :return: 封装了获取元素，点击操作，输入内容，获取控件单位方法
        """
        if text == '获取元素':
            proo = '获取classname元素>>>：'
            logging.info(u'%s%s' % (proo, classname))
            return self.driver.find_elements_by_class_name(classname)
        else:
            if text == 'click':
                pro = '点击控件classname>>>：'
                logging.info(u'%s%s索引数字：%s' % (pro, classname, list_id))
                return self.driver.find_elements_by_class_name(classname)[list_id].click(), time.sleep(sleep_time)
            elif text == '属性':
                proa = '获取控件classname的其他属性>>>：'
                logging.info(u'%s%s索引数字：%s' % (proa, classname, list_id))
                return self.driver.find_elements_by_class_name(classname)[list_id].get_attribute(shuxing), time.sleep(
                    sleep_time)
            elif text == 'text':
                proa = '获取控件text属性>>>：'
                logging.info(u'%s%s索引数字：%s' % (proa, classname, list_id))
                return self.driver.find_elements_by_class_name(classname)[list_id].text, time.sleep(sleep_time)
            else:
                pros = '输入内容为>>>：'
                logging.info(u'定位控件%s,%s%s' % (classname, pros, text))
                return self.driver.find_elements_by_class_name(classname)[list_id].set_text(text)

    def my_class_name_shuru_dianji(self, className, text):
        """
        :param className: class元素
        :param text: text控件名称
        :return: 封装一个根据clsaa+text的方法点击控件
        """
        clickClassName = self.driver.find_elements_by_class_name(className)
        for clickclassNameOne in clickClassName:
            if text in clickclassNameOne.text:
                clickclassNameOne.click()
                break

    def my_classText_huoqu(self, className, text):
        """
        :param className: 名字
        :param text: text想找的内容
        :return: 封装一个根据class+text的方法获取元素
        """
        clickClassName = self.driver.find_elements_by_class_name(className)
        for clickclassNameOne in clickClassName:
            if text in clickclassNameOne.text:
                print(text)
                print(clickclassNameOne)
                logging.info(text)
                break
            else:
                logging.info(f'没找到{text}')

    def huoQu_className(self, className):
        """
        :param className: class元素名称
        :return: 封装一个获取className的方法（className唯一）
        """

        return self.driver.find_element_by_class_name(className)

    def scroll_resourceId(self, idcode, textCode):
        """
        :param idcode: id名字
        :param textCode: 要寻找的名字
        :return: 封装一个滑动当前页面查找元素方法
        """
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().resourceId("%s")).scrollIntoView(new UiSelector().text("%s"))' % (
                idcode, textCode))

    def scroll_classText(self, classNameCode, textCode):
        """
        :param classNameCode: class名字
        :param textCode: 要寻找的名字
        :return: 封装一个滑动当前页面class+text查看元素方法
        """
        # noinspection LongLine
        self.driver.find_element_by_android_uiautomator((
                'new UiScrollable(new UiSelector().className("%s")).scrollIntoView(new UiSelector().text("%s"))' % (
            classNameCode, textCode)))

    def back_Login(self):
        """
        :return: 封装退出APP方法
        """
        time.sleep(10)
        self.driver.find_element_by_id(module_info['账户']).click()
        os.popen('adb shell input swipe 50 1000 50 0 100')
        self.driver.find_element_by_id(account['更多']).click()
        self.driver.find_element_by_id(module_info['退出']).click()
        self.driver.find_element_by_id('com.yourenkeji.shenghuidai:id/positiveButton').click()

    def find_toast(self, message):
        """
        :param message: 吐司的信息内容
        :return: 封装获取toast方法
        """
        toast_Code = ('xpath', './/*[contains(@text,"%s")]' % message)
        t = (WebDriverWait(self.driver, 5, 0.1).until(EC.presence_of_element_located(toast_Code))).text
        if message == t:
            logging.info(f'吐司正确,内容为>>>:{message}')
            return message
        else:
            logging.info(f'吐司错误，正确的吐司是toast :{t}')
            return t

    def loginCode(self, username, password):
        """
        :param username: 账户
        :param password: 密码
        :return: 封装登陆方法
        """
        My_method.My_id(self, module_info['账户'], 'click')
        My_method.My_id(self, zhuce['登录'], 'click')
        My_method.My_id(self, zhuce['账号'], username)
        My_method.My_id(self, 'com.yourenkeji.shenghuidai:id/zhu_bt', 'click')
        My_method.My_id(self, zhuce['密码'], password)
        My_method.My_id(self, 'com.yourenkeji.shenghuidai:id/denglu_bt_a', 'click')
        My_method.My_id(self, zhuce['跳过'], 'click')
        logging.info('初始化登陆成功')

    def yiwai_login(self, uesrnames="***********", passwords=123456):
        """
        :param uesrnames: 账户
        :param passwords: 密码
        :return: token失效时调用这个函数
        """
        My_method.my_class_name_id_dianji(self, 'android.widget.Button', 0, 'click')
        My_method.My_id(self, zhuce['账号'], uesrnames)
        My_method.My_id(self, 'com.yourenkeji.shenghuidai:id/zhu_bt', 'click')
        My_method.My_id(self, zhuce['密码'], passwords)
        My_method.My_id(self, 'com.yourenkeji.shenghuidai:id/denglu_bt_a', 'click')
        My_method.My_id(self, zhuce['跳过'], 'click')
        logging.info('重新登录成功')

    def login_exit(self):
        """
        :return: 封装一个退出方法
        """
        My_method.My_id(self, module_info['账户'], 'click')
        My_method.My_id(self, account['更多'], 'click')
        My_method.My_id(self, module_info['退出'], 'click')
        My_method.My_id(self, 'com.yourenkeji.shenghuidai:id/positiveButton', 'click')
        logging.info('退出账号成功')

    def login_turn_or_flase(self, panduan_login, name, password):
        """
        :param panduan_login: 提供一个执行条件
        :param name: 账号名字
        :param password: 账号密码
        :return: 判断是否登录
        """
        My_method.My_id(self, module_info['账户'], 'click')
        if panduan_login == '判断登录':
            self.driver.implicitly_wait(3)
            try:

                a = My_method.My_id(self, zhuce['登录'], '获取元素')
                if a:
                    My_method.loginCode(self, name, password)
            except Exception:
                logging.info('已经登录了哦')

    def app_back(self, cishu=1):
        """
        :param cishu: 返回的次数，默认为1
        :return: 封装一个多次返回的方法
        """
        for i in range(cishu):
            self.driver.back()
        pro = '一共返回了:'
        logging.info(f'{pro}{cishu}次')


# noinspection PyUnresolvedReferences
class myMethod(object):
    def randomTel(self):
        """
        :return: 封装一个随机生成电话号码的方法,默认方法首位字母为185，其余八位随机
        """
        i = 1
        listUsername = ['185']
        while i <= 8:
            Usernamecode = str(random.choice(range(10)))
            listUsername.append(Usernamecode)
            i += 1
        logging.info(f'手机号为:{listUsername}')
        return ''.join(listUsername)

    def randomID(self):
        """

        :return:身份证号码
        """
        i = 1
        list_username_i_d = ['2321']
        while i <= 14:
            Usernamecode = str(random.choice(range(10)))
            list_username_i_d.append(Usernamecode)
            i += 1
        logging.info(f'身份证号:{list_username_i_d}')
        return ''.join(list_username_i_d)

    def bankId(self):
        """

        :return: 银行卡号 6212260200094536345
        """
        i = 1
        kahao_id = ['6212']
        while i <= 15:
            Usernamecode = str(random.choice(range(10)))
            kahao_id.append(Usernamecode)
            i += 1
        logging.info(f'身份证号:{kahao_id}')
        return ''.join(kahao_id)

    def wait_time(self, resourceid, waitTime=None):
        """
        :param resourceid: 需要查找的ID
        :param waitTime: 等待时间
        :return: 等待定位元素
        """
        try:
            if waitTime == None:
                waitTime = 10
            WebDriverWait(waitTime).until(lambda driver: self.driver.find_element_by_id(resourceid))
            logging.info(u'>>>检测到{},页面未跳转成功'.format(resourceid))
        except Exception as f:
            print(f)
            logging.info(u'>>>未检测到{},页面跳转成功'.format(resourceid))


# noinspection PyUnresolvedReferences
class Pingmu_unlock_the_screen(object):
    def pingmu_jiesuo(self):
        """
        :return: 手机本身的解锁
        """
        b = os.popen('adb shell dumpsys window policy|grep mScreenOnFully')
        a = b.read().strip()
        deng = a[-5:]
        logging.info(f'判断是否锁屏{deng}')
        if deng == str('false'):
            logging.info('屏幕是灭的,等待解锁')
            os.popen('adb shell input keyevent 26')
            time.sleep(1)
            os.popen('adb shell input swipe 50 1000 50 0 100')
        else:
            os.popen('adb shell input swipe 50 1000 50 0 100')
            logging.info('不是锁屏状态,可直接执行项目哦')

    def App_jiesuo(self):
        """
        :return: 解锁app内部的滑动解锁
        """
        time.sleep(6)
        list_pwd = self.driver.find_elements_by_class_name("android.widget.ImageView")
        logging.info(list_pwd)
        try:
            TouchAction(self.driver).press(list_pwd[0]).move_to(list_pwd[3]).move_to(list_pwd[6]).wait(100).move_to(
                list_pwd[7]).wait(100).move_to(list_pwd[8]).release().perform()
            time.sleep(4)
            logging.info('解锁成功')
            return True
        except Exception:
            logging.info('解锁失败')


# noinspection PyUnresolvedReferences
class Huadong(object):
    def Getsize(self):
        """
        :return:获取手机的分辨率
        """
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        logging.info(x, y)
        return x, y

    def huadong(self, fangxiang, huadong_time, sleep_time=1):
        """
        :param fangxiang: 滑动的方向
        :param huadong_time: 滑动时间
        :param sleep_time: 睡眠时间
        :return: 滑动的方法
        """
        screen_size = Huadong.Getsize(self)
        if fangxiang == '上':
            x1 = int(screen_size[0] * 0.5)
            y1 = int(screen_size[1] * 0.75)
            y2 = int(screen_size[1] * 0.25)
            zuobiao = '手机坐标为>>>：'
            logging.info('%s,x=(%s%s),y=(%s%s),向%s滑动了%s毫秒' % (zuobiao, x1, y1, x1, y2, fangxiang, huadong_time))
            return self.driver.swipe(x1, y1, x1, y2, huadong_time), time.sleep(sleep_time)
        elif fangxiang == '下':
            x2 = int(screen_size[0] * 0.5)
            y3 = int(screen_size[1] * 0.25)
            y4 = int(screen_size[1] * 0.75)
            zuobiao = '手机坐标为>>>：'
            logging.info('%s,x=(%s%s),y=(%s%s),向%s滑动了%s毫秒' % (zuobiao, x2, y3, x2, y4, fangxiang, huadong_time))
            return self.driver.swipe(x2, y3, x2, y4, huadong_time), time.sleep(sleep_time)
        elif fangxiang == '左':
            x3 = int(screen_size[0] * 0.75)
            y5 = int(screen_size[1] * 0.5)
            x4 = int(screen_size[0] * 0.05)
            zuobiao = '手机坐标为>>>：'
            logging.info('%s,x=(%s%s),y=(%s%s),向%s滑动了%s毫秒' % (zuobiao, x3, y5, x4, y5, fangxiang, huadong_time))
            return self.driver.swipe(x3, y5, x4, y5, huadong_time), time.sleep(sleep_time)
        elif fangxiang == '右':
            x5 = int(screen_size[0] * 0.05)
            y6 = int(screen_size[1] * 0.5)
            x6 = int(screen_size[0] * 0.75)
            zuobiao = '手机坐标为>>>：'
            logging.info('%s,x=(%s%s),y=(%s%s),向%s滑动了%s毫秒' % (zuobiao, x5, y6, x6, y6, fangxiang, huadong_time))
            return self.driver.swipe(x5, y6, x6, y6, huadong_time), time.sleep(sleep_time)
        else:
            logging.info("写错了哦，无法滑动")


# noinspection PyUnresolvedReferences
class jietu(object):
    def jietu_picture(self, name):
        """
        :param name: 相片的名字
        :return: 截图功能
        """
        self.driver.implicitly_wait(1)
        picture_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.driver.save_screenshot((HTMLbaogao['图片地址'] + picture_time + "%s.png") % name)


class daojishi(object):
    def daojishi_seconds(self, seconds):
        """
        :param seconds: 倒计时的秒数
        :return: 倒计时功能来阻止程序运行
        """
        count = 0
        while count < seconds:
            ncount = seconds - count
            sys.stdout.write("\r%d " % ncount)
            sys.stdout.flush()
            time.sleep(1)
            count += 1

# # -*- coding:utf-8 -*-
import os
import time
import Uninstall
import installApks

def eMail():
    """
    1.需要登录QQ邮箱，然后去获取新邮件
    2.获取新邮件成功后，判断附件是否带有.apk文件
    3.如果没有继续监听，有的话把文件下载到本地
    4.判断手机是否有此apk的包名，有则先执行Uninstall卸载命令，然后执行adb install 命令安装
    5.提示成功/失败的信息
    6.这个程序，需要后台常驻，需要开机自启动。
    7.还需要判断，手机有没有连接上，
    8.读取未读邮件
    9.学习的网址：http://www.liaoxuefeng.com/wiki/d8147196000
    :return:
    """
    #qqemail.qqemail(username, password)
    #downapk.download_apk(url='https://www.pgyer.com/apiv1/app/install?aId=351e4777abeff98c146ef004bf13c4f0&_api_key'
       #                      '=e91274ea7400de5d8350df83e56a5e80')
    adb_device = os.popen("adb shell pm list packages -3").readlines()
    if adb_device:
        print("手机连接成功，正在为你卸载软件,请等待10S")
        if Uninstall.uninstall() is None:
            pass
        else:
            Uninstall.uninstall()
        time.sleep(10)
        print("---------卸载完成------------")
        print("---------软件安装中----------")
        installApks.installAllApks(dir='./')
        installApks.installApk(file)
        print('install ' + file + ' success')
    else:
        print("手机连接失败,请检查数据线是否插好")


if __name__ == '__main__':
    eMail()

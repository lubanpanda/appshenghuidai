#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2018/2/15 23:05
import itchat
import time

def send_weixin(message):
	"""
	:param message: 发送消息的内容
	:return:
	"""
	itchat.search_friends()
	users = itchat.search_friends(name='夏天')   # 使用备注名来查找实际用户名
	userName = users[0]['UserName']
	print(f'名字：{userName}')
	i=1
	while True:
		itchat.send(msg =message,toUserName = userName)
		i += 1
		print(i)
		time.sleep(0.2)
		continue


#微信自动回复
@itchat.msg_register('Text')
def text_reply(msg):
    if not msg['FromUserName'] == myUserName:
        itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
                        (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
                         msg['User']['NickName'],
                         msg['Text']), 'filehelper')

        return '[自动回复]您好，我现在有事不在，一会再和您联系。\n已经收到您的的信息：%s\n' % (msg['Text'])

if __name__ == '__main__':
    itchat.auto_login(hotReload = True)
    send_weixin("无聊")
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    # itchat.run()
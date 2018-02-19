#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2018/2/19 14:29
import itchat
import time,re
from itchat.content import *
import threading

#自动回复消息
@itchat.msg_register('Text')
def text_reply(self,msg):
    if not msg['FromUserName'] == self.myUserName:
        itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
                        (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
                         msg['User']['NickName'],
                         msg['Text']), 'filehelper')

        return '[自动回复]您好，我现在有事不在，一会再和您联系。\n我已经收到您的的信息：%s\n' % (msg['Text'])

#接受好友消息
@itchat.msg_register ([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO],
                      isFriendChat = True, isGroupChat = True, isMpChat = True)
def personal_msg (msg):
	msg_time_rec=time.strftime ("%Y-%m-%d %H:%M:%S", time.localtime ())
	msg_from = itchat.search_friends (userName = msg ['FromUserName']) ['NickName']
	if msg ['Type'] == 'Text' or msg ['Type'] == "Friends":
		print(msg_time_rec + "  " + msg_from + ' send a ' + msg ['Type'] + ' : ' + msg ['Text'])
	elif msg ['Type'] == 'Map':
		x, y, location = re.search ("<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*",
		                            msg ['OriContent']).group (1, 2, 3)
		print(msg_time_rec + "  " + msg_from + ' send a ' + msg ['Type'] + ' : ' + msg ['Text'])
		print('The detail location is : ' + u"纬度->" + x.__str__ () + u" 经度->" + y.__str__ ())
	elif msg ['Type'] == 'Card':
		print(msg_time_rec + "  " + msg_from + ' send a ' + msg ['Type'] + ' : ' + msg ['RecommendInfo'] [
			'NickName'] + '的名片')
	elif msg ['Type'] == 'Sharing':
		print(msg_time_rec + "  " + msg_from + ' send a ' + msg ['Type'] + ' : ' + msg ['Text'])
		print('The Url is: ' + msg ['Url'])
	elif msg ['Type'] == "Attachment" or msg ['Type'] == "Video" or msg ['Type'] == 'Picture' or msg [
		'Type'] == 'Recording':
		print(msg_time_rec + "  " + msg_from + ' send a ' + msg ['Type'])

if __name__ == '__main__':
	itchat.auto_login (hotReload = True)
	itchat.run()
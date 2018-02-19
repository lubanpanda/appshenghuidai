#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2018/2/19 14:44


import itchat
import time,re
from itchat.content import *

# 接收群聊天信息
@itchat.msg_register ([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO],
                      isFriendChat = False, isGroupChat = True, isMpChat = False)
def chatroom_msg (msg):
	msg_time_rec = time.strftime ("%Y-%m-%d %H:%M:%S", time.localtime ())
	msg_from = itchat.search_chatrooms (userName = msg ['FromUserName']) ['NickName'] + '  ' + msg [
		'ActualNickName']
	if msg ['Type'] == 'Text':
		print(msg_time_rec + "  " + msg_from + ' send a ' + msg ['Type'] + ' : ' + msg ['Text'])
	elif msg ['Type'] == 'Map':
		x, y, location = re.search ("<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*",
		                            msg ['OriContent']).group (1, 2, 3)
		print(msg_time_rec + "  " + msg_from + ' send a ' + msg ['Type'] + ' : ' + msg ['Text'])
		print('The detail location is : ' + u"纬度->" + x.__str__ () + u" 经度->" + y.__str__ ())
	elif msg ['Type'] == 'Card':
		print(msg_time_rec + "  " + msg_from + ' send a ' + msg ['Type'] + ' : ' + msg ['RecommendInfo'] [
			'NickName'] + u'的名片')
	elif msg ['Type'] == 'Sharing':
		print(msg_time_rec + "  " + msg_from + ' send a ' + msg ['Type'] + ' : ' + msg ['Text'])
		print('The Url is: ' + msg ['Url'])
	elif msg ['Type'] == "Attachment" or msg ['Type'] == "Video" or msg ['Type'] == 'Picture' or msg [
			'Type'] == 'Recording':
		print(msg_time_rec + "  " + msg_from + ' send a ' + msg ['Type'])
if __name__ == '__main__':
	itchat.auto_login (hotReload = True)
	itchat.run()
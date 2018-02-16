#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2018/2/15 14:23
import itchat
import time
import re
from itchat.content import *
import xlwt

class weixin(object):
	"""
	微信信息数据
	1.可以分析好友里的数据信息
	2.可以发送微信消息
	3.可以自动回复微信消息
	4.把自己的信息存储到一个excel表格里
	"""
	def __init__(self):
		itchat.auto_login (hotReload = True)
		self.friends = itchat.get_friends (update = True) [0:]
		self.myUserName=itchat.get_friends(update=True)[0]["UserName"]
		self.friedd_data=[]
		self.book = xlwt.Workbook (encoding = 'utf-8', style_compression = 0)#style_compression是否进行文件压缩，0代表否
		self.sheet = self.book.add_sheet ('微信详细信息', cell_overwrite_ok = True)

#获取微信所有的信息
	def weixin_info(self):
		for friend in self.friends[1:]:
			f_d={
				'uuid':friend['UserName'],#账号
				'niceName':friend ['NickName'],#网民
				'remarkName' : friend ['RemarkName'],#备注名
				'city' : friend ['City'],#地点
				'sex' : friend ['Sex'],#性别1为男
				'province' : friend ['Province'],#省份
				'signature' : friend ['Signature']#签名
			}
			self.friedd_data.append(f_d)
		print(self.friedd_data)
		feiend_number=len(self.friedd_data)
		print(f'一共有{feiend_number}位好友')
		boy=0
		girl=0

		for i in range(feiend_number):
			beizhu=self.friedd_data[i]['remarkName']
			id=self.friedd_data[i]['uuid']
			Sex=self.friedd_data[i]['sex']
			if self.friedd_data[i]['sex']==1:
				xingbie='男'
			else:
				xingbie='女'
			if not beizhu:
				self.sheet.write(i+1,0,self.friedd_data[i]['niceName'])
				# print(self.friedd_data[i]['niceName']+',性别：'+xingbie+',uuid='+self.friedd_data[i]['uuid'])#网名
				if xingbie=='男':
					boy += 1
				else:
					girl+=1
			else:
				self.sheet.write (i+1,0, beizhu)
				print(beizhu+',性别:'+xingbie+',uuid='+id)
				if Sex==1:
					boy+=1
				else:
					girl+=1

			shuxing_info=[self.friedd_data[i]['niceName'],xingbie,self.friedd_data[i]['uuid'],self.friedd_data[i]['city'],self.friedd_data[i]['signature'],self.friedd_data[i]['province']]
			for a in range(6):
				self.sheet.write(i+1,1+a,shuxing_info[a])
		head = ['备注', '网名', '性别', '微信ID', '城市', '个性签名', '省份']
		for b in range (7):
			self.sheet.write (0, b, head [b])

		self.book.save ('../self_CX/微信个人信息.xls')
		print(f'男孩子有{boy}个，女孩子有{girl}个')
		if boy>girl:
			print('你的微信怎么全是男孩子哦，要添加点异性朋友哦')
		elif boy-girl==0:
			print('男女朋友刚刚好，very good')
		else:
			print('额。。。。。女同志有点多哦')

#发送消息
	def send_weixin(self,name,message):
		"""
		:param message: 发送消息的内容
		:return:
		"""
		itchat.search_friends ()
		users = itchat.search_friends (name = name)  # 使用备注名来查找实际用户名
		userName = users [0] ['UserName']
		print(f'名字：{userName}')
		i=1
		while True:
			itchat.send(msg =message,toUserName = userName)
			i += 1
			print(i)
			time.sleep(0.2)
			continue


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
	msg_time_rec = time.strftime ("%Y-%m-%d %H:%M:%S", time.localtime ())
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

# 接收群聊天信息，如果不需要可以不运行
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
	a=weixin()
	a.weixin_info()
	# a.chatroom_msg()
	# itchat.auto_login (hotReload = True)
	# itchat.run ()
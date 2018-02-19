#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2018/2/19 13:20

import itchat
import time
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
		self.book = xlwt.Workbook (encoding = 'utf-8', style_compression = 0)   #style_compression是否进行文件压缩，0代表否
		self.sheet = self.book.add_sheet ('微信详细信息', cell_overwrite_ok = True)
		self.name = time.strftime ("%Y-%m-%d %H:%M:%S", time.localtime ())

#获取微信所有的信息
	def weixin_info(self):
		for friend in self.friends[1:]:
			f_d={
				'uuid':friend['UserName'],                      #账号
				'niceName':friend ['NickName'],                 #网民
				'remarkName' : friend ['RemarkName'],           #备注名
				'city' : friend ['City'],                       #地点
				'sex' : friend ['Sex'],                         #性别1为男
				'province' : friend ['Province'],               #省份
				'signature' : friend ['Signature']              #签名
			}                                                   #获取你需要的数据内容
			self.friedd_data.append(f_d)
		feiend_number=len(self.friedd_data)
		boy=0
		girl=0

		for i in range(feiend_number):
			beizhu=self.friedd_data[i]['remarkName']
			id=self.friedd_data[i]['uuid']
			Sex=self.friedd_data[i]['sex']
			if self.friedd_data[i]['sex']==1:                   #定义性别，把数字转化为男或女
				xingbie='男'
			else:
				xingbie='女'
			if not beizhu:                                      #判断是否有备注
				self.sheet.write(i+1,0,self.friedd_data[i]['niceName'])     #向excel表格写数据
				print(self.friedd_data[i]['niceName']+',性别：'+xingbie+',uuid='+self.friedd_data[i]['uuid'])
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
		self.book.save ('../Weixin/'+self.name+'.xls')
		print(f'一共有{feiend_number}位好友，男孩子有{boy}个，女孩子有{girl}个')

if __name__ == '__main__':
    a=weixin()
    a.weixin_info()
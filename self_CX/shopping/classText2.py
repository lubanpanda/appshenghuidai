#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/9/16 23:17
# @Author  : Panda
import os
import random
import time

now_time=time.strftime ("%Y-%m-%d %H:%M:%S", time.localtime ())
class School (object):
	def __init__ (self, school_name, school_ID, school_Address, school_Attribute):
		'''
        :param school_name: 学校名字
        :param school_ID: 学校ID
        :param school_Address: 学校地址
        :param school_Attribute:学校的属性
        '''
		self.school_name = school_name
		self.school_ID = school_ID
		self.school_Address = school_Address
		self.school_Attribute = school_Attribute

	def teacher (self, teacher_name, teacher_age, teacher_sex):
		'''
        :param teacher_name: 老师的名字
        :param teacher_age: 老师的年龄
        :param teacher_sex: 老师的性别
        :return:
        '''
		self.teacher_name = teacher_name
		self.teacher_age = teacher_age
		self.teacher_sex = teacher_sex
		self.subject = []
		teacher_subject = int (input ('老师你好，请选择你教的科目名称,输入1一直输入，输入2退出:' + os.linesep))
		if teacher_subject == 1:
			while True:
				teacher_info = input ("请输入课程：" + os.linesep)
				if teacher_info == str (2):
					break
				self.subject.append (teacher_info)
			print ("老师的名字叫%s,性别%s,在%s教学，地址是%s，属于%s，今天%s岁，教的学生的科目是%s" % (
				self.teacher_name, self.teacher_sex, self.school_name, self.school_Address, self.school_Attribute,
				self.teacher_age, self.subject))
			teacher_subject_info = "老师的名字叫%s,在%s教学，地址是%s，属于%s，今天%s岁，教的学生的科目是%s" % (
				self.teacher_name, self.school_name, self.school_Address, self.school_Attribute, self.teacher_age,
				self.subject) + os.linesep
			with open ("老师的信息和课程.txt", 'a+', encoding = 'UTF-8') as f:
				f.write (now_time+teacher_subject_info)

	def student (self, student_name, student_age, student_sex, student_grent):
		'''
        :param student_name:学生名字
        :param student_age: 学生年龄
        :param student_sex: 学生性别
        :param student_grent: 学生班级
        :return:
        '''
		self.student_name = student_name
		self.student_age = student_age
		self.student_sex = student_sex
		self.student_grent = student_grent
		print ('学生的名字叫%s，今年%s岁，性别%s，在%s' % (self.student_name, self.student_age, self.student_sex, self.student_grent,))
		student_subject_info = '学生的名字叫%s，今年%s岁，性别%s，在%s' % (
			self.student_name, self.student_age, self.student_sex, self.student_grent,) + os.linesep
		with open ("老师的信息和课程.txt", 'a+', encoding = 'UTF-8') as f:
			f.write (now_time+student_subject_info)
		print('欢迎来到%s学校,欢迎你来到这里'%self.school_name)

	def caishuzi (self):
		'''
		猜数字游戏
		:return:
		'''
		while True:
			try:
				xitongshuzi = random.randint (0, 5)
				root_random = int (input ("猜数字啦，请在0～5之间选择一个数字，与系统的数字一致即为胜利哦!!!不想玩就输入6~~") + os.linesep)
				if root_random == xitongshuzi:
					print (xitongshuzi)
					print ('you are win')
				elif root_random == 6:
					break
				else:
					print (xitongshuzi)
					print ("you failure ")
			except Exception:
				print ("亲，请输入数字哦")
				continue
class Shopping (object):
	"""
	class类
	"""

	def __init__ (self, user_rmb):
		self.user_rmb = user_rmb

	def chongzhi (self):
		print ('剩余的金钱不足，请及时充值')
		chongzhi_xz = int (input ('是否充值，充值请安1，任意键退出：'))
		if chongzhi_xz == 1:
			chongzhi_money = int (input ("请输入金额,充值最低金额为5000，否则将充值失败："))
			with open ("剩余金额.txt", 'w') as chong_rmb:
				chong_rmb.write (str (chongzhi_money + int (s_money)))
			print ("充值成功,成功充值%s元" % chongzhi_money)

	def buy_info (self):
		shop_list = [
			('iphone', 4300),
			('mac', 8888),
			('book', 430),
			('car', 10000),
			('tv', 500),
			('tee', 66),
		]
		user_shop = []

		while True:
			for item in shop_list:
				print (shop_list.index (item), item)
			user_id = input ("请输入商品的ID名称,退出请按'q',现在共有现金%s：" % self.user_rmb)
			if user_id.isdigit ():
				user_id = int (user_id)
				if len (shop_list) > user_id >= 0:
					buy_shop = shop_list [user_id]
					if buy_shop [1] <= self.user_rmb:
						print ("买得起,你购买的商品是%s" % buy_shop [0])
						user_shop.append (buy_shop)
						self.user_rmb -= buy_shop [1]
						print ("购买 %s 成功，花费了 %s 元，还剩余 %s 元" % (buy_shop [0], buy_shop [1], self.user_rmb))
						with open ("剩余金额.txt", 'w') as s:
							s.write (str (self.user_rmb) + os.linesep)
					else:
						print ("余额不足，购物已结束")
						exit ()
						# TODO 这想做成可以直接去充值的，可是一直没想明白怎么去实现，充值之后钱的金额数不能自动刷新，先做成退出的功能
				else:
					print ("没有此商品,请重新输入商品编号")
					continue
			elif user_id == 'q':
				print ("退出购物车成功，你还剩余 %s 元" % self.user_rmb)
				with open ('购物车.txt', 'a+') as buy:
					buy.write (str (user_shop))
				print ("------my_shop-----")
				for shop in user_shop:
					print (shop)
				exit ()

			else:
				print ("你输入的信息有误，请重新输入")


if __name__ == '__main__':
	school1 = School ('苏州街大学', '10001', '北京市海淀区苏州街110号', '公办教育')
	school1.teacher ('panda', 18, '男')
	school1.student ('熊猫', 30, '男', '一年一班')
	print ("%s,Want to play a game?"%school1.student_name)
	play_game = input ("想玩输入X，不想玩输入N")
	if play_game == 'X':
		school1.caishuzi ()
	else:
		print ("不玩喽，还是亲购物吧")
	with open ("剩余金额.txt", 'r') as s_rmb:
		s_money = s_rmb.read ()
		buy1 = Shopping (int (s_money))
		while True:
			if int (s_money) > 5000:
				buy1.buy_info ()
			else:
				buy1.chongzhi ()
			with open ("剩余金额.txt", 'r') as s_rmb:
				s_money = s_rmb.read ()
				buy1 = Shopping (int (s_money))
				if int (s_money) < 5000:
					continue
				else:
					buy1.buy_info ()
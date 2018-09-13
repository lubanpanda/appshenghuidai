#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

"""
大家来写个猜数字的游戏，需求：
1.随机整数，范围1-100
2.用户输入数字，判断类型，非整数给提示，是整数则判断大小
3.记录用户的逐次输入，并判断范围。
举例：中奖数字为60，用户曾经输入过50,55,80,85，那么提示，范围为55-80，如再输入70，则范围为55-70
4.记录猜的次数，最终告诉用户是第几次猜中的


"""
import random

zhongjiang_number = random.randint (0, 100)
shuzi_list = [0, 100, zhongjiang_number]
print ("中奖的号码为：", zhongjiang_number)
print ("请输入中奖的号码,在1-100之间的整数：")


def Caishuzi ():
	while True:
		yonghu = input ()
		if yonghu.isdigit ():
			shuzi_list.append (int (yonghu))
			if 1 <= int (yonghu) <= 100:
				if int (yonghu) == zhongjiang_number:
					break
				else:
					shuzi_list.sort ()
					No1 = shuzi_list.index (zhongjiang_number)
					if int (yonghu) > zhongjiang_number:
						print (f"诶呀，你的数字猜大了，数字在{shuzi_list[No1-1]}和{shuzi_list[No1+1]}之间")
					else:
						print (f"诶呀，你的数字猜小了，数字在{shuzi_list[No1-1]}和{shuzi_list[No1+1]}之间")
			else:
				print ('输入的数字超范围了，请输入1-100之间的数字')
		else:
			print ('你输入的不是整数，请重新输入')
	print ('猜对了，用户一共猜了%s次' % (len (shuzi_list) - 3))


if __name__ == '__main__':
	Caishuzi ()

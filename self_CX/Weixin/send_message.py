#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2018/2/19 13:21
import itchat

from self_CX.Weixin.friend_info import weixin


class Send_wein(weixin):

	@staticmethod
	def send_weixin ():
		Help = """友情提示：
		请输入想要查询的城市名称，如果输入的内容不对，则只显示哈尔滨的天气
		"""
		beizhu_name = input ('请输入要发送微信人的昵称')
		users = itchat.search_friends (name = beizhu_name)
		userName = users [0] ['UserName']
		# print(f'名字：{userName}')
		# itchat.send (Help, toUserName = users)
		itchat.send (msg = Help, toUserName = userName)
		return users,Help

if __name__ == '__main__':
    ab=Send_wein()
    ab.send_weixin()
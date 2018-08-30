#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

from qqbot import _bot as bot, qqbotsched


@qqbotsched (hour = '11,17', minute = '55')
def mytask (bot):
	gl = bot.List ('group', '456班')
	if gl is not None:
		for group in gl:
			bot.SendTo (group, '同志们：开饭啦啦啦啦啦啦！！！')


if __name__ == '__main__':
	bot.Login (['-q 84305510'])
	bot.Run ()

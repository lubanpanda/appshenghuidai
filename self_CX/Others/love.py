#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import requests
from qqbot import RunBot, qqbotsched, qqbotslot

"每天天气提醒"


def weather(name):
    url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + name
    tq_info = requests.get(url)
    tq_json = tq_info.json()
    today = (tq_json.get('data').get('forecast')[0])  # 今天
    tomorrow = (tq_json.get('data').get('forecast')[1])  # 明天
    xiaoxi = tq_json.get('data').get('ganmao')
    high = today['high'][-3:-1]
    if 0 < int(high) < 10:
        info = '今天的天气有点凉哦，注意穿点衣服'
    elif int(high) < 0:
        info = "温度都零下了，记得穿羽绒服哦"
    else:
        info = '今天的温度还可以哦'
    xiangqing = \
        f"城市:{name}\n" \
            f"今日日期：{today['date']}\n" \
            f"天气状况：{today['type']}\n" \
            f"最高温度：{today['high']}\n" \
            f"最低温度：{today['low']}\n" \
            f"明日日期：{tomorrow['date']}\n" \
            f"天气状况：{tomorrow['type']}\n" \
            f"最高温度：{tomorrow['high']}\n" \
            f"最低温度：{tomorrow['low']}\n" \
            f"熊猫提醒: {info}\n" \
            f"官方提醒: {xiaoxi}"
    return xiangqing


# 单独发
@qqbotsched(hour='07', minute='25')
def mytask(bot):
    gl = bot.List('buddy', 'A大白兔奶糖')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, str(weather('南京')))


@qqbotslot
def onQQMessage(bot, contact, member, content):
    if '天气' in content:
        Addrs = content[2:]
        bot.SendTo(contact, str(weather(Addrs)))

    elif bot.isMe(contact, member):
        print('This is me')


if __name__ == '__main__':
    # print(weather())
    RunBot(["-u", "somebody"])

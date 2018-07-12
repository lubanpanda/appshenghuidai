# coding=utf-8

"""
app = Flask(__name__)
@app.route('/')
def hellp():
    return "heool"
@app.route('/')#使用装饰器route()告诉FLASK哪个URL才能触发我们的函数,app.route是flask中的路由
def hello_world():

    return 'Hello World!'

# if __name__ == '__main__':
# 	app.run(debug = True)

conf=configparser.ConfigParser()
conf.read('congit.ini')
# print(info)
print(conf['bitbucket.org']['User'])
a='wo: shi panda'
bbb=a.split(':')[-1].splitlines()[0]
print(bbb)

from qqbot import QQBotSlot as qqbotslot, RunBot


@qqbotslot
def onQQMessage (bot, contact, member, content):
    # if content == '-hello':
    #
    #     bot.SendTo (contact, '你好，我是QQ机器人')
    # elif content == '在':
    #     print(member)
    #     bot.SendTo (contact, '我一直在呢，嘻嘻')
    if content=='111111':

        bot.SendTo(content,atm.main.run(),'发送成功')

    elif content == '-stop':

        bot.SendTo (contact, 'QQ机器人已关闭')
        bot.Stop ()


if __name__ == '__main__':
    RunBot ()
"""
import json

a = {1: 2, 3: 4}
print (json.dumps (a))

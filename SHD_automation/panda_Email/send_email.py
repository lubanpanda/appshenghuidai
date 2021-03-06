#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2018/3/7 14:00

import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_QQ_Email(name):
	username = '1007596772@qq.com'
	password = ''  # 填写自己QQ邮箱的授权码
	sender = username
	receivers = ','.join (['20778962@qq.com'])

	msg = MIMEMultipart()
	msg['Subject'] = 'shenghuidai Test'
	msg['From'] = sender
	msg['To'] = receivers

	# 下面是文字部分，也就是纯文本
	puretext = MIMEText('测试报告')
	msg.attach(puretext)

	# 定义附件的类型
	xlsxpart = MIMEApplication(open(name, 'rb').read())
	xlsxpart.add_header('Content-Disposition', 'attachment', filename=name)
	msg.attach(xlsxpart)

	try:
	    client = smtplib.SMTP_SSL('smtp.qq.com', 465)
	    client.login(username, password)
	    client.sendmail(sender, receivers, msg.as_string())
	    client.quit()
	    print (f'带有附件{name}的邮件发送成功！')
	except Exception as e :
		print('邮件发送失败',e)
if __name__ == '__main__':
	send_QQ_Email ('ATM.zip')

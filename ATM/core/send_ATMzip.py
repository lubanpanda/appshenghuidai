#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import os
import smtplib
import zipfile
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

BASE_DIR = os.path.dirname (os.path.dirname (os.path.abspath (__file__)))


# 打包目录为zip文件（未压缩）
def make_zip (source_dir, output_filename):
	zipf = zipfile.ZipFile (output_filename, 'w')
	pre_len = len (os.path.dirname (source_dir))
	for parent, dirnames, filenames in os.walk (source_dir):
		for filename in filenames:
			pathfile = os.path.join (parent, filename)
			arcname = pathfile [pre_len:].strip (os.path.sep)  # 相对路径
			zipf.write (pathfile, arcname)
	print ('压缩成功文件成功')
	zipf.close ()


def send_QQ_Email (name):
	username = '1007596772@qq.com'
	password = ''  # '填写自己的QQ号的授权码'
	sender = username
	receivers = []
	while True:
		send_qq = input ('请输入要发送的QQ号码,按回车输入下一位QQ接受人，结束时直接按回车即可完成发送' + os.linesep)
		if send_qq is not None and send_qq != '':
			receivers.append (send_qq + '@qq.com')
			continue
		else:
			break
	msg = MIMEMultipart ()
	msg ['Subject'] = 'shenghuidai Test'
	msg ['From'] = sender
	msg ['To'] = ','.join (receivers)

	# 下面是文字部分，也就是纯文本
	puretext = MIMEText ('ATM小程序自动打包发送小程序')
	msg.attach (puretext)

	# 定义附件的类型
	xlsxpart = MIMEApplication (open (name, 'rb').read ())
	xlsxpart.add_header ('Content-Disposition', 'attachment', filename = name)
	msg.attach (xlsxpart)

	try:
		client = smtplib.SMTP_SSL ('smtp.qq.com', 465)
		client.login (username, password)
		client.sendmail (sender, receivers, msg.as_string ())
		client.quit ()
		print ('邮件发送成功！')
	except Exception as e:
		print ('邮件发送失败', e)

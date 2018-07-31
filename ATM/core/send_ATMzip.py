#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "panda  84305510@qq.com"

import os
import smtplib
import zipfile
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep

from tqdm import tqdm

BASE_DIR = os.path.dirname (os.path.dirname (os.path.abspath (__file__)))


# 打包目录为zip文件（未压缩）
def Make_zip (source_dir, output_filename):
	zipf = zipfile.ZipFile (output_filename, 'w')
	pre_len = len (os.path.dirname (source_dir))
	for parent, dirnames, filenames in os.walk (source_dir):
		for filename in filenames:
			pathfile = os.path.join (parent, filename)
			arcname = pathfile [pre_len:].strip (os.path.sep)  # 相对路径
			zipf.write (pathfile, arcname)
	print ('文件打包成功')
	zipf.close ()


def Send_QQ_Email (name):
	username = '1007596772@qq.com'
	password = 'dpkbrcajfhsibfgi'  # '填写自己的QQ号的授权码'
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
	puretext = MIMEText ('ATM小程序\n本程序由系统自动发送，请忽回复。')
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
		for i in tqdm (range (len (name))):
			sleep (0.05)
		print ('邮件发送成功！')
	except Exception as e:
		print ('邮件发送失败', e)

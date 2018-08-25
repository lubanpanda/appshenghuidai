#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from email.mime.application import MIMEApplication

__author__ = "panda  84305510@qq.com"

import os
import smtplib
import zipfile
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
			arcname = pathfile [pre_len:].strip (os.path.sep)
	print ('文件打包成功')
	zipf.close ()


def Send_QQ_Email (name):
	username = '1007596772@qq.com'
	password = 'dpkbrcajfhsibfgi'  # '填写自己的QQ号的授权码'
	sender = username
	receivers = ['84305510@qq.com']

	msg = MIMEMultipart ()
	msg ['Subject'] = 'ATM小程序'
	msg ['From'] = sender
	msg ['To'] = ','.join (receivers)
	# 试一试
	# 下面是文字部分，也就是纯文本
	puretext = MIMEText ('ATM小程序\n本程序由系统自动发送，请忽回复。', name)
	msg.attach (puretext)

	# 定义附件类型
	xlsxpart = MIMEApplication (open (name, 'rb').read ())
	xlsxpart.add_header ('Content-Disposition', 'attachment', filename = name)
	msg.attach (xlsxpart)
	try:
		client = smtplib.SMTP_SSL ('smtp.qq.com', 465)
		client.login (username, password)
		client.sendmail (sender, receivers, msg.as_string ())
		client.quit ()
		for i in tqdm (range (len (name))):
			sleep (0.01)
		print ('邮件发送成功！', receivers, name)
	except Exception as e:
		print ('邮件发送失败', e)


if __name__ == '__main__':
	Make_zip (BASE_DIR, BASE_DIR + '.zip')
	Send_QQ_Email (BASE_DIR + '.zip')

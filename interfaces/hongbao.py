#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda
import requests
import json
from iphoneinfo import shoujiinfo
device=shoujiinfo.connnect_ipad_device()

def hongbao():
	url = "http://apitest.shenghuidai.com:8012/v1/asset/18519291259/red/pocket"
	headers = {'cache-control': "no-cache", 'postman-token': "78531346-aad3-2a2b-57bb-b886fe3718ff"}
	response = requests.request ("POST", url, headers = headers)
	if response.status_code==200:
		print("请求成功")
	else:
		print("请求失败，请查看网络配置")
	hongbao_info=json.loads(response.text)
	hongbao_geshu=[]
	for i in hongbao_info['content']:
		hongbao_geshu.append(len(i))
	url = "http://apitest.shenghuidai.com:8012/v1/asset/18519291259/rate/pocket"
	headers = {'cache-control': "no-cache", 'postman-token': "a5aa815a-8c15-5674-9ead-4b1340b46cbf"}
	response = requests.request ("POST", url, headers = headers)
	if response.status_code==200:
		print("请求成功")
	else:
		print("请求失败，请查看网络配置")
	jiaxiquan_info = json.loads (response.text)
	jiaxiquan_geshu = []
	for i in jiaxiquan_info ['content']:
		jiaxiquan_geshu.append (len (i))
	#print (len (jiaxiquan_geshu))
	device.implicitly_wait(8)
	device.find_elements_by_class_name('android.widget.RadioButton')[3].click()
	device.find_elements_by_class_name('android.widget.TextView')[10].click()
	if len(hongbao_geshu) >0:
		print('有红包,红包个数为：',len(hongbao_geshu))
		device.find_elements_by_class_name ('android.widget.TextView') [3].click ()
		if len (jiaxiquan_geshu) > 0:
			print ("有加息券，个数为：", len (jiaxiquan_geshu))
			device.back ()
	else:
		print("没有红包")
		device.find_elements_by_class_name('android.widget.TextView')[3].click()
		if len(jiaxiquan_geshu)>0:
			print("有加息券，个数为：",len(jiaxiquan_geshu))
			device.back()


if __name__ == '__main__':
    hongbao()
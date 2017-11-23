#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda
from iphoneinfo import shoujiinfo
device=shoujiinfo.connnect_ipad_device()
import time
def banner_iphone():
	time.sleep(5)
	device.find_elements_by_class_name ('android.widget.RadioButton')[2].click ()
	device.find_elements_by_class_name('android.widget.TextView')[3].click()
	device.find_element_by_xpath('//android.view.View[@content-desc="hdzx_hlzcl"]').click()

	device.find_elements_by_class_name('android.view.View')[9].click()
	time.sleep(6)
	device.find_elements_by_class_name('android.widget.Button')[1].click()


if __name__ == '__main__':
    banner_iphone()

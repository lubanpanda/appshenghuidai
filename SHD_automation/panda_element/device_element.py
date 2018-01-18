#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  84305510@qq.com
'手机配置信息'
global device_info
# noinspection PyRedeclaration
device_info={}
device_info['platformName']='Android'
device_info['deviceName']='3cdbb8e5'
device_info['platformVersion']= '7.0'
device_info['sessionOverride']=True  #允许 session 被覆盖 (冲突的话),默认是False
device_info['appPackage']='com.yourenkeji.shenghuidai'
device_info['newCommandTimeout']=600  # 一段时间不输入命令的话，app会退出。这个参数用来设置超时时间
device_info['appActivity']='com.delevin.shenghuidai.welcome.WelcomeActivity'
device_info['autoAcceptAlerts']=True# iOS 的个人信息访问警告(如位置'联系人、图片) 出现时，自动选择接受( Accept )。默认值 false。
device_info['noReset']=True # 不要在会话前重置应用状态。默认值false
device_info['unicodeKeyboard']= True  # 设置appium输入法后就不会弹默认的系统输入法了
device_info['resetKeyboard']= True  # 重置系统输入法

global module_info
# noinspection PyRedeclaration
module_info={}
module_info['首页']='com.yourenkeji.shenghuidai:id/boluos_bt_home'
module_info['项目']='com.yourenkeji.shenghuidai:id/boluos_bt_touzi'
module_info['发现']='com.yourenkeji.shenghuidai:id/boluos_bt_faxian'
module_info['账户']='com.yourenkeji.shenghuidai:id/boluos_bt_my'
module_info['退出']='com.yourenkeji.shenghuidai:id/boluos_exit'

global shouye_modul
# noinspection PyRedeclaration
shouye_modul={}
shouye_modul['投资攻略']='com.yourenkeji.shenghuidai:id/home_guanyuwomen'
shouye_modul['开户绑卡']='android.view.View'  #5
shouye_modul['充值投资']='android.view.View'   #7
shouye_modul['坐等拿收益']='android.view.View' #9
shouye_modul['新手指引']='com.yourenkeji.shenghuidai:id/home_xinshoubidu'
shouye_modul['邀请好友']='com.yourenkeji.shenghuidai:id/home_yaoqinghaoyou'
shouye_modul['每日签到']='com.yourenkeji.shenghuidai:id/home_qiandaosongli'
shouye_modul['消息公告']='com.yourenkeji.shenghuidai:id/home_more_meiti_img'
shouye_modul['邀请-好友']='com.yourenkeji.shenghuidai:id/webView_bt_share'
shouye_modul['分享发送']='com.tencent.mobileqq:id/dialogRightBtn'
shouye_modul['分享取消']='com.tencent.mobileqq:id/dialogLeftBtn'

#帮助中心
shouye_modul['帮助中心']='com.yourenkeji.shenghuidai:id/home_kefu'
shouye_modul['常见问题']='com.yourenkeji.shenghuidai:id/boluos_help_faq'
shouye_modul['咨询电话']='com.yourenkeji.shenghuidai:id/boluos_help_tel'
shouye_modul['在线客服']='com.yourenkeji.shenghuidai:id/boluos_help_online'
shouye_modul['微信公众号']='com.yourenkeji.shenghuidai:id/boluos_help_wechat'
shouye_modul['QQ客服']='com.yourenkeji.shenghuidai:id/boluos_help_QQGroup'

global faxian
# noinspection PyRedeclaration
faxian={}
faxian['平台数据']='com.yourenkeji.shenghuidai:id/yaoqinghaoyou'
faxian['安全保障']='com.yourenkeji.shenghuidai:id/anquanbaozhang'
faxian['积分商城']='com.yourenkeji.shenghuidai:id/jifenshangcheng'
faxian['活动中心']='com.yourenkeji.shenghuidai:id/huodongzhongxin'
faxian['第一个活动']='com.yourenkeji.shenghuidai:id/faxian_xshb_iv'
faxian['第二个活动']='com.yourenkeji.shenghuidai:id/faxian_xydzp_iv'
faxian['更多']='android.widget.TextView'  #list=6

global account
# noinspection PyRedeclaration
account={}
account['隐藏或显示']='com.yourenkeji.shenghuidai:id/my_eyes_checkbox'
account['详情']='com.yourenkeji.shenghuidai:id/imageView1'
account['投资记录']='com.yourenkeji.shenghuidai:id/my_touzi_tv'
account['截标记录']='com.yourenkeji.shenghuidai:id/tvRightComplete'
account['回款日历']='com.yourenkeji.shenghuidai:id/my_return_tv'
account['提现']='com.yourenkeji.shenghuidai:id/my_tixian'
account['我的余额']='com.yourenkeji.shenghuidai:id/tixian_remain_balance'
account['提现-下一步']= 'com.yourenkeji.shenghuidai:id/bt_tixian'
account['资金记录']='com.yourenkeji.shenghuidai:id/my_money_tv'
account['我的优惠券']='com.yourenkeji.shenghuidai:id/my_page_layout'
account['安全管理']='com.yourenkeji.shenghuidai:id/my_safe_tv'
account['个人信息']='com.yourenkeji.shenghuidai:id/my_info_tv'
account['更多']='com.yourenkeji.shenghuidai:id/my_many_tv'
account['风险评估']='com.yourenkeji.shenghuidai:id/more_fengxian_pinggu'

#绑定银行卡元素
account['绑定卡号']='com.yourenkeji.shenghuidai:id/My_bangdingbankcard'
account['姓名']='com.yourenkeji.shenghuidai:id/pay_Name'
account['身份证号']='com.yourenkeji.shenghuidai:id/pay_idCode'
account['银行卡号']='com.yourenkeji.shenghuidai:id/pay_bankCode'
account['手机号']='com.yourenkeji.shenghuidai:id/pay_phone'
account['绑卡-下一步']='com.yourenkeji.shenghuidai:id/bt_pay'
account['支持银行']='com.yourenkeji.shenghuidai:id/tvRightComplete'

#收货地址元素
account['地址管理']='com.yourenkeji.shenghuidai:id/my_head_pic_rl_shouhuoAdress'
account['联系人']='com.yourenkeji.shenghuidai:id/adress_name'
account['手机号']='com.yourenkeji.shenghuidai:id/adress_phone'
account['收货地址']='com.yourenkeji.shenghuidai:id/adress_adress'
account['收货地址格式']='com.yourenkeji.shenghuidai:id/address_tip_tv'
account['地址保存']='com.yourenkeji.shenghuidai:id/adress_bt'

#注册方面的元素
account['验证码']='com.yourenkeji.shenghuidai:id/login_edt_phoneCode'
account['登录密码']='com.yourenkeji.shenghuidai:id/login_set_password'
account['确认密码']='com.yourenkeji.shenghuidai:id/login_copy_password'
account['推荐人']='com.yourenkeji.shenghuidai:id/login_copy_toPhone'
account['确定']='com.yourenkeji.shenghuidai:id/bt_login'
account['注册-下一步']='com.yourenkeji.shenghuidai:id/zhu_bt'

global zhuce
# noinspection PyRedeclaration
zhuce={}
zhuce['登录']='com.yourenkeji.shenghuidai:id/bt_dilog_login'
zhuce['注册']='com.yourenkeji.shenghuidai:id/bt_dilog_resger'
zhuce['账号']='com.yourenkeji.shenghuidai:id/zhu_phone'
zhuce['密码']='com.yourenkeji.shenghuidai:id/fragment_Login_password'
zhuce['跳过']='com.yourenkeji.shenghuidai:id/img_cancel'

global HTMLbaogao
# noinspection PyRedeclaration
HTMLbaogao={}
HTMLbaogao['报告地址']='/Users/yuchengtao/PycharmProjects/shenghuidai/SHD_automation/panda_baogao/'
HTMLbaogao['图片地址']='/Users/yuchengtao/PycharmProjects/shenghuidai/SHD_automation/panda_picture/'

global others
others={}


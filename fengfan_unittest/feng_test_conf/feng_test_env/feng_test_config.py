global config
config = {}
config['appiumPort']='4723'
config['bootStrapPort']=''
config['seldnroidPort']=''
config['chromiumPort']=''
config['platformName'] = 'Android'
config['plarformVersion'] = '4.4.4'
config['deviceName'] = '1ee1d49b1f5c3'
config['appPackage'] = 'com.yce.deerstewardphone'
config['appActivity']="com.yce.deerstewardphone.activity.SplashActivity"
config['noReset'] = True
config['unicodekeyboard'] = True
config['resetKeyboart'] = True
config['automationName']= 'uiautomator2'
config['app'] = r'D:\\bao\\app-debug(21).apk'
config['newCommandTimeout'] = '300'

global bottom
bottom = {}
bottom['首页id'] = 'com.yce.deerstewardphone:id/btn_home'
bottom['商城id'] = 'com.yce.deerstewardphone:id/btn_service'
bottom['消息id'] = 'com.yce.deerstewardphone:id/btn_im'
bottom['我id']   = 'com.yce.deerstewardphone:id/btn_me'

global login  #登录页面action
login = {}
login['账号id'] = 'com.yce.deerstewardphone:id/edt_login_user'
login['验证码id'] = 'com.yce.deerstewardphone:id/lay_get_code'
login['验证码文字id'] = 'com.yce.deerstewardphone:id/txt_get_code'
login['密码id'] = 'com.yce.deerstewardphone:id/edt_login_code'
login['登录id'] = 'com.yce.deerstewardphone:id/btn_submit'

global newUserLogin #新用户登录首页action
newUserLogin = {}
newUserLogin['立即使用xpath'] = '//android.widget.TextView[@text=\"立即使用\"]'
newUserLogin['完善资料xpath'] = '//android.widget.TextView[@text=\"(完善个人资料并自动创建家庭群)\"]'
newUserLogin['logoxpath']     = '//android.widget.RelativeLayout[@resource-id=\"com.yce.deerstewardphone:id/lay_head\"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]'
newUserLogin['名医视讯id']    = 'com.yce.deerstewardphone:id/img_heath_guide'
newUserLogin['二维码id']      = 'com.yce.deerstewardphone:id/img_dimension_code'

global perfect  #完善信息action
perfect = {}
perfect['家庭群名id'] = 'com.yce.deerstewardphone:id/edt_family_name'
perfect['更换头像id'] = 'com.yce.deerstewardphone:id/lay_img_head_update'
perfect['用户名id']   = 'com.yce.deerstewardphone:id/edt_user_name'
perfect['身份证号id'] = 'com.yce.deerstewardphone:id/edt_id_card'
perfect['性别男id']   = 'com.yce.deerstewardphone:id/btn_man'
perfect['性别女id']   = 'com.yce.deerstewardphone:id/btn_woman'
perfect['出生年月日id'] = 'com.yce.deerstewardphone:id/txt_age_select'
perfect['身高id']      =  'com.yce.deerstewardphone:id/edt_height'
perfect['体重id']      =  'com.yce.deerstewardphone:id/txt_weight_unit'

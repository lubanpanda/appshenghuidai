import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '84305510@qq.com'
my_user = ("919792828@qq.com",)
def mail():
    ret = True
    try:
        msg = MIMEText("""
        翟科是个大逗逼
        咿呀咿呀哟
        天气好的话别忘了我周五去找你撸串哦
        摸摸哒
        """, 'plain', 'utf-8')
        msg['From'] = formataddr(["熊猫", my_sender])
        msg['To'] = 'entry'.join(my_user)
        msg['Subject'] = "测试"
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(my_sender, "ayjeieecvoxdbhdf")
        server.sendmail(my_sender, [my_user, ], msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret
ret = mail()
if ret:
    print("ok,邮件发送成功，请注意查收")
    print("ok,给%s邮件发送成功，,请注意查收" % my_user)
else:
    print("发送失败")

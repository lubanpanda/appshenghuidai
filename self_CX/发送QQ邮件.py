import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import requests
from bs4 import BeautifulSoup

my_sender = '84305510@qq.com'
my_user = "1007596772@qq.com"

def mail():
    ret = True
    try:
        with open('QQ.text','r') as e:
            news=e.read()
        msg = MIMEText(news, 'plain', 'utf-8')
        msg['From'] = formataddr(["熊猫", my_sender])
        msg['To'] = 'entry'.join(my_user)
        msg['Subject'] = "天气预报 "
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(my_sender, "ayjeieecvoxdbhdf")
        server.sendmail(my_sender, [my_user, ], msg.as_string())
        server.set_debuglevel(1)
        server.quit()
    except Exception:
        ret = False
    return ret
if __name__ == '__main__':
    ret = mail()
    if ret:
        print(f"ok,给{my_user}邮件发送成功，,请注意查收")
    else:
        print("发送失败")

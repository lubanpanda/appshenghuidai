import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import requests
from bs4 import BeautifulSoup

my_sender = '84305510@qq.com'
my_user = "1007596772@qq.com"

def weather(city_name):
	url='http://m.sohu.com/weather/?city='+city_name
	UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
	weather_shuju=requests.get(url,headers={'User-Agent':UA})
	html=weather_shuju.text
	soup=BeautifulSoup(html,'html.parser')
	now_wendu=soup.find('p',class_='cur').string
	up_wendu=soup.find('em',class_='highest').string
	low_wendu=soup.find('em',class_='lowest').string
	xiangqing=soup.find('em',class_='stat').string
	PM=soup.find('p',class_='tit').string
	fengli=soup.find('div',class_='pm')
	feng,shidu=map(lambda a:a.string,fengli)
	return (f'城市：{city_name}\n现在的温度：{now_wendu}\n最高气温：{up_wendu}\n最低温度：{low_wendu}\n天气情况:{xiangqing}\nPM值：{PM}\n舒适指数：{feng,shidu}')
def mail(news):
    ret = True
    try:
    #     with open('QQ.text','r') as e:
    #         news=e.read()
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
    news=weather("北京")
    ret = mail(news)
    if ret:
        print(f"ok,给{my_user}邮件发送成功，,请注意查收")
    else:
        print("发送失败")

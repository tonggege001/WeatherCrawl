__author__ = 'Administor'
# -*- coding: UTF-8 -*-
from smtplib import SMTP_SSL
from WeatherCra import get_description
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from email.header import Header
import sys


message = get_description()

#qq邮箱smtp服务器
host_server = 'smtp.qq.com'
#sender_qq为发件人的qq号码
sender_qq = '*270**783*'
#pwd为qq邮箱的授权码
pwd = '###########'
#发件人的邮箱
sender_qq_mail = '*270**783*@qq.com'
#收件人邮箱
receiver = ""
#邮件的正文内容
mail_content = message
#邮件标题
mail_title = '天气预报'

#ssl登录
smtp = SMTP_SSL(host_server)
#set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
smtp.set_debuglevel(0)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

msg = MIMEText(mail_content, "plain", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
qqs = []
with open("qqnumbers.txt",'r') as f:
    qqs = f.read().split('\n')
for i in range(len(qqs)):
    qqs[0]
    if(qqs[i]!=""):
        msg["To"] = qqs[i]
        smtp.sendmail(sender_qq_mail, qqs[i], msg.as_string())
smtp.quit()


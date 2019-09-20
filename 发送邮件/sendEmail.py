#!/usr/bin/python
# coding=UTF-8

import smtplib
from email.mime.text import MIMEText

msg_Sender = '3522271681@qq.com'                                #发送方邮箱
msg_code = 'aymhwvxiumgjdbcj'                                  #发送方邮箱的授权码
msg_Receiver = '7277710@qq.com'                              #收件人邮箱

subject = "python邮件测试"                                        #主题
content = "这是我使用python smtplib及email模块发送的邮件sss"      #正文
msg = MIMEText(content,_charset="utf-8")
msg['Subject'] = subject
msg['From'] = msg_Sender
msg['To'] = msg_Receiver
try:
    s = smtplib.SMTP_SSL("smtp.qq.com",465)                   #邮件服务器及端口号
    s.login(msg_Sender, msg_code)
    s.sendmail(msg_Sender, msg_Receiver, msg.as_string())
    print "发送成功"
# except s.SMTPException,e:
#     print "发送失败"
finally:
    s.quit()

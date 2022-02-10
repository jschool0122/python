#!/usr/bin/env python
# coding: utf-8

# In[4]:


#메일 발송 자동화

# -*- coding:utf-8 -*-
import smtplib
from email.header import Header
from email.mime.text import MIMEText


def send_mail(title, body, to=[], cc=[], bcc=[]):
    sender = ""
    sender_account = ""
    sender_password = ""
    
    msg = MIMEText(body, "html", _charset='utf-8')
    msg['Subject'] = Header(s=title, charset="utf-8")
    msg['From'] = sender
    msg['To'] = ", ".join(to)
    msg['Cc'] = ", ".join(cc)
    msg['Bcc'] = ", ".join(bcc)

    s = smtplib.SMTP("smtp.gmail.com", "587")
    s.starttls()
    s.login(sender_account, sender_password)
    s.sendmail(sender_account, to + cc + bcc, msg.as_string())
    s.quit()


mail_title = "자동화프로젝트_test입니다"
body = "자동화프로젝트_test입니다"
cc = []
bcc = []

send_mail(mail_title, body, ['보내고자 하는 이메일'], cc, bcc)


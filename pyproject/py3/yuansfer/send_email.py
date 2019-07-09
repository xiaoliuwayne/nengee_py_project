#!/usr/bin/env python
# coding=utf-8
"""
Send html email test
"""

import os
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
# import sys
# import imp
# imp.reload(sys)
# sys.setdefaultencoding("utf-8")

# _EMAIL_TEMPLATE = 'email_template.html'
_EMAIL_TEMPLATE = 'verify_code_template_table2.html'
# _EMAIL_TEMPLATE = 'email_code_table2.html'



def _get_mime_image(image_path, cid):
    with open(image_path, 'rb') as f:
        msg_image = MIMEImage(f.read())
    msg_image.add_header('Content-ID', '<%s>' % cid)
    return msg_image


def _get_mime_text(html_content):
    msg_alternative = MIMEMultipart('alternative')
    msg_text = MIMEText(html_content, 'html', 'utf-8')
    msg_alternative.attach(msg_text)
    return msg_alternative


def _get_email_template():
    print('__file__',__file__)
    # __file__ C:\Users\My\Desktop\Nengee\python\send_email.py
    cur_path = os.path.dirname(__file__)
    email_template_path = os.path.join(cur_path, _EMAIL_TEMPLATE)
    # email_template_path = cur_path + '\\' + _EMAIL_TEMPLATE
    print('email_template_path',email_template_path)
    with open(email_template_path, 'r',encoding='utf-8') as f:
        content = f.read()
    return content


def main():
    email_server_host = 'smtp.aliyun.com'
    email_server_port = 465
    username = 'wayne_lau@aliyun.com'
    password = 'AAAAAAAAA'
    receivers = ['wayne.lau.gz@gmail.com', username]

    msg_root = MIMEMultipart('related')
    msg_root['Subject'] = Header(u'发送邮件测试', 'utf-8')
    msg_root['From'] = username
    msg_root['To'] = '; '.join(receivers)

    html_content = _get_email_template()
    msg_root.attach(_get_mime_text(html_content))

    cur_path = os.path.dirname(__file__)
    # head_jpg = os.path.join(cur_path, 'head.jpg')
    # msg_root.attach(_get_mime_image(head_jpg, 'head_jpg'))

    # foot_jpg = os.path.join(cur_path, 'foot.jpg')
    # msg_root.attach(_get_mime_image(foot_jpg, 'foot_jpg'))

    client = smtplib.SMTP_SSL(email_server_host, email_server_port)
    client.login(username, password)
    client.sendmail(username, receivers, msg_root.as_string())
    client.quit()


if __name__ == '__main__':
    main()

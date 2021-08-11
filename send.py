import smtplib
import email
# 负责构造文本
from email import encoders
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header


def send_email(name, email_address, code, link, date):
    # SMTP服务器,这里使用163邮箱
    mail_host = "smtp.163.com"
    # 发件人邮箱
    mail_sender = "13480369698@163.com"
    # 邮箱授权码,注意这里不是邮箱密码,如何获取邮箱授权码,请看本文最后教程
    mail_license = "MWTOQGRVXTNZGSHT"
    # 收件人邮箱，可以为多个收件人
    # 只能发三个
    mail_receivers = ["13480369698@163.com", email_address]
    # 75075153@qq.com
    # 505373410@qq.com
    mm = MIMEMultipart('related')

    # 邮件主题
    subject_content = """Python邮件测试"""
    # 设置发送者,注意严格遵守格式,里面邮箱为发件人邮箱
    mm["From"] = "13480369698@163.com"
    # 设置接受者,注意严格遵守格式,里面邮箱为接受者邮箱
    mm["To"] = ','.join(mail_receivers)
    # 设置邮件主题
    mm["Subject"] = Header(subject_content, 'utf-8')

    # sendfile = open(r'D:\Users\highw\PycharmProjects\pythonProject\zjx.png', 'rb').read()
    sendfile = open(code, 'rb').read()
    text_att = MIMEText(sendfile, 'base64', 'utf-8')
    # text_att["Content-Type"] = 'application/octet-stream'
    text_att.add_header('Content-Disposition', 'attachment', filename='zjx.png')
    text_att.add_header('Content-ID', '<0>')
    text_att.add_header('X-Attachment-Id', '0')
    # encoders.encode_base64(text_att)
    mm.attach(text_att)

    html = """
    <html>  
      <head></head>  
      <body>  
        <p>Hello {name},<br>  
           Your code:<br>         
           <img src="cid:0" height="200" width="200"/><br>
           Your link： {link}<br> 
           Date:{date}<br> 
        </p> 
      </body>  
    </html>  
    """.format(name=name, link=link, date=date)
    # <img src="cid:0" /><br>
    text_html = MIMEText(html, 'html', 'utf-8')
    # text_html["Content-Disposition"] = 'attachment; filename="texthtml.html"'
    mm.attach(text_html)

    # 创建SMTP对象
    stp = smtplib.SMTP()
    # 设置发件人邮箱的域名和端口，端口地址为25
    stp.connect(mail_host)
    # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
    stp.set_debuglevel(1)
    # 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
    stp.login(mail_sender, mail_license)
    # 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str
    stp.sendmail(mail_sender, mm["To"].split(','), mm.as_string())
    print("邮件发送成功")
    # 关闭SMTP对象
    stp.quit()

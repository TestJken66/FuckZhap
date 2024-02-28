import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header


import os
# 从环境变量获取口令
mail_pass = os.getenv('EMAIL_PASS2', '默认值')

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "chinapolicy110@163.com"    # 用户名
# mail_pass = "KEMJEXTPIQLPENGG"   # 口令

sender = 'chinapolicy110@163.com'
receivers = ['ecochainliesstop@gmail.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("chinapolicy110@163.com", 'utf-8')
message['To'] = "ecochainliesstop@gmail.com"  # 直接使用字符串赋值
subject = '【警惕网络诈骗,人人有责】'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
message.attach(MIMEText('警惕网络诈骗,人人有责,不作恶，无作恶！！', 'plain', 'utf-8'))

# 构造附件，传送当前目录下的 test.mp4 文件
att = MIMEBase('application', 'octet-stream')
att.set_payload(open('1926_1708514905.mp4', 'rb').read())
encoders.encode_base64(att)
att.add_header('Content-Disposition', 'attachment; filename="1926_1708514905.mp4"')
message.attach(att)


for i in range(20):
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件", e)
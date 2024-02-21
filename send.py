import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="chinapolicy110_365@163.com"    #用户名
mail_pass=""   #口令  
 
 
sender = 'chinapolicy110_365@163.com'
receivers = ['chinapolicy110_365@163.com','ecochainliesstop@gmail.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱 
 
message = MIMEText('【警惕网络诈骗,人人有责】!', 'plain', 'utf-8')
message['From'] = Header("chinapolicy110_365@163.com", 'utf-8')
message['To'] =  Header("ecochainliesstop@gmail.com", 'utf-8')
 
subject = '【警惕网络诈骗,人人有责】'
message['Subject'] = Header(subject, 'utf-8')
 
 
for i in range(100):
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host,25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")
# -*- coding:UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.header import Header



class sendEmail:

    def __init__(self,my_sender,my_pass,my_user):
        self.my_sender = my_sender
        self.my_pass = my_pass
        self.my_user = my_user

    ##普通发送
    def mail(self):
        ret = True
        try:
            msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
            msg['From'] = formataddr(["System", self.my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["FK", self.my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = "python发送邮件测试"  # 邮件的主题，也可以说是标题

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(self.my_sender, self.my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.my_sender, [self.my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret = False
        return ret

    #带有附件的邮件
    def mail_mult(self,file):
        ret = True
        try:
            # 创建一个带附件的实例
            message = MIMEMultipart()
            message['From'] = Header("jiuyue", 'utf-8')
            message['To'] = Header("python", 'utf-8')
            subject = ''
            message['Subject'] = Header(subject, 'utf-8')

            # 邮件正文内容
            message.attach(MIMEText('python邮件 ', 'plain', 'utf-8'))

            # 构造附件1，传送当前目录下的 test.txt 文件
            att1 = MIMEText(open('111.xlsx', 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att1["Content-Disposition"] = 'attachment; filename="111.xlsx"'
            message.attach(att1)

            # 构造附件2，传送当前目录下的 runoob.txt 文件
            att2 = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
            att2["Content-Type"] = 'application/octet-stream'
            att2["Content-Disposition"] = 'attachment; filename="nihao.txt"'
            message.attach(att2)

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(self.my_sender, self.my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.my_sender, [self.my_user, ], message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret = False
        return ret

my_sender = '489435760@qq.com'  # 发件人邮箱账号
my_pass = 'my_pass'  # 发件人邮箱密码，qq有自己的授权码
my_user = '489435760@qq.com'  # 收件人邮箱账号，我这边发送给自己
#如何调用邮件发送功能
e = sendEmail(my_sender,my_pass,my_user)

#发送带有附件的邮件
# e.mail_mult('ss.txt')
#发送十次邮件
for i in range(10):
    e.mail()
# ret = 1
#
# if ret:
#     print("邮件发送成功")
# else:
#     print("邮件发送失败")

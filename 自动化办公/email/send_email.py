# -*- coding:utf-8 -*-
"""
作者：HET
日期：2023年04月14日
"""
import time
import smtplib
import schedule
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

# 第三方的smtp
mail_host='smtp.sina.com'
mail_user='xxx'   # 用户名
mail_pass='xxx'  # 可能是邮箱授权码，也可能是是密码（大多为授权码）
# 进入邮箱smtp，开通，获取授权码
sender='xxx'  # 发送者邮箱
receivers=['xxx']  # 接收者邮箱

# =======发送普通文本邮件=======
# message=MIMEText('这是一个测试','plain','utf-8')  # 内容  plain：是普通的文本格式
# =======发送html邮件==========
# message=MIMEText('<p style="color:red">这是一个测试</p>','html','utf-8')  # 内容  html：html格式类型
# =======发送带附件的邮件=======
message=MIMEMultipart()

message['From']=Header(sender)
message['Subject']=Header('python脚本测试','utf-8')  # 主题
# =========以下内容只有带附件的邮件需要使用============
attr=MIMEText(open('send','rb').read(),'base64','utf-8')
attr['Content-Type']='application/octet-stream'
attr['Content-Disposition']='attachment;filename="send_email.py"'  # 将send_email.py以附件的形式发送
message.attach(attr)
message.attach(MIMEText('这是一个测试','plain','utf-8'))
# ================================================
def send():
    # 若发送失败，进行异常处理
    try:
        smtp_obj=smtplib.SMTP()
        smtp_obj.connect(mail_host,25)  # 端口号可以在邮箱设置中查看
        smtp_obj.login(mail_user,mail_pass)
        smtp_obj.sendmail(sender,receivers,message.as_string())  # .as_string()是将信息转成加密字符串发送
    except smtplib.SMTPException as e:
        print('error is：%s' % e)

if __name__=='__main__':
    schedule.every(10).seconds.do(send())  # 每10s执行一次send函数
    # 通过while不停监测任务是否达到定时时间
    while 1:
        schedule.run_pending()  # 此时会进行判断，当前是否有任务处于要被执行的状态，若没有，会结束程序
        time.sleep(1)  # 避免查询频率过快，消耗CPU，提高性能
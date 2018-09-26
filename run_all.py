# coding: utf-8
import unittest
from common import HTMLTestRunner_cn
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 用例地址
tc_dir = "D:\\test\\case"
# 测试套件收集用例
# discover方法加载多个用例集合
discover = unittest.defaultTestLoader.discover(start_dir=tc_dir,
                                               pattern="aws*.py",
                                               top_level_dir=None)

print(discover)

if __name__ == "__main__":
    # 生成报告的路径及时间
    report_path = "D:\\thiscomputer\\workspace\\aws_test\\report\\"+"result.html"
    # 打开报告并写入测试结果
    fp = open(report_path,"wb")
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                              title=u"大数据平台AWS测试报告",
                                              description=u"用例执行结果")

    # 运行测试用例
    runner.run(discover)
    # 关闭报告文件
    fp.close()


# --------1.跟发件相关的参数------
smtserver = "smtp.qq.com"      # 发件服务器
port = 465
sender = "515923085@qq.com"    # 账号
psw = "ektidiwtgkrdbhdj"       # 密码
receiver = "zhanglei2@ghcchina.com.cn"  # 接收人

# --------2.编辑邮件的内容-----
# 读文件
file_path = "D:\\thiscomputer\\workspace\\aws_test\\report\\"+"result.html"
with open(file_path,"rb") as fp:
    mail_body = fp.read()

msg = MIMEMultipart()
msg["from"] = sender
msg["to"] = receiver
msg["subject"] = "大数据平台AWS测试"

# 正文
body = MIMEText(mail_body,"html","utf-8")
msg.attach(body)

# 附件
att = MIMEText(mail_body,"base64","utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = "attachment;filename='test_report.html'"
msg.attach(att)

# --------3.发送邮件-----
smtp = smtplib.SMTP_SSL(smtserver,port)         # 连服务器
smtp.login(sender,psw)                          # 登录
smtp.sendmail(sender,receiver,msg.as_string())  # 发送
smtp.quit()                                     # 关闭



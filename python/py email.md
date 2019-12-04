```python
import smtplib
from email.mime.text import MIMEText


class MailUtil(object):
    def __init__(self, host, user, passwd, port="465"):
        if port == "465":
            # 加密端口
            self.server = smtplib.SMTP_SSL(host, port)
            # 括号中对应的是发件人邮箱账号、邮箱密码
        elif port == "25":
            self.server = smtplib.SMTP()
            self.server.connect(host, port)  # 25 为 SMTP 端口号
        else:
            raise AttributeError("mail port must be 465 or 25")
        self.server.login(user, passwd)
        self.host = host
        self.user = user
        self.passwd = passwd

    def send(self, receivers, message):
        self.server.sendmail(self.user, receivers, message.as_string())

    def send_by_html(self, to_reciver: list, msg, subject, cc_reciver=[]):
        """抄送自己可以避免退信"""
        if type(msg) == str:
            message = MIMEText(msg, "html", 'utf-8')
            message['From'] = self.user
            message['To'] = ";".join(to_reciver)
            message['Subject'] = subject
        elif type(msg) == MIMEText:
            message = msg
        else:
            raise AttributeError("非法的msg")

        receivers = to_reciver
        if cc_reciver:
            message['Cc'] = ";".join(cc_reciver)
            receivers += cc_reciver

        self.send(receivers, message)


if __name__ == "__main__":
    a = MailUtil('smtp.163.com', 'test@163.com', 'passwd')
    html = "<h1>test</h1>"
    a.send_by_html(['test@qq.com', 'test2@163.com'], "html", '错误通知', ['test@163.com'])

```

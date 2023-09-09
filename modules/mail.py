import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

class Mail:
    def __init__(self, config):
      self.smtp_server = config['smtp_server']
      self.smtp_port = config['smtp_port']
      self.smtp_email = config['smtp_email']
      self.smtp_password = config['smtp_password']
      self.msg = MIMEMultipart()
      self.msg['From'] = self.smtp_email
    def send(self, target):
      self.msg['To'] = target
      now = datetime.datetime.now()
      subject = now.strftime('%Y-%m-%d')+" github하세요 !"
      message = '해라고..'
      
      self.msg['Subject'] = subject
      self.msg.attach(MIMEText(message, 'plain'))
      try:
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.smtp_email, self.smtp_password)
            server.sendmail(self.smtp_email, target, self.msg.as_string())
        return True
      except:
        return False

# 이메일 객체 생성


# 본문 추가

# SMTP 서버에 연결 및 로그인

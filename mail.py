import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re

class Email:
    """
    Класс для отправки и получения почтовых сообщений
    """

    def __init__(self, login, password):
        """
        Метод объявления класса Email
        :param login: e-mail адрес
        :param password: пароль почтового ящика
        """
        self.login = login
        self.password = password
        regexp = r"[\w\W]+\@([a-zA-Z0-9-]+\.[a-z]+)"
        self.mail_smpt = re.sub(regexp, r"smpt.\1", login)
        self.mail_imap = re.sub(regexp, r"imap.\1", login)

    def create_msg(self, subject, recipients, msg_txt):
        """
        Метод создания исходящего сообщения
        :param subject: предмет сообщения
        :param recipients: получатели сообщения (список)
        :param msg_txt: тест сообщения
        """
        self.recipients = recipients
        self.msg = MIMEMultipart()
        self.msg['From'] = self.login
        self.msg['To'] = ', '.join(recipients)
        self.msg['Subject'] = subject
        self.msg.attach(MIMEText(msg_txt))

    def send_msg(self):
        """
        Метод отправки созданного почтового сообщения
        """
        ms = smtplib.SMTP(self.mail_smpt, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, self.recipients, self.msg.as_string())
        ms.quit()
        # send end

    def  receive_msg(self, header=None):
        """
        Метод получения почтового сообщения
        :param header: предмет сообщения, если необходимо
        :return: self.email_msg: текст искомого сообщения либо последнего из непрочитанных
        """
        mail = imaplib.IMAP4_SSL(self.mail_imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', "", criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', str(latest_email_uid), '(RFC822)')
        self.email_msg = email.message_from_string(data[0][1])
        mail.logout()
        return self.email_msg




from functions import task12
from mail import Email
import re

if __name__ == '__main__':
    # Решение заданий 1-2 (все функции в файле functions.py)
    task12()

    # Решение задания 3 ( класс Email в файле mail.ru)
    login = input('Введите ваш почтовый адрес: ')
    password = input('Введите пароль к почтовому ящику: ')
    my_email = Email(login=login, password=password)
    if int(input('Отправить или получить почту (1 - отправить, 0 - получить): ')):
        subject = input('Предмет сообщения: ')
        recipients = input('E-mail адреса получателей через запятую: ')
        message = input('Текст сообщения: ')
        recipients = re.sub(r"\s", "", recipients).split(',')
        my_email.create_msg(subject, recipients, message)
        my_email.send_msg()
    else:
        header = input('Предмет получаемого сообщения (необязательно): ')
        receive_msg = my_email.receive_msg(header)












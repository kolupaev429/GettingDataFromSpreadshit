import smtplib
import codecs
import getingdata


def send(recipient, text):
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_obj.starttls()
    smtp_obj.login('csoprocom.sa@gmail.com', 'qgks245njsd1')
    smtp_obj.sendmail('csoprocom.sa@gmail.com', recipient, text)
    smtp_obj.quit()


if __name__ == '__main__':
    with codecs.open('text.txt', 'r', 'utf_8') as file:
        message_text = file.read()

    text = ("""\
Subject: Вебінар "Розробка телеграм-боту на Python"

""" + message_text).encode('utf-8')
    recipients = getingdata.recipients

    for recipient in recipients:
        send(recipient, text)

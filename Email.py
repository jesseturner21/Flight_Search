import smtplib
import os


class Email:
    def __init__(self):
        # # ------------SENDING EMAIL----------------#

        self.EMAIL = 'searchflightsearch@gmail.com'
        self.PASSWORD = os.environ.get('EMAIL_PASSWORD')

    def send_email(self, receiver, subject, body):
        # connecting to email
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=self.EMAIL, password=self.PASSWORD)
            message = "Subject: " + subject + "\n\n" + body

            connection.sendmail(from_addr=self.EMAIL, to_addrs=receiver, msg=message)

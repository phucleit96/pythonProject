from twilio.rest import Client
import smtplib
TWILIO_SID = "AC94a6705ee8376c7cbfc5c13db05db0e0"
TWILIO_AUTH_TOKEN = "0b9b17390d4046af0a7d5f081775def2"
TWILIO_VIRTUAL_NUMBER = '+16318886492'
TWILIO_VERIFIED_NUMBER = '+84936382650'
my_email = "moonknight196@gmail.com"
password = "qrqmazreuirftjlo"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    # def send_sms(self, message):
    #     message = self.client.messages.create(
    #         body=message,
    #         from_=TWILIO_VIRTUAL_NUMBER,
    #         to=TWILIO_VERIFIED_NUMBER,
    #     )
    #     # Prints if successfully sent
    #     print(message.sid)
    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            for email in emails:
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject: NEW LOW PRICE FLIGHT!\n\n{message}".encode('utf-8')
                )
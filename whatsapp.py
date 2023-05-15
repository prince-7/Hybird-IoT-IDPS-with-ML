from twilio.rest import Client
from tabulate import tabulate

class WhatsApp():
    def __init__(self, account_sid, auth_token, from_number, to_number):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.from_number = from_number
        self.to_number = to_number

    def send_message(self, message):
        report = f"Results of latest analysis:- \n\n {tabulate(message, showindex=False, headers=message.columns)}"
        client = Client(self.account_sid, self.auth_token)
        client.messages.create(
            body=report,
            from_='whatsapp:'+self.from_number,
            to='whatsapp:'+self.to_number
        )

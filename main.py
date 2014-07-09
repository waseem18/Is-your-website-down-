import webapp2
from twilio import twiml
from twilio.rest import TwilioRestClient



class SendSMS(webapp2.RequestHandler):
    def get(self):
        account_sid = "AC5e69469ba8cb4c0ae0aeee5a592db605"
        auth_token = "561ed7bcde49ee9d294e128b572d0619"
        client = TwilioRestClient(account_sid, auth_token)
        rv = client.sms.messages.create(to="+919160216436",
                                        from_="+19138714534",
                                        body="Hello your website/blog is down!")
        self.response.write(str(rv.sid))

app = webapp2.WSGIApplication([('/send_sms', SendSMS)],
                              debug=True)

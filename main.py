#Texts you when your blog or website goes down!
#Working on a working prototype.
#Send me a pull request to report bugs or to add new features.
#Author: Wasim Thabraze

import webapp2
import json
import urllib2
import contextlib
from twilio import twiml
from twilio.rest import TwilioRestClient
from google.appengine.api.app_identity import get_application_id

uptime_key = os.environ['uptime_key']
twilio_sid = os.environ['twilio_sid']
twilio_from = os.environ['twilio_from']
twilio_to = o.environ['twilio_to']

def SendSMS(self):
    account_sid = "#"
     auth_token = "#"
    client = TwilioRestClient(account_sid, auth_token)
    rv = client.sms.messages.create(to=twilio_to,
                                    from_=twilio_from,
                                    body="Hey there! Your website is down!")
        #self.response.write(str(rv.sid))

class WebsiteStatus(webapp2.RequestHandler):
    def get(self):
        with contextlib.closing(urllib2.urlopen(uptime_api)) as data
        result = json.load(data)

        for m in result['monitors']['monitor']:
            if m['status'] == '9':
                SendSMS()


app = webapp2.WSGIApplication([('/send_sms', SendSMS)],
                              debug=True)

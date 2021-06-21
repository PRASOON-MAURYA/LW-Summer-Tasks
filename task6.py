# TASK - 6.2

# Import Module Used to Send Whatsapp Message
! pip install pywhatkit
import pywhatkit

# Use 'sendwhatmsg()' function to send message
pywhatkit.sendwhatmsg ( "Friend's Phone Number", "Message",Hour ,Minute )

# To Confirm Message Send or Not
print ("Message Sent...")

# TASK - 6.3


# Import Module Used to Send SMS
! pip install twilio
from twilio.rest import Client as cl

# Storing ACCOUNT_SID and AUTH_TOKEN provided in Twilio Account
x = "ACCOUNT_SID"
y = "AUTH_TOKEN"
client = cl (x,y)

# Sending SMS
SMS = client.messages.create ( from_ = "Number Purchased in Twilio Account" , to = "Mobile Number to Whom You Want to Message" , body = "Message" )

# To Confirm SMS Send or Not
print ("SMS Sent...")

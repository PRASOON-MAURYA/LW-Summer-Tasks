# IMAGE RECOGNITION

import cv2
import what_sms as whs
import send_email as em
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    if len(faces)>0:
        # Display
        em.send_email()
        whs.send_what_sms()
        cv2.imshow('img', img)
        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k==27:
            cv2.destroyAllWindows()
            break
# Release the VideoCapture object
cap.release()


SENDING EMAIL

import smtplib

def send_email():

   message = f"""From: From Person {sender}
   To To Person {recv}
   Subject: Face Found
   this indicates that the face has been found 
   """ 
   try:
      smtpObj = smtplib.SMTP(smtpserv,port=smtpport)
      smtpObj.login(sender, password)
      smtpObj.sendmail(sender, receivers, message)         
      print("Successfully sent email")
   except SMTPException:
      print("Error: unable to send email")

print("Enter email credentials")
sender = input("Enter sender email")
recv =input("Enter reciever email")
recv = list(recv)
password = input("Enter_Your_Password_Here")
smtpport = int(input("enter smtp port"))
smtpserv =input("Enter smtp server address")


SENDING WHATSAPP MESSAGE AND SMS

#install pywhatkit
import pywhatkit
from twilio.rest import Client as cl
print("Enter Twilio account credentials and whatsapp credentials for sending sms and whatsapp")
x = input("Enter Twilio Account SID")
y = input("Enter Twilio Account Auth Token")
client = cl (x,y)
recv_mob=input("Enter reciever mob number")
recv_what=input("Enter reciever whatsapp number")
num_pur=input("Enter purchased twilio number")
def send_what_sms():
    # Use 'sendwhatmsg()' function to send message
    pywhatkit.sendwhatmsg(recv_what, "Face found",Hour ,Minute )

    # To Confirm Message Send or Not
    print ("Message Sent...")


    # Sending SMS
    SMS = client.messages.create( from_ = num_pur , to = recv_mob , body = "Your face was detected!!" )

    # To Confirm SMS Send or Not
    print ("SMS Sent...") 

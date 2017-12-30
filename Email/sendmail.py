#!/usr/bin/env python

import os
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys
import glob
from time import gmtime, strftime


recipients = ['me@gmail.com','you@yahoo.com'] 
emaillist = [elem.strip().split(',') for elem in recipients]
msg = MIMEMultipart()
msg['Subject'] = "[AutoSentry] Motion Detected at %s" % strftime("%Y-%m-%d %H:%M:%S", gmtime())
msg['From'] = 'myemail@gmail.com'
msg['Reply-to'] = 'myemail@gmail.com'
 
msg.preamble = 'Multipart massage.\n'
 
part = MIMEText("Motion Detected")
msg.attach(part)

os.chdir("./pics")
files = glob.glob("capture-*.jpg")
for f in files:
   app = open(f,"rb").read()
   part = MIMEApplication(app)
   part.add_header('Content-Disposition', 'attachment', filename=str(f))
   msg.attach(part)
   os.remove(f)

#app = open(str("../Camera/video.mp4"),"rb").read()
#part = MIMEApplication(app)
#part.add_header('Content-Disposition', 'attachment', filename=str("video.mp4"))
#msg.attach(part)
 
server = smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()
server.login("myemail@gmail.com", "mypassword")
 
server.sendmail(msg['From'], emaillist , msg.as_string())



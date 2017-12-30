#!/usr/bin/env python

import os
from subprocess import check_output
import subprocess
import socket
import fcntl
import struct
import glob

homeDir = "/home/pi/"
emailDir = "/home/pi/AutoSentry/Email"
cameraDir = "/home/pi/AutoSentry/Camera/picam"
pixDir = "/home/pi/AutoSentry/Camera/pix"
videoDir = "/home/pi/AutoSentry/Email/pics"

picamProcName = "picam"

def sendAlert():
   os.chdir(emailDir)
   os.system("./sendmail.py")


def checkPiCam():
   try:
      # Everything is good ie. Streamer process running
      pid = check_output(["pidof", picamProcName])
   except subprocess.CalledProcessError:
      # Streamer process has died
      os.chdir(cameraDir)
      os.system("./picam &")

def checkPics():
   os.chdir(pixDir)
   files = glob.glob("capture-*.jpg")
   hasImages = False
   for f in files:
      os.rename(f, "%s/%s" % (videoDir, f))
      hasImages = True
   return hasImages

def createVideo():
   os.chdir(videoDir)
   os.system("./convert.sh")
   os.rename("video.mp4", "../video.mp4")
   files = glob.glob("capture-*.jpg")
   for f in files:
      os.remove(f)

      
if __name__ == '__main__':
   checkPiCam()
   img = checkPics()
   if img:
      #createVideo()
      sendAlert()

#!/usr/bin/python3
import os  
import time 
import sys
import threading
import urllib.request
import logging
import subprocess

def checkwificonnection():
      try:
          networks = list(os.popen("ip address show | grep '{}' | grep 'inet'".format('wlan0')).read().split())
          network = {
            'method' : 'dynamic' if "dynamic" in networks else 'static',
            'ip' :  networks[networks.index('inet') + 1 ] 
          }
          logging.info("Wifi connected...")

      except ValueError as e:
          logging.info("Wifi not connected rebooting...")
          command = "/usr/bin/sudo /sbin/shutdown -r now"
          # process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
          # output = process.communicate()[0]
          # logging.info(output)
      try:
          with open("/home/pi/Desktop/config.txt") as f:
                data = f.read()
          url="google.com"
          if data:
            url = data
          else:
            url = "http://snapexpressbuffalo.com/index.php"
          urllib.request.urlopen(url)
          logging.info("Connected...")
          
      except:          
          logging.info("Url not responding rebooting...")
          command = "/usr/bin/sudo /sbin/shutdown -r now"
          # process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
          # output = process.communicate()[0]
          # logging.info(output)
               
     
    # do stuff...
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("Waiting for RPZW....")
    time.sleep(130)
    while True:
      checkwificonnection()
      time.sleep(5)

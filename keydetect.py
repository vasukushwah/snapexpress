#!/usr/bin/python3
import os
import subprocess
import time
import keyboard
import logging

def checkkey():
  try:
    if keyboard.is_pressed('Esc'):
      command="sudo systemctl stop connection.service"
      process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
      output = process.communicate()[0]
      logging.info(output)
      logging.info("Pressed")
      command="pkill -o chromium"
      process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
      output = process.communicate()[0]
      logging.info(output)
  except Exception as e:
      logging.info(e)

if __name__ == "__main__":
  format = "%(asctime)s: %(message)s"
  logging.basicConfig(format=format, level=logging.INFO,
                      datefmt="%H:%M:%S")
  while True:
    checkkey()
    time.sleep(0.1)


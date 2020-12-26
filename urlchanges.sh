
#!/bin/bash

value=`cat /home/pi/Desktop/config.txt`
@unclutter -idle 10
chromium-browser --noerrdialogs --disable-infobars --kiosk $value
The mod2 is the one that actually was used. I had to adapt and change the scripts from the older version because the parameters and scope of the project was changed half way through. 


To Setup The Pi:

1. Place a standard boot of Raspberrian onto an sd card. 
2. On that system download Apache.
3. Place current.xml and index.html file in this file location: /var/www/html
4. Place the MTConnectAdapterMod2 folder onto the Pi's Desktop.
5. Go to the Command Prompt and type "Sudo crontab -e"
6. In the crontab at the bottum copy and paste the content found in the crontab.txt file at the end of the content.
7. Restart the Pi.


To Restore The RPI3:

1. Place a standard boot of Raspberrian onto an sd card. 
2. On that system download Apache.
3. Place current.xml and index.html file in this file location: /var/www/html
4. Place the SaveData folder, the ConfirmationNumbers.txt, the python files and lastly the Shell files onto the Desktop.
5. Go to the Command Prompt and type "Sudo crontab -e"
6. In the crontab at the bottum copy and paste the content found in the crontab.txt file.

import os
import xml.etree.cElementTree as ET
import urllib.request
import shelve

PartCountfile = shelve.open("/home/pi/Desktop/SaveData/register")
if PartCountfile["execution"] != "ACTIVE":
	try:
	### grab data from url
		content = str(urllib.request.urlopen("http://192.168.200.25:915/").read())
		#print(content)
		PartCount = content.rsplit('PC2="',1)
		PartCount = PartCount[1]
		PartCount = PartCount.split('"',1)

		#find the base quantity for part count
		BaseQuantity = content.rsplit('BQ="',1)
		BaseQuantity = BaseQuantity[1].split('>',1)
		BaseQuantity = BaseQuantity[0].split('"',1)
		BaseQuantity = BaseQuantity[0]
		PartCountfile["BaseQuantity"] = BaseQuantity #store the base quantity


		### parse the data for the confirmation number
		ConfNumb = content.rsplit('CN="',1)
		ConfNumb = ConfNumb[1] 
		ConfNumb = ConfNumb.split('"',1)
		#print(ConfNumb[0])
		### read the previous confirmation number
		Myfile = open("/home/pi/Desktop/ConfirmationNumbers.txt","r+")
		prevConf= Myfile.readline()
		#print(prevConf)
		Myfile.close()
		### store the number 
		Myfile = open("/home/pi/Desktop/ConfirmationNumbers.txt","w")
		Myfile.write(ConfNumb[0])
		Myfile.write("\n")
		if ConfNumb[0] in prevConf:
			Myfile.write("0")
			#print("Same")
		else:
			Myfile.write("1")
			#print("New")
		Myfile.write("\n")
		Myfile.write(PartCount[0])
		Myfile.write("\n")
		Myfile.close()
	except:
		print("httpget.py: An Error has occurred");

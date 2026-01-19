import os
import xml.etree.cElementTree as ET
import urllib.request
import shelve

infile= shelve.open("/home/pi/Desktop/MTConnectAdapterMod2/SaveData/SAP_DATA")

try:
	### grab data from url
	content = str(urllib.request.urlopen("http://192.168.200.25:915/").read())
	#print(content) #debug
	PartCount = content.rsplit('PC2="',1)
	PartCount = PartCount[1]
	PartCount = PartCount.split('"',1)

	#find the base quantity for part count
	BaseQuantity = content.rsplit('BQ="',1)
	BaseQuantity = BaseQuantity[1].split('>',1)
	BaseQuantity = BaseQuantity[0].split('"',1)
	BaseQuantity = BaseQuantity[0]
	infile["BQ"] = BaseQuantity #store the base quantity

	### parse the data for the confirmation number
	ConfNumb = content.rsplit('CN="',1)
	ConfNumb = ConfNumb[1] 
	ConfNumb = ConfNumb.split('"',1)
	
	if ConfNumb[0] == "" or ConfNumb[0] in infile["CN"]:
		infile["NEW_Job"] = 0
		#print("Same") # debug
	else:
		infile["NEW_Job"] = 1
		infile["CN"] = ConfNumb[0]
		#print("New") # debug	
except:
	print("httpget.py: An Error has occurred");

#print(infile["BQ"]) # debug
#print(infile["CN"]) # debug
#print(infile["NEW_Job"]) # debug
infile.close()

import shelve
import os


infile = shelve.open("/home/pi/Desktop/MTConnectAdapterMod2/SaveData/SAP_DATA")

#infile["BQ"] = 0 # base quantity
#infile["CN"] = "" # confirmation number
#infile["NEW_Job"] = 0 # confirmation number

print(infile["BQ"])
print(infile["CN"])
print(infile["NEW_Job"])

import shelve
import os


# This file is for manually regulating the Saved data When needed.

#initialize the registry
infile = shelve.open("/home/pi/Desktop/MTConnectAdapterMod2/SaveData/register")

#infile["MachineStatus"] = "OFF"
#infile["mode"] = "MANUAL"
#infile["execution"] = "READY"
#infile["PartCount"] = 206
#infile["frame"] = 0
#infile["buffer"] = 0
#infile["io1"]= 0
#infile["io2"]= 0
#infile["io3"]= 0
#infile["io4"]= 0
#infile["io5"]= 0
#infile["io6"]= 0
#infile["io7"]= 0
#infile["io8"]= 0
#infile["trim"]= 0


print(infile["MachineStatus"])
print(infile["mode"])
print(infile["execution"])
print(infile["PartCount"])
print(infile["frame"])
print(infile["buffer"])
print(infile["io1"])
print(infile["io2"])
print(infile["io3"])
print(infile["io4"])
print(infile["io5"])
print(infile["io6"])
print(infile["io7"])
print(infile["io8"])
print(infile["trim"])

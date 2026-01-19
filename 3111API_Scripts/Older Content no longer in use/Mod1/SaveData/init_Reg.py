import shelve

#initialize the registry
infile = shelve.open("/home/pi/Desktop/SaveData/register")
#infile["pin8"] = 0
#infile["io8"] = 0
#infile["trigger"] = 1
#infile["PCcount"] = 0
#infile["counter"] = 0
#infile["BaseQuantity"] = 1
#infile["buffer"] = 0
#infile["frame"] = 0
#infile["Machinepartcount"] = 157
#infile["execution"]= "ACTIVE"


#print(infile["BaseQuantity"])
#print(infile["PCcount"])
#print(infile["trigger"])

#print(infile["Machinepartcount"])
#print(infile["execution"])
#print(infile["io8"])

trimfile = shelve.open("/home/pi/Desktop/SaveData/trimcut")

#trimfile["TrimCut"] = 1
trimfile["frame"] = 0

print(trimfile["TrimCut"])
print(trimfile["frame"])

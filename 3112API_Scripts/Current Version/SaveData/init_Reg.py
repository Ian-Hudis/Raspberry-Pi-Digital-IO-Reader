import shelve

#initialize the registry

infile = shelve.open("/home/pi/Desktop/SaveData/register")

#infile["BaseQuantity"] = 1
#infile["TrimCut"] = 0
#infile["pc"]= 0

print(infile["pc"])
print(infile["BaseQuantity"])
print(infile["TrimCut"] )

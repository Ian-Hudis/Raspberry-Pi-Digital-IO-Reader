#	Ian Hudis
#	2/28/2025

## Program for the agent ##
import os
from pathlib import Path
from datetime import datetime
import xml.etree.cElementTree as ET
import shelve # this is for the part count

def InitializeAgent(FilePath, time):
    SeqNum = 0
    Mainroot = ET.Element("MTConnnectStreams")
    Header = ET.SubElement(Mainroot, "Header", creationTime=str(time), sender="Amada Bandpi", instanceId="1", version="0.0.1.0", LastSequence=str(SeqNum))
    writeroot = ET.SubElement(Mainroot, "Streams")
    ComponentStreams = ET.SubElement(writeroot, "ComponentStream")
    #outputs
    doc1 = ET.SubElement(ComponentStreams,"Events")
    SeqNum += 1
    ET.SubElement(doc1, "MachineStatus", dataItemId="machinestatus", timestamp = str(time), sequence=str(SeqNum)).text = "off" ## 1
    SeqNum += 1
    ET.SubElement(doc1, "ControllerMode", dataItemId="mode", timeStamp = str(time), sequence=str(SeqNum)).text = "UNAVAILABLE" ## 2 - 3
    SeqNum += 1
    ET.SubElement(doc1, "Execution", dataItemId="execution", timestamp = str(time), sequence=str(SeqNum)).text = "UNAVAILABLE" ## 5
    SeqNum += 1
    #Myfile = open("ConfirmationNumbers.txt", "r+")
    #contentlines = (Myfile.readlines())
    #partcount = contentlines[2] 
    #Myfile.close()
    #print(partcount)


    ET.SubElement(doc1, "PartCount", dataItemId="PartCountAct", timestamp = str(time), sequence=str(SeqNum)).text = "0" #partcount ## 6 - 7

    #inputs
    doc2 = ET.SubElement(ComponentStreams, "Samples")
    SeqNum += 1
    ET.SubElement(doc2, "Frame", dataItemId="frame", timestamp = str(time), sequence=str(SeqNum)).text = "0"
    SeqNum += 1
    ET.SubElement(doc2, "Buffer", dataItemId="buffer", timestamp = str(time), sequence=str(SeqNum)).text = "0"
    SeqNum += 1
    ET.SubElement(doc2, "Sample1", dataItemId="IO1", timestamp = str(time), sequence=str(SeqNum)).text = "init"  
    SeqNum += 1
    ET.SubElement(doc2, "Sample2", dataItemId="IO2", timestamp = str(time), sequence=str(SeqNum)).text = "init"
    SeqNum += 1
    ET.SubElement(doc2, "Sample3", dataItemId="IO3", timestamp = str(time), sequence=str(SeqNum)).text = "init"  
    SeqNum += 1
    ET.SubElement(doc2, "Sample4", dataItemId="IO4", timestamp = str(time), sequence=str(SeqNum)).text = "init"  
    SeqNum += 1
    ET.SubElement(doc2, "Sample5", dataItemId="IO5", timestamp = str(time), sequence=str(SeqNum)).text = "init"  
    SeqNum += 1
    ET.SubElement(doc2, "Sample6", dataItemId="IO6", timestamp = str(time), sequence=str(SeqNum)).text = "init"  
    SeqNum += 1
    ET.SubElement(doc2, "Sample7", dataItemId="IO7", timestamp = str(time), sequence=str(SeqNum)).text = "init"      
    SeqNum += 1
    ET.SubElement(doc2, "Sample8", dataItemId="IO8", timestamp = str(time), sequence=str(SeqNum)).text = "init"      
    ##other
    doc0 = ET.SubElement(ComponentStreams,"Ref")
    ET.SubElement(doc0, "sequence", dataItemId = "seq", timestamp = str(time), sequence = str(SeqNum)).text = str(SeqNum)
    ET.SubElement(doc0, "timestamp", dataItemId = "time" , timestamp = str(time), sequence = str(SeqNum)).text = str(time)
    # export the MTConnect data
    tree = ET.ElementTree(Mainroot)
    tree.write(FilePath)

def VariableStatus(root, doc, Var, VarRoot, dataitemid, SeqNum, NewValue):
    prevValue = root.find(VarRoot).text 
    if str(NewValue) == prevValue:
        ET.SubElement(doc, Var, dataItemId=dataitemid, timestamp = str(root.find(VarRoot).get("timestamp")), sequence= root.find(VarRoot).get("sequence")).text = prevValue
    else: ## the value has changed
        SeqNum += 1
        ET.SubElement(doc, Var, DataItemId=dataitemid, timestamp = str(datetime.now()), sequence=str(SeqNum)).text = str(NewValue)
    return SeqNum

def UpdateAgent(FilePath, time, output0, output1, output2, output3, output4, output5, In1, In2, In3, In4, In5, In6, In7, In8):
    tree = ET.parse(FilePath)
    root = tree.getroot()

    SeqNum = eval(root.find("./Streams/ComponentStream/Ref/sequence").text) # get a value 

    Mainroot = ET.Element("MTConnnectStreams")
    Header = ET.SubElement(Mainroot, "Header", creationTime=str(time), sender="Amada Bandpi", instanceId="1", version="0.0.1.0", LastSequence=str(SeqNum))
    writeroot = ET.SubElement(Mainroot, "Streams")
    ComponentStreams = ET.SubElement(writeroot, "ComponentStream")
	
    #outputs
    doc1 = ET.SubElement(ComponentStreams,"Events")
    SeqNum = VariableStatus(root, doc1, "MachineStatus", "./Streams/ComponentStream/Events/MachineStatus", "machinestatus", SeqNum, output0)
    SeqNum = VariableStatus(root, doc1, "ControllerMode", "./Streams/ComponentStream/Events/ControllerMode", "mode", SeqNum, output1)
    SeqNum = VariableStatus(root,doc1,"Execution","./Streams/ComponentStream/Events/Execution","execution", SeqNum, output2)
    SeqNum = VariableStatus(root,doc1,"PartCount","./Streams/ComponentStream/Events/PartCount","PartCountAct", SeqNum, output3)


    #inputs
    doc2 = ET.SubElement(ComponentStreams, "Samples")
    SeqNum = VariableStatus(root, doc2, "Frame",   "./Streams/ComponentStream/Samples/Frame","frame", SeqNum, output4)
    SeqNum = VariableStatus(root, doc2, "Buffer",   "./Streams/ComponentStream/Samples/Buffer","buffer", SeqNum, output5)
    SeqNum = VariableStatus(root, doc2, "Sample1", "./Streams/ComponentStream/Samples/Sample1", "IO1", SeqNum, In1)
    SeqNum = VariableStatus(root, doc2, "Sample2", "./Streams/ComponentStream/Samples/Sample2", "IO2", SeqNum, In2)
    SeqNum = VariableStatus(root, doc2, "Sample3", "./Streams/ComponentStream/Samples/Sample3", "IO3", SeqNum, In3)
    SeqNum = VariableStatus(root, doc2, "Sample4", "./Streams/ComponentStream/Samples/Sample4", "IO4", SeqNum, In4)
    SeqNum = VariableStatus(root, doc2, "Sample5", "./Streams/ComponentStream/Samples/Sample5", "IO5", SeqNum, In5)
    SeqNum = VariableStatus(root, doc2, "Sample6", "./Streams/ComponentStream/Samples/Sample6", "IO6", SeqNum, In6)
    SeqNum = VariableStatus(root, doc2, "Sample7", "./Streams/ComponentStream/Samples/Sample7", "IO7", SeqNum, In7)
    SeqNum = VariableStatus(root, doc2, "Sample8", "./Streams/ComponentStream/Samples/Sample8", "IO8", SeqNum, In8)

    
    ##other
    doc0 = ET.SubElement(ComponentStreams,"Ref")
    #ET.SubElement(doc0, "sequence", dataItemId = "seq").text = str(SeqNum)
    #ET.SubElement(doc0, "timestamp", dataItemId = "time").text = str(time)
    ET.SubElement(doc0, "sequence", dataItemId = "seq", timestamp = str(time), sequence = str(SeqNum)).text = str(SeqNum)
    ET.SubElement(doc0, "timestamp", dataItemId = "time" , timestamp = str(time), sequence = str(SeqNum)).text = str(time)

    # export the MTConnect data
    tree = ET.ElementTree(Mainroot)
    tree.write(FilePath)
    # prevents an eventual error
    if SeqNum > 2000000000:
        SeqNum = 0

## Program for the adapter ##
import RPi._GPIO as GPIO
import time

def Find(input):
    if input==1:
        return 0
    else:
        return 1

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(8, GPIO.IN)
#GPIO.setup(7, GPIO.IN)

# MTConnect Adapter grabs the information from the GPIO
io1 = Find(GPIO.input(17)) ## machine on/off
io2 = Find(GPIO.input(27)) ##mode
io3 = Find(GPIO.input(22)) ##mode
io4 = Find(GPIO.input(23)) ## mode
io5 = Find(GPIO.input(24)) ## machine execution
io6 = Find(GPIO.input(25))## vice clamp grip
io7 = Find(GPIO.input(8)) ## vice clamp let grip

PartCountfile = shelve.open("/home/pi/Desktop/SaveData/register")
TrimFile = shelve.open("/home/pi/Desktop/SaveData/trimcut")
#io8 = (PartCountfile["io8"]) #Find(GPIO.input(7))  ## for part count bottom sensor
io8 = PartCountfile["PCcount"] # the io8 signal is fast so this is the delayed version of it for display purposes

## translate the gpio logic to mtconnect ##

# machine on
if io1 == 0:
	MachineStatus = "OFF"
else:
	MachineStatus = "ON"

## mode
if io2 == 1:
    mode = "SEMI-AUTOMATIC" # SingleCycle
elif io3 == 1:
    mode = "AUTOMATIC"      # AutoCycle"
elif io2 == 0 and io3 == 0:
    mode = "MANUAL"			# manual
else:
    mode = "UNAVAILABLE"    
    
## execution

if io5 == 1: # blade is on
    execution = "ACTIVE"
    PartCountfile["buffer"] = 0 
elif PartCountfile["buffer"]<30 and i05 == 0 and execution == "ACTIVE": #blade is not on, wait 30 seconds 
    #execution = "ACTIVE"
    PartCountfile["buffer"] += 1
else: # after 30 seconds declare it as idle
    execution = "READY"
    #PartCountfile["buffer"] = 0 

PartCountfile["execution"] = execution



## Part Count
Frameup = TrimFile["frame"]
MachinePartCount = PartCountfile["Machinepartcount"]

## Part Count Trim Cut activate
if mode == "MANUAL" and io6 == 0 and TrimFile["TrimCut"]  == 0: # machine is in manual and the clamp is open
    TrimFile["TrimCut"] = 1
    print(str(datetime.now()) + " Trim Cut Activated ")

## part count using the Clamps (original method) ##
#if io3 == 1 and io6 == 0 and Frameup == 0: # Frame has gone all the way down while the blade is on and in automatic
#	MachinePartCount += 1 ## add to the number
#	Frameup = 1
#elif io5 == 1:
#	Frameup = 0  
	
## part count using the frame down signal using the subroutine ##
if PartCountfile["PCcount"] == 1 and execution == "ACTIVE" and Frameup == 0:  # cyclecount
	if TrimFile["TrimCut"] == 1:
		#BQ = int(PartCountfile["BaseQuantity"]) #get the base quantity
		print(str(datetime.now()) + " Trim Cut Complete")
	else: # trim cu
		BQ = int(PartCountfile["BaseQuantity"]) #get the base quantity
		MachinePartCount += BQ ## add to the base quantity to the part count
		print(str(datetime.now()) + " Part " + str(MachinePartCount)  + " Complete;")
	Frameup = 5

if Frameup > 1:  # delay
    Frameup -= 1 
    TrimFile["TrimCut"] = 0 # turn the trim cut off after the 1st part
if Frameup == 1: # reset trigger
    print(str(datetime.now()) + " Reset the pcsig;")
    TrimFile["TrimCut"] = 0 # make sure the trim cut gets turned off
    PartCountfile["PCcount"] = 0 # reset the trigger
    Frameup = 0
	
#if execution != "ACTIVE":
#    Frameup = 0
#    PartCountfile["PCcount"] = 0 # reset the trigger

if io3 == 0 or io1 == 0:
    Frameup = 0
    PartCountfile["PCcount"] = 0 # reset the trigger
	
	
## see if there is a new job
try:
    Myfile = open("/home/pi/Desktop/ConfirmationNumbers.txt", "r+") # grab the httpgrab data from a txt file 
    NewJob = int(Myfile.read(9)[8:9])
    Myfile.close()  #print(NewJob)
except:
    NewJob = 0
    print("ConfirmationNumbers.txt not found")

if NewJob == 1: # zero the part count for a new job
    MachinePartCount = 0
    

TrimFile["frame"] = Frameup # store the frame value
PartCountfile["Machinepartcount"] = MachinePartCount # store the part count


filepath = "/var/www/html/current.xml"
my_file = Path(filepath)

## Update the MtConnect Agent ##
if my_file.is_file():
	#tree = ET.parse("/var/www/html/current.xml")
	#root = tree.getroot()

   # print("<Updating Agent>")
	try:
		UpdateAgent(filepath, datetime.now(), MachineStatus, mode, execution, MachinePartCount, Frameup, PartCountfile["buffer"], io1, io2, io3, io4, io5, io6, io7, io8)
	except:
		os.system("sudo rm /var/www/html/current.xml") # get rid of the file if corrupt
else:     #file doesnt exist
	print("<Making the Agent>")
	InitializeAgent(filepath, datetime.now()) 

## Program for the agent ##
import os
from pathlib import Path
from datetime import datetime
import xml.etree.cElementTree as ET
import shelve

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


    ET.SubElement(doc1, "PartCount", dataItemId="PartCountAct", timestamp = str(time), sequence=str(SeqNum)).text = 0#partcount ## 6 - 7

    #inputs
    doc2 = ET.SubElement(ComponentStreams, "Samples")
    SeqNum += 1
    ET.SubElement(doc2, "Frame", dataItemId="frame", timestamp = str(time), sequence=str(SeqNum)).text = "UNAVAILABLE" ## 6 - 7
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

def UpdateAgent(FilePath, time, output0, output1, output2, output3, output4, In1, In2, In3, In4, In5, In6, In7, In8):
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
    SeqNum = VariableStatus(root,doc2,"Frame","./Streams/ComponentStream/Samples/Frame","frame", SeqNum, output4)
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
GPIO.setup(7, GPIO.IN)

# MTConnect Adapter grabs the information from the GPIO
io1 = Find(GPIO.input(17)) ## machine on/off
io2 = Find(GPIO.input(27)) ##mode
io3 = Find(GPIO.input(22)) ##mode
io4 = Find(GPIO.input(23)) ## mode
io5 = Find(GPIO.input(24)) ## machine execution
io6 = Find(GPIO.input(25))## for part count
io7 = Find(GPIO.input(8)) ## for part count
io8 = 0 #Find(GPIO.input(7))  ## Unused

## translate the gpio logic to mtconnect ##



# machine on
if io1 == 0:
	MachineStatus = "OFF"
else:
	MachineStatus = "ON"


## mode
if io2 == 1:
	mode = "MANUAL" # manual
elif io3 == 1:
	mode = "AUTOMATIC"      # automatic for running
elif io2 == 0 and io3 == 0:
	mode = "UNAVAILABLE" #BLADE_CHANGE"			# Tool Change
else:
	mode = "UNAVAILABLE"    #
	
## execution
if io5 == 1: # red blade light is on
	execution = "ACTIVE"
else: # red blade light is off and the red warning light is off
	execution = "READY"

### partcount
try: # find the previous number
	tree = ET.parse("/var/www/html/current.xml")
	root = tree.getroot()
	Frameup = int(root.find("./Streams/ComponentStream/Samples/Frame").text)
	MachinePartCount = int(root.find("./Streams/ComponentStream/Events/PartCount").text)
except:
	Frameup =0
	MachinePartCount = 0
	

## Part Count
PartCountfile = shelve.open("/home/pi/Desktop/SaveData/register")
if mode != "AUTOMATIC" and io6 == 1: # the machine frame gets raised while in manual
	PartCountfile["TrimCut"] = 1


if io7 == 1 and Frameup == 0 and io3 == 1 and io5 == 1: # the frame lowers while running parts
	Frameup = 1
	
if io6 == 1 and Frameup == 1 and io3 == 1 and io5 == 1: # Frame raises while still in automatic
	Frameup = 2
	

if Frameup == 2 and io3 == 1 and PartCountfile["TrimCut"] == 1: #Frame is going back up after a part is completed
	PartCountfile["TrimCut"] = 0 # skips the trim cut
	Frameup = 0
	print("Trim Cut;")
elif Frameup == 2 and io3 == 1 and PartCountfile["TrimCut"] == 0: # count parts after the trim cut
	BQ = int(PartCountfile["BaseQuantity"])
	MachinePartCount += BQ ## add to the number
	Frameup = 0
	print("Part " + str(MachinePartCount) + " complete;")

if io3 == 0 or io5 == 0: #  no longer in automatic
	Frameup = 0	

#elif Frameup == 2 and MachinePartCount == 0:
#	MachinePartCount += 1 ## add to the number
#	Frameup = 0

## see if there is a new job
try:
	Myfile = open("/home/pi/Desktop/ConfirmationNumbers.txt", "r+")
	NewJob = int(Myfile.read(9)[8:9])
	Myfile.close()  #print(NewJob)
except:
	NewJob = 0
	print("ConfirmationNumbers.txt not found")

if NewJob == 1: # zero the part count for a new job
	MachinePartCount = 0
	
# Update the MtConnect Agent
filepath = "/var/www/html/current.xml"
my_file = Path(filepath)
if my_file.is_file():
   # print("<Updating Agent>")
   try:
       UpdateAgent(filepath, datetime.now(), MachineStatus, mode, execution, MachinePartCount, Frameup, io1, io2, io3, io4, io5, io6, io7, io8)
   except:
       os.system("sudo rm /var/www/html/current.xml") # get rid of the file if corrupt
else:     #file doesnt exist
    print("<Making the Agent>")
    InitializeAgent(filepath, datetime.now())


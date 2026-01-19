#	Ian Hudis
#	8/28/2025

## Program for the agent ##
import os
from pathlib import Path
from datetime import datetime
import xml.etree.cElementTree as ET
import shelve # this is for the part count
import time

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
    SeqNum += 1
    ET.SubElement(doc2, "Trim", dataItemId="TrimCut", timestamp = str(time), sequence=str(SeqNum)).text = "init"      
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

def UpdateAgent(FilePath, time, output0, output1, output2, output3, output4, output5, In1, In2, In3, In4, In5, In6, In7, In8, trim):
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
    SeqNum = VariableStatus(root, doc2, "Trim", "./Streams/ComponentStream/Samples/Trim", "TrimCut", SeqNum, trim)
    
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


##! Grab the values from the register
File = shelve.open("/home/pi/Desktop/MTConnectAdapterMod2/SaveData/register")

MachineStatus = File["MachineStatus"]
Mode = File["mode"]
Execution = File["execution"]
MachinePartCount = File["PartCount"]
Frameup = File["frame"]
Buffer = File["buffer"]
io1 = File["io1"]
io2 = File["io2"]
io3 = File["io3"]
io4 = File["io4"]
io5 = File["io5"]
io6 = File["io6"]
io7 = File["io7"]
io8 = File["io8"]
trim = File["trim"]
File.close()
##! Grab the values from the register

##! Update the MtConnect Agent ##
filepath = "/var/www/html/current.xml"
my_file = Path(filepath)

if my_file.is_file():
	#tree = ET.parse("/var/www/html/current.xml")
	#root = tree.getroot()
   # print("<Updating Agent>")
	try:
		UpdateAgent(filepath, datetime.now(), MachineStatus, Mode, Execution, MachinePartCount, Frameup, Buffer, io1, io2, io3, io4, io5, io6, io7, io8, trim)
	except:
		os.system("sudo rm /var/www/html/current.xml") # get rid of the file if corrupt
else:     #file doesnt exist
	print("<Making the Agent>")
	InitializeAgent(filepath, datetime.now()) 
##! Update the MtConnect Agent ##

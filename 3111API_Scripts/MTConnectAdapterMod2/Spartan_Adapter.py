#	Ian Hudis
#	8/28/2025

## Program for the adapter ##
import os
from pathlib import Path
from datetime import datetime
import shelve # this is for the part count
import RPi._GPIO as GPIO
import time

def Find(input):
    if input==1:
        return 0
    else:
        return 1

##! READ the values from the register
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
##! READ the values from the register

##! READ the values from the SAP register
SAP_File = shelve.open("/home/pi/Desktop/MTConnectAdapterMod2/SaveData/SAP_DATA")
BaseQuantity = SAP_File["BQ"] # tells amount of parts done per cycle
NewJob = SAP_File["NEW_Job"] #  tells that a new job has been entered into the kiosk
SAP_File.close()
##! READ the values from the SAP register

# Setup for the hardware reading
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN) # io1
GPIO.setup(27, GPIO.IN) # io2
GPIO.setup(22, GPIO.IN) # io3
GPIO.setup(23, GPIO.IN) # io4
GPIO.setup(24, GPIO.IN) # io5
GPIO.setup(25, GPIO.IN) # io6
GPIO.setup(8, GPIO.IN)  # io7
GPIO.setup(7, GPIO.IN)  # io8

# MTConnect Adapter grabs the information from the GPIO
io1 = Find(GPIO.input(17)) ## machine on/off
io2 = Find(GPIO.input(27)) ## mode: Manual
io3 = Find(GPIO.input(22)) ## mode: Automatic
io4 = Find(GPIO.input(23)) ## mode
io5 = Find(GPIO.input(24)) ## machine execution
io6 = Find(GPIO.input(25))## vice clamp grip
io7 = Find(GPIO.input(8)) ## vice clamp let grip
io8 = Find(GPIO.input(7)) ## push button under frame

# machine on
if io1 == 0:
	MachineStatus = "OFF"
else:
	MachineStatus = "ON"

## mode
if io2 == 1:
    Mode = "SEMI-AUTOMATIC" # SingleCycle
elif io3 == 1:
    Mode = "AUTOMATIC"      # AutoCycle"
elif io2 == 0 and io3 == 0:
    Mode = "MANUAL"			# manual
else:
    Mode = "UNAVAILABLE"   

## execution
if io5 == 1: # blade is on
    Execution = "ACTIVE"
    Buffer = 0
    if Frameup == 1:
     Frameup = 0
     print(str(datetime.now()) + " Blade Reactivated")
elif Buffer < 15 and io5 == 0 and Execution == "ACTIVE": #blade is not on, wait 30 seconds 
    Buffer+= 1
else: # after 30 seconds declare it as idle
    Execution = "READY"

## Part Count Trim Cut activate
if Mode == "MANUAL" and io6 == 0 and trim  == 0: # machine is in manual and the clamp is open
    trim = 1
    print(str(datetime.now()) + " Trim Cut Activated ")

# zero the part count if its a new job
if (NewJob == 1):
    MachinePartCount = 0
    print(str(datetime.now()) + " Starting New Job! -> "+ str(MachinePartCount))

##! reading the push button for part count while the machine is running
while (io1 == 1 and io2 == 0 and io5 == 1):
	# MTConnect Adapter grabs the information from the GPIO
	io1 = Find(GPIO.input(17)) ## machine on/off
	io2 = Find(GPIO.input(27)) ## mode: Manual
	io3 = Find(GPIO.input(22)) ## mode: Automatic
	io4 = Find(GPIO.input(23)) ## mode
	io5 = Find(GPIO.input(24)) ## machine execution
	io6 = Find(GPIO.input(25))## vice clamp grip
	io7 = Find(GPIO.input(8)) ## vice clamp let grip
	io8 = Find(GPIO.input(7)) ## push button under frame
	
	if io8 == 1 and trim == 0 and Frameup == 0: # the frame down sensor is pressed
		try:
		    MachinePartCount += int(BaseQuantity) # count the part by the increment
		except:
		    MachinePartCount += 1 # count the part by the increment
		print(str(datetime.now()) + " Button Pressed -> "+ str(MachinePartCount))	 # just for debug
		Frameup = 1
		break
	elif io8 == 1 and trim == 1 and Frameup == 0: # the frame down sensor is pressed	
		trim = 0
		print(str(datetime.now()) + " Trim Cut Complete -> "+ str(MachinePartCount))	 # just for debug
		Frameup = 1
		break
	time.sleep(0.05)
##! reading the push button for part count while the machine is running

##! Write the Values into the register
outputFile = shelve.open("/home/pi/Desktop/MTConnectAdapterMod2/SaveData/register")
outputFile["MachineStatus"] = MachineStatus
outputFile["mode"] = Mode
outputFile["execution"] = Execution 
outputFile["PartCount"] = MachinePartCount 
outputFile["frame"] = Frameup
outputFile["buffer"] = Buffer
outputFile["io1"] = io1
outputFile["io2"] = io2
outputFile["io3"] = io3
outputFile["io4"] = io4
outputFile["io5"] = io5
outputFile["io6"] = io6
outputFile["io7"] = io7
outputFile["io8"] = io8
outputFile["trim"] = trim
File.close()
##! Write the Values into the register

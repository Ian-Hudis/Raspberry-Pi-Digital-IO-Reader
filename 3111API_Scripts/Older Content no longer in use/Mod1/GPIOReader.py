import shelve

def Find(input):
	if input == 1:
		return 0
	else:
		return 1		

Now = datetime.now() 
myfile = shelve.open("/home/pi/Desktop/SaveData/register")

if myfile["execution"]=="ACTIVE": # machine running
	if(myfile["PCcount"] == 0):	# dont bother reading the button if the machine isnt in the right conditions.
			
		if myfile["trigger"] == 0:
			myfile["trigger"] = 1
			print(str(Now) + " GPIOReader scanning...") # just for debug	
			
		GPIO.setmode(GPIO.BCM)
		
		GPIO.setup(7, GPIO.IN)
		
		counter = 0
		
		while True:
			
			io8 = Find(GPIO.input(7)) ## down button	
			if io8 == 1: # the frame down sensor is pressed	
				myfile["PCcount"] = 1 #signal to the adapter that it needs to count a part 
				print(str(Now) + " Button Pressed")	 # just for debug
				break
			
			if counter > 14000:
				print(str(Now) + " Session Expired")	 # just for debug
				break
			counter += counter
			time.sleep(0.04) # 40 ms wait
	else:	# Wait for the xmltest.py file to read the PCcount signal
		if myfile["trigger"] == 1: # the adapter has read the down sensor is pressed
			myfile["trigger"] = 0
			print(str(Now) + " Wait for Count")	# just for debug
		#time.sleep(5) # acts as a delay to allow the xmltest.py to do other tasks so this program doesnt interrupt it.

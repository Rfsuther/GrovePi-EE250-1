""" EE 250L Lab 02: GrovePi Sensors
List team members here.
Insert Github repository link here.
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages
The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi

from grove_rgb_lcd import *

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
    ultPrt = 4    # D4 is the port for ultrasonic  ranger
    potPrt = 0 #A0 is the potentiometer port



grovepi.pinMode(potPrt,"INPUT")


full_distance = 517



count = 0

##MAIN
while True:
	#So we do not poll the sensors too quickly which may introduce noise,
	#sleep for a reasonable time of 200ms between each iteration.
	time.sleep(0.2)

	#ultIN = grovepi.ultrasonicRead(PORT)
	potIN = grovepi.analogRead(potPrt)
	distIN = grovepi.ultrasonicRead(ultPrt)
	

	# if count < 10:
	# 	setText(f"Hello world\nLCD test {count}")
	# 	setRGB(0,128,64)
	# 	count += 1
	# 	time.sleep(0.01)

	# elif (10 <= count and count <= 20) :
	# 	setText(f"Goodbyeeee\nLCD test {count}")
	# 	setRGB(128,0,64)
	# 	count += 1
	# else:
	# 	count=0
	# 	time.sleep(0.01)
	# 	setText(f"error")
	# 	count += 1




#cd /home/pi/GrovePi-EE250-1/ee250/lab02

# if oldThresh != newThresh set the buffer clear


	dist2obj = int(distIN)

	newThresh = int(517*(potIN/1023))


	if dist2obj < newThresh:                   #   object
		setRGB(255,10,10) #Sets red (R,G,B)
		setText_norefresh(f"{newThresh}cm OBJ PRES\n{dist2obj}cm")



	else:                           # no object
		setRGB(10,255,10) #SET TO GREEN

		setText_norefresh(f"{newThresh}cm         \n{dist2obj}cm")


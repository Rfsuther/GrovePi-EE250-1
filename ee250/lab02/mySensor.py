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


    print("Pot val =  ", potIN)
    print("Ultra val = " , grovepi.ultrasonicRead(ultPrt))
    # if oldThresh != newThresh




	if count < 100:

		setText("Hello world\nLCD test")
		setRGB(0,128,64)
		count += 1
		time.sleep(0.1)

	else if 100<count and count <200:

		setText("Goodbyeeee\nLCD test")
		setRGB(128,0,64)
		count += 1
	else:
		count=0
		time.sleep(0.1)










    # if ...:                            #   object
    # 	setRGB(255,10,20) #Sets red (R,G,B)
    # 	setText_norefresh("Set text here A {}...".format(str(X)) )



    # else...:                           # no object
    # 	setRGB(10,255,30) #SET TO GREEN

    # 	setText_norefresh("Set text here B {}...".format(str(Y)) )


   	# (.....BUFFFER CLEAR)

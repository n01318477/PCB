#!/usr/bin/python3
import sys
import os
from time import sleep

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

def turnoff():
    GPIO.output(PIN_17, GPIO.LOW)    # Turn OFF the LED connected to GPIO 17.
    print ('LED is off')
    return

def turnon():
    GPIO.output(PIN_17, GPIO.HIGH)    # Turn ON the LED connected to GPIO 17.
    print ('LED is on')
    return

def buttonDetect(channel):
    if GPIO.input(27):
        turnon()
    else:
        turnoff()

def main():
    global PIN_17
    global PIN_18
    global GPIO_Chan_List

    print ('Welcome to my LED demo')
    GPIO.setmode(GPIO.BCM)   # use this BCM (Board GPIO number) instead of using Board Pin numbers.
    GPIO.setwarnings(False)

    GPIO.setup(27, GPIO.IN)  #Initialize pin 27 as an input
    GPIO.setup(17, GPIO.OUT) #set up pin 17 as an output

    GPIO.add_event_detect(27,GPIO.BOTH,callback=buttonDetect) #detect rising and falling edge

    message = input("Press enter to quit at any time\n\n")

    GPIO.cleanup()
	
if __name__ == "__main__":
  main()

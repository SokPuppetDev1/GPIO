
import RPi.GPIO as GPIO
import time              #imports

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  #pin setup

ledout=18
buttonin=5

GPIO.setup(ledout,GPIO.OUT)   #pin config
GPIO.setup(buttonin,GPIO.IN)
led=0
GPIO.output(ledout,led)

while True:
    if GPIO.input(buttonin)==GPIO.HIGH:
        if led==0:
            led=1
            GPIO.output(ledout,led)
            time.sleep(1)
        else:
            led=0
            GPIO.output(ledout,led)
            time.sleep(1)

import RPi.GPIO as GPIO
import time              #imports

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  #pin setup

GPIO.setup(18,GPIO.OUT)   #pin config

while True:
    GPIO.output(18,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(18,GPIO.LOW)
    time.sleep(0.5)

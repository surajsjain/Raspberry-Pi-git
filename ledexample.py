import RPi.GPIO as GPIO
import time

##setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

##code
for i in range(1,10):
    GPIO.output(18, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(18, GPIO.LOW)
    time.sleep(1)

GPIO.cleanup()

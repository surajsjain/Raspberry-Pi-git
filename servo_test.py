import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(7, GPIO.OUT)
servo=GPIO.PWM(7, 50)
servo.start(2.0)

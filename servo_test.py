import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(07, GPIO.OUT)
servo=GPIO.PWM(07, 50)
servo.ChangeDutyCycle(50)

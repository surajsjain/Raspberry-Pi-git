import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(07, GPIO.OUT)
servo=GPIO.PWM(07, 50)
servo.start(2.0)

def SetAngle(angle):
    duty = angle / 18 + 2
	GPIO.output(07, True)
	servo.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(07, False)
	pwm.ChangeDutyCycle(0)

SetAngle(90)

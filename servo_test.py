import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def servo(pin, angle):
	GPIO.setup(pin, GPIO.OUT)
	pwm=GPIO.PWM(pin, 50)
	p=angle*0.055555
	p=p+2.5
	pwm.start(p)
	time.sleep(0.25)
	pwm.stop()

ang=input("Enter the angle: ")
servo(17, ang)
GPIO.cleanup()

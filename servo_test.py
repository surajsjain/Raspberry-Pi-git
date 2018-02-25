import time
import RPi.GPIO as gpio
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.OUT)
pwm=gpio.PWM(7, 50)
pwm.start(5)
for x in range (0,7):
    pwm.ChangeDutyCycle(x)
    time.sleep(0.5)
gpio.cleanup()
pwm.stop

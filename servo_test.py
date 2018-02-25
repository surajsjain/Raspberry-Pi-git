import time
import RPi.GPIO as gpio
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.OUT)
gpio.output(7, True)
time.sleep(0.0015)
gpio.output(7, False)
'''
pwm = gpio.PWM(7,100)
pwm.start(2.5)
def change(k):
    pwm.ChangeDutyCycle(k)
    time.sleep(1)

try:
    while True:
        k = float(raw_input("enter angle: "))
        k = (1+(float(k)/180))/20
        change(k)
except KeyboardInterrupt:
    pwm.stop()
    gpio.cleanup()
    exit
'''

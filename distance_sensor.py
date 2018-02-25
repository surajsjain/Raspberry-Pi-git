import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

trig=4
echo=18

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

print "Enter 1 to stop the program"
while(True):

    GPIO.output(trig, True)
    time.sleep(0.0001)
    GPIO.output(trig, False)

    while GPIO.input(echo) == False:
        start=time.time()

    while GPIO.input(echo) == True:
        end=time.time()

    sig_time= end-start

    distance= sig_time/0.000058
    time.sleep(0.5)
    print "distance"+str(distance)
    GPIO.cleanup()

GPIO.cleanup()

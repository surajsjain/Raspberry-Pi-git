
########## Program 1 ###########
'''
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)
servo=GPIO.PWM(17, 50)
servo.start(3)
time.sleep(3)
servo.ChangeDutyCycle(7.5)
servo.stop()
GPIO.cleanup()

'''

########## Program 2 ###########
'''
# This gives us control of the Raspberry Pi's pins.
import RPi.GPIO as GPIO

# This is only used for time delays... standard Python stuff.
import time

# Tell i which pin number we'll  be using to refer to the GPIO pains.
# We will use the physical pin ordering.
GPIO.setmode(GPIO.BOARD)

# We will tell the Broadcom CPU which pins do what.
# There are many pins and most have up to 5 different functions,
# each with a default.  Check the pinout to find non-specialized
# "GPIO" pins.  We'll use P!-Pin_11 (using BOARD reference),
# which is the same as GPIO17 (Broadcom / BCM reference).
# We need our pin to use the GPIO digital output function, so we just
# tell it to designate this pin for OUTPUT.
pin_number = 17
GPIO.setup(pin_number, GPIO.OUT)

# Now we can use PWM on pin 11.  It's software PWM, so don't expect perfect
# results.  Linux is a multitasking OS so other processes could interrupt
# the process which generate the PWM signal at any time.
# Raspberry Pi has a hardware PWm channel, but this Pythong library
# does not yet support it.
frequency_hertz = 50
pwm = GPIO.PWM(pin_number, frequency_hertz)


# How to position a servo?  All servos are pretty much the same.
# Send repeated purses of an absolute duration (not a relative duty cycle)
# between 0.40 ms and 2.5 ms in duration.  A single pulse will only move it
# a short distance in the desired direction.  Repeated pulses will continue
# its movement and then once it arrives at the specified position it will
# insruct the motor to forcefully hold its position.
left_position = 0.40
right_position = 2.5
middle_position = (right_position - left_position) / 2 + left_position

# I'll store a sequence of positions for use in a loop later on.
positionList = [left_position, middle_position, right_position, middle_position]

# total number of milliseconds in a a cycle.  Given this, we will then
# know both how long we want to pulse in this cycle and how long tghe
# cycle itself is.  That is all we need to calculate a duty cycle as
# a percentage.
ms_per_cycle = 1000 / frequency_hertz

# Iterate through the positions sequence 3 times.
for i in range(3):
	# This sequence contains positions from left to right
	# and then back again.  Move the motor to each position in order.
	for position in positionList:
		duty_cycle_percentage = position * 100 / ms_per_cycle
		print("Position: " + str(position))
		print("Duty Cycle: " + str(duty_cycle_percentage))
		print("")
		pwm.start(duty_cycle_percentage)
		time.sleep(.5)


# Done.  Terminate all signals and relax the motor.
pwm.stop()

# We have shut all our stuff down but we should do a complete
# close on all GPIO stuff.  There's only one copy of real hardware.
# We need to be polite and put it back the way we found it.
GPIO.cleanup()
'''

##### Program 3 ########


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
servo_pin=17
GPIO.setup(servo_pin, GPIO.OUT)

p = GPIO.PWM(servo_pin, 50)

p.start(7.5)

try:
        while True:
		p.ChangeDutyCycle(7.5)  # turn towards 90 degree
		time.sleep(3)
		p.ChangeDutyCycle(2.5)  # turn towards 0 degree
		time.sleep(3)
		p.ChangeDutyCycle(12.5) # turn towards 180 degree
        time.sleep(3)
except KeyboardInterrupt:
	p.stop()
        GPIO.cleanup()

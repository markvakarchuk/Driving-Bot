import RPi.GPIO as GPIO        # import RPi.GPIO module  
import time
from clr import clear

 #set GPIO mode to BOARD  
# GPIO.setmode(GPIO.BOARD)      
# GPIOsetup = False

# #set pinouts of motors
# #if PinA is HIGH & PinB is LOW motor spins forward 
motorL_pinA = 31    
motorL_pinB = 33
motorR_pinA = 35
motorR_pinB = 37

class robot():
    global motorL_pinA
    global motorL_pinB
    global motorR_pinA
    global motorR_pinB

    def __init__(self):
        global GPIOsetup
        GPIOsetup = False
        print("GPIO setup: " + str(GPIOsetup))
        if not GPIOsetup:
            print("GPIO initalizing")
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(motorL_pinA, GPIO.OUT)          
            GPIO.setup(motorR_pinA, GPIO.OUT)         
            GPIO.setup(motorR_pinB, GPIO.OUT)
            GPIO.setup(motorL_pinB, GPIO.OUT)
            GPIOsetup = True
            print("GPIO setup: " + str(GPIOsetup))
    
    def forward(self):
        GPIO.output(motorL_pinA, 0)         
        GPIO.output(motorR_pinB, 0)
        GPIO.output(motorL_pinB, 1)         
        GPIO.output(motorR_pinA, 1)
    
    def backward(self):
        GPIO.output(motorL_pinA, 1)         
        GPIO.output(motorR_pinB, 1)
        GPIO.output(motorL_pinB, 0)         
        GPIO.output(motorR_pinA, 0)
    
    def left(self):
        GPIO.output(motorL_pinA, 0)         
        GPIO.output(motorR_pinB, 0)
        GPIO.output(motorL_pinB, 1)         
        GPIO.output(motorR_pinA, 0)
    
    def right(self):
        GPIO.output(motorL_pinA, 0)         
        GPIO.output(motorR_pinB, 0)
        GPIO.output(motorL_pinB, 0)         
        GPIO.output(motorR_pinA, 1)

    def cw(self):
        GPIO.output(motorL_pinA, 1)         
        GPIO.output(motorR_pinB, 0)
        GPIO.output(motorL_pinB, 0)         
        GPIO.output(motorR_pinA, 1)

    def ccw(self):
        GPIO.output(motorL_pinA, 0)         
        GPIO.output(motorR_pinB, 1)
        GPIO.output(motorL_pinB, 1)         
        GPIO.output(motorR_pinA, 0)
    
    def stop(self):
        GPIO.output(motorL_pinA, 0)         
        GPIO.output(motorR_pinB, 0)
        GPIO.output(motorL_pinB, 0)         
        GPIO.output(motorR_pinA, 0)

    def quit (self):
        GPIO.output(motorL_pinA, 0)         
        GPIO.output(motorR_pinB, 0)
        GPIO.output(motorL_pinB, 0)         
        GPIO.output(motorR_pinA, 0)
        clear()
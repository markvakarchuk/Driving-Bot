import RPi.GPIO as GPIO        # import RPi.GPIO module  
import time

GPIO.setmode(GPIO.BOARD)       # set GPIO mode to BOARD  
GPIO.setup(31, GPIO.OUT)          
GPIO.setup(33, GPIO.OUT)         
GPIO.setup(35, GPIO.OUT)         
GPIO.setup(37, GPIO.OUT)

def run():
    #forward
    GPIO.output(31, 0)         
    GPIO.output(37, 0)
    GPIO.output(33, 1)         
    GPIO.output(35, 1)
    time.sleep(1)
    #forward
    GPIO.output(31, 0)         
    GPIO.output(37, 0)
    GPIO.output(33, 0.5)         
    GPIO.output(35, 0.5)
    time.sleep(1)
    #LEFT turn -- right motor forward
    GPIO.output(31, 0)         
    GPIO.output(37, 0)
    GPIO.output(33, 1)         
    GPIO.output(35, 0)
    time.sleep(1)

    #RIGHT turn -- left motor forward
    GPIO.output(31, 0)         
    GPIO.output(37, 0)
    GPIO.output(33, 0)         
    GPIO.output(35, 1)
    time.sleep(1)

    #backward
    GPIO.output(31, 1)         
    GPIO.output(37, 1)
    GPIO.output(33, 0)         
    GPIO.output(35, 0)
    time.sleep(1)

    #clockwise
    GPIO.output(31, 1)         
    GPIO.output(37, 0)
    GPIO.output(33, 0)         
    GPIO.output(35, 1)
    time.sleep(1)

    #counter clockwise
    GPIO.output(31, 0)         
    GPIO.output(37, 1)
    GPIO.output(33, 1)         
    GPIO.output(35, 0)
    time.sleep(1)

run()
GPIO.cleanup()
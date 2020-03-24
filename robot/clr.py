import RPi.GPIO as GPIO 

def clear():
    GPIO.setmode(GPIO.BOARD) 

    GPIO.setup(31, GPIO.OUT)          
    GPIO.setup(33, GPIO.OUT)         
    GPIO.setup(35, GPIO.OUT)         
    GPIO.setup(37, GPIO.OUT)

    GPIO.output(31, 0)         
    GPIO.output(37, 0)
    GPIO.output(33, 0)         
    GPIO.output(35, 0)
    GPIO.cleanup()

clear()
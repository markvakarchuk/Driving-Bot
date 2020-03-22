import RPi.GPIO as GPIO        # import RPi.GPIO module  
import time, keyboard, curses, sys, tty, termios

 #set GPIO mode to BOARD  
# GPIO.setmode(GPIO.BOARD)      
# GPIOsetup = False

# #set pinouts of motors
# #if PinA is HIGH & PinB is LOW motor spins forward 
motorL_pinA = 31    
motorL_pinB = 33
motorR_pinA = 35
motorR_pinB = 37

t = 0.1

i = 0

class robot():
    def __init__(self):
        global GPIOsetup
        GPIOsetup = False
        print(GPIOsetup)
        if not GPIOsetup:
            GPIO.setmode(GPIO.BOARD)
            motorL_pinA = 31    
            motorL_pinB = 33
            motorR_pinA = 35
            motorR_pinB = 37

            GPIO.setup(motorL_pinA, GPIO.OUT)          
            GPIO.setup(motorR_pinA, GPIO.OUT)         
            GPIO.setup(motorR_pinB, GPIO.OUT)
            GPIO.setup(motorL_pinB, GPIO.OUT)
            GPIOsetup = True
            print(GPIOsetup)
        
    def forward(self):
        GPIO.output(motorL_pinA, 0)         
        GPIO.output(motorR_pinB, 0)
        GPIO.output(motorL_pinB, 1)         
        GPIO.output(motorR_pinA, 1)
        time.sleep(t)
        self.stop()
    
    def backward(self):
        GPIO.output(motorL_pinA, 1)         
        GPIO.output(motorR_pinB, 1)
        GPIO.output(motorL_pinB, 0)         
        GPIO.output(motorR_pinA, 0)
        time.sleep(t)
        self.stop()
    
    def left(self):
        GPIO.output(motorL_pinA, 0)         
        GPIO.output(motorR_pinB, 0)
        GPIO.output(motorL_pinB, 1)         
        GPIO.output(motorR_pinA, 0)
        time.sleep(t)
        self.stop()
    
    def right(self):
        GPIO.output(motorL_pinA, 0)         
        GPIO.output(motorR_pinB, 0)
        GPIO.output(motorL_pinB, 0)         
        GPIO.output(motorR_pinA, 1)
        time.sleep(t)
        self.stop()

    def cw(self):
        GPIO.output(motorL_pinA, 1)         
        GPIO.output(motorR_pinB, 0)
        GPIO.output(motorL_pinB, 0)         
        GPIO.output(motorR_pinA, 1)
        time.sleep(t)
        self.stop()

    def ccw(self):
        GPIO.output(motorL_pinA, 0)         
        GPIO.output(motorR_pinB, 1)
        GPIO.output(motorL_pinB, 1)         
        GPIO.output(motorR_pinA, 0)
        time.sleep(t)
        self.stop()
    
    def stop(self):
        GPIO.output(motorL_pinA, 0)         
        GPIO.output(motorR_pinB, 0)
        GPIO.output(motorL_pinB, 0)         
        GPIO.output(motorR_pinA, 0)


# bot = robot()

# def getch():

#     char = getch.getch()

#     return ch

# while True:
#     char = raw_input()

#     # The car will drive forward when the "w" key is pressed
#     if(char == "w"):
#         bot.forward()

#     # The car will reverse when the "s" key is pressed
#     if(char == "s"):
#         bot.backward()

#     # The "a" key will toggle the steering left
#     if(char == "a"):
#         bot.left()

#     # The "d" key will toggle the steering right
#     if(char == "d"):
#         bot.right()

#     # The "d" key will toggle the steering right
#     if(char == "c"):
#         bot.cw()

#     # The "d" key will toggle the steering right
#     if(char == "cc"):
#         bot.ccw()
    
#     # The "x" key will break the loop and exit the program
#     if(char == "x"):
#         print("Program Ended")
#         False
#         bot.stop()
#         break
        
#     i = i+1
#     if i > 500:
#         break


GPIO.cleanup()
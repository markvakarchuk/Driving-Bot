import RPi.GPIO as GPIO        # import RPi.GPIO module  
import time, keyboard, curses, sys, tty, termios
# from gpiozero import Robot

GPIO.setmode(GPIO.BOARD)       # set GPIO mode to BOARD  
GPIO.setup(31, GPIO.OUT)          
GPIO.setup(33, GPIO.OUT)         
GPIO.setup(35, GPIO.OUT)         
GPIO.setup(37, GPIO.OUT)



def forward():
    GPIO.output(31, 0)         
    GPIO.output(37, 0)
    GPIO.output(33, 1)         
    GPIO.output(35, 1)

def backward():
    GPIO.output(31, 1)         
    GPIO.output(37, 1)
    GPIO.output(33, 0)         
    GPIO.output(35, 0)

def left():
    GPIO.output(31, 0)         
    GPIO.output(37, 0)
    GPIO.output(33, 1)         
    GPIO.output(35, 0)

def right():
    GPIO.output(31, 0)         
    GPIO.output(37, 0)
    GPIO.output(33, 0)         
    GPIO.output(35, 1)

def stop():
    GPIO.output(31, 0)         
    GPIO.output(37, 0)
    GPIO.output(33, 0)         
    GPIO.output(35, 0)

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

while True:
    # Keyboard character retrieval method is called and saved into variable
    char = getch()

    # The car will drive forward when the "w" key is pressed
    if(char == "w"):
        forward()

    # The car will reverse when the "s" key is pressed
    if(char == "s"):
        backward()

    # The "a" key will toggle the steering left
    if(char == "a"):
        left()

    # The "d" key will toggle the steering right
    if(char == "d"):
        right()

    # The "x" key will break the loop and exit the program
    if(char == "x"):
        print("Program Ended")
        False
        stop()
        break

    stop()
# actions = {
#             curses.KEY_UP:    forward(),
#             curses.KEY_DOWN:  backward(),
#             curses.KEY_LEFT:  left(),
#             curses.KEY_RIGHT: right(),
#         }
# def main(window):
#     next_key = None
#     while True:
#         curses.halfdelay(1)
#         if next_key is None:
#             key = window.getch()
#         else:
#             key = next_key
#             next_key = None
#         if key != -1:
#             # KEY DOWN
#             curses.halfdelay(3)
#             action = actions.get(key)
#             if action is not None:
#                 action()
#             next_key = key
#             while next_key == key:
#                 next_key = window.getch()
#             # KEY UP
#             stop()
#             GPIO.cleanup()
# main()
GPIO.cleanup()
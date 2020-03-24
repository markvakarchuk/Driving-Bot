from robot import *
from clr import clear
import time, logging, websocket, io, picamera

bot = robot()

try:
    try:
        import thread
    except ImportError:
        import _thread as thread

    def on_message(ws, message):
        if(message == "w"):
            bot.forward()
        elif(message == "s"):
            bot.backward()
        elif(message == "a"):
            bot.left()
        elif(message == "d"):
            bot.right()
        elif(message == "cw"):
            bot.cw()
        elif(message == "ccw"):
            bot.ccw()
        elif(message == "null"):
            bot.stop()
        elif(message == "quit"):
            bot.quit()
            ws.close()
        else:
            print("Unregonized message:" + message)
        # print("Client(%d) said: %s" % (client['id'], message))

    def on_error(ws, error):
        print(error)

    def on_close(ws):
        print("### closed ###")

    def on_open(ws):
        def run(*args):
            for i in range(3):
                time.sleep(1)
                ws.send("Hello %d" % i)
            time.sleep(1)
            my_stream = io.BytesIO()
            with picamera.PiCamera() as camera:
                camera.start_preview()
                # Camera warm-up time
                time.sleep(2)
                stream = camera.capture(my_stream, 'h.264')
            ws.send(stream)
                # ws.close()
                # print("thread terminating...")
            # thread.start_new_thread(run, ())


    def main():
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp("ws://192.168.86.23:8080/?bot=true",on_message = on_message, on_error = on_error,on_close = on_close)
        ws.on_open = on_open
        ws.run_forever()


    if __name__ == "__main__":
        main()

except KeyboardInterupt:
    print("Keyboard Interupt")
except:
    print("something else happened")
finally:
    clear()
    print("GPIO pins cleared using clear()")    



# my_stream = io.BytesIO()
# with picamera.PiCamera() as camera:
#     camera.start_preview()
#     # Camera warm-up time
#     time.sleep(2)
#     camera.capture(my_stream, 'h264')
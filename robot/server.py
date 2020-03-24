from websocket_server import WebsocketServer
from robot import *
import time
import logging

# class robot():
#   def __init__(self):
#     print("Init")

#   def forward(self):
#     print("Forward")
# # Called for every client connecting (after handshake)

bot = robot()

def new_client(client, server):
	print("New client connected and was given id %d" % client['id'])
	server.send_message_to_all("Hey all, a new client has joined us")


# Called for every client disconnecting
def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
  if(message == "w"):
    bot.forward()
  
  if(message == "s"):
    bot.backward()
  
  if(message == "a"):
    bot.left()
  
  if(message == "d"):
    bot.right()

  if(message == "cw"):
    bot.cw()

  if(message == "ccw"):
    bot.ccw()

  print("Client(%d) said: %s" % (client['id'], message))



PORT=9001
HOST="0.0.0.0"
server = WebsocketServer(PORT, "0.0.0.0", loglevel=logging.INFO)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
# print("Started on " + str(PORT))
# print("Host " + HOST)
server.run_forever()
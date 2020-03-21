from websocket_server import WebsocketServer
from driving import Robot

# class Robot():
#   def __init__(self):
#     print("Init")

#   def forward(self):
#     print("Forward")
# Called for every client connecting (after handshake)

bot = Robot()

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

  print("Client(%d) said: %s" % (client['id'], message))



PORT=9001
server = WebsocketServer(PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
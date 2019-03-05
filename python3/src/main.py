from colyseus.client import Client
from colyseus.room import Room
import threading

thread = None

def doAction():
    room = Room(client.connection)
    room.send("Hi there!")

def on_message(message):
    print("Message:", message)

def on_error(error):
    print("An error occurred with the socket:", error)

def on_close():
    print("### closed ###")

def on_open():
    print("Socket connection opened!")
    thread = threading.Thread(target=doAction)
    thread.start()


print("Hi ya")
client = Client("ws://localhost:3000")
client.on_open.add(on_open)

client.connection.run_forever()

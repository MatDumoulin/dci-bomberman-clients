from websocket import create_connection
from colyseus.connection import Connection
from colyseus.room import Room
import time
import threading

thread = None

def doAction():
    room = Room(conn)
    room.send("Hi there!")

def on_message(ws, message):
    print("Message:", message)

def on_error(ws, error):
    print("An error occurred with the socket:", error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    print("Socket connection opened!")
    thread = threading.Thread(target=doAction)
    thread.start()


print("Hi ya")
conn = Connection("ws://localhost:3000", on_open=on_open, on_close=on_close, on_error=on_error, on_message=on_message)
conn.run_forever()

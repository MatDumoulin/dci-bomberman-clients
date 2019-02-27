from websocket import create_connection
from colyseus.connection import Connection
import time

try:
    import thread
except ImportError:
    import _thread as thread

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
    doAction()


print("Hi ya")
conn = Connection("ws://localhost:3000", on_open=on_open, on_close=on_close, on_error=on_error, on_message=on_message)

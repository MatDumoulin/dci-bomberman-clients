from colyseus.connection import Connection
from colyseus.compression import Compression
from colyseus.protocol import Protocol

class Room:
    def __init__(self, connection):
        print("In room constructor")
        self.conn = connection
        self.id = "abcdef"

    def send(self, data):
        self.conn.send([Protocol.ROOM_DATA, self.id, data])


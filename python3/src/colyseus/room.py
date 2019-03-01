from colyseus.connection import Connection
from colyseus.compression import Compression
from colyseus.protocol import Protocol
from colyseus.signal import Signal


class Room:
    def __init__(self, name):
        self.conn = Connection("ws://localhost:3000",
            on_open=self.on_open,
            on_close=self.leave,
            on_error=self.on_error,
            on_message=self.message_callback
        )

        self.on_join = Signal()
        self.on_state_change = Signal()
        self.on_message = Signal()
        self.on_error = Signal()
        self.on_leave = Signal()

        self.on_leave.add(self.remove_all_listeners)
        self.id = None
        self.sessionId = None
        self.name = name

    def connect(self, endpoint):
        self.conn.url = endpoint
        self.conn.reconnect_enabled = False
        self.conn.on_message = self.message_callback
        self.conn.on_close = lambda e: self.on_leave.dispatch(e)
        self.conn.on_error = lambda e: self.on_error.dispatch(e)
        self.conn.open()

    def send(self, data):
        self.conn.send([Protocol.ROOM_DATA, self.id, data])

    def leave(self):
        self.conn.send([Protocol.LEAVE_ROOM])

    def remove_all_listeners(self):
        self.on_join.remove_all()
        self.on_state_change.remove_all() 
        self.on_message.remove_all()
        self.on_error.remove_all()
        self.on_leave.remove_all() 

    def message_callback(self, ws, message):
        message = ["blabla"] # TODO
        code = message[0]

        if (code == Protocol.JOIN_ROOM):
            self.sessionId = message[1]
            self.on_join.dispatch()

    def on_open(ws):
        print("Socket connection opened!")
        doAction()
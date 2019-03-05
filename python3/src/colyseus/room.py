from colyseus.connection import Connection
from colyseus.compression import Compression
from colyseus.protocol import Protocol
from colyseus.signal import Signal


class Room:
    def __init__(self, name, options = {}):
        self.on_join = Signal()
        self.on_state_change = Signal()
        self.on_message = Signal()
        self.on_error = Signal()
        self.on_leave = Signal()

        self.on_leave.add(self.remove_all_listeners)
        self.id = None
        self.sessionId = None
        self.name = name
        self.options = options

    def connect(self, endpoint):
        self.conn = Connection(endpoint)
        # Setting up listeners
        self.conn.on_open.add(lambda: self.on_join.dispatch())
        self.conn.on_close.add(lambda: self.on_leave.dispatch())
        self.conn.on_error.add(lambda e: self.handle_connection_error(e))
        self.conn.on_message.add(lambda m: self.message_callback(m))

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

    def handle_connection_error(self, e):
        print("Possible causes: room's onAuth() failed or maxClients has been reached.")
        self.on_error.dispatch(e)

    def message_callback(self, message):
        code = message[0]

        if code == Protocol.JOIN_ROOM:
            self.sessionId = message[1]
            self.on_join.dispatch()
        elif code == Protocol.JOIN_ERROR:
            print("Error:", message[1])
            self.on_error.dispatch(message[1])
        elif code == Protocol.ROOM_STATE:
            state = message[1]
            remote_current_time = message[2]
            remote_elapsed_time = message[3]
            #self.setState( state, remote_current_time, remote_elapsed_time )
            print("TODO: ROOM STATE")
        elif code == Protocol.ROOM_STATE_PATCH:
            print("TODO: PATCH INCOMING")
            pass#self.patch( message[1] )
        elif code == Protocol.ROOM_DATA:
            self.on_message.dispatch(message[1])
        elif code == Protocol.LEAVE_ROOM:
            self.leave()

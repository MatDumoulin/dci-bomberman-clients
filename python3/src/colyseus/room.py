import msgpack
import array
from colyseus.connection import Connection
from colyseus.compression import Compression
from colyseus.protocol import Protocol
from colyseus.signal import Signal
from colyseus.state_listener import StateListener


class Room(StateListener):
    def __init__(self, name, options = {}):
        super().__init__()
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

    def __del__(self):
        self.remove_all_listeners()
        self.leave()

    def connect(self, endpoint):
        self.conn = Connection(endpoint)
        # Setting up listeners
        self.conn.on_open.add(lambda: self.on_join.dispatch())
        self.conn.on_close.add(lambda: self.on_leave.dispatch())
        self.conn.on_error.add(lambda e: self.handle_connection_error(e))
        self.conn.on_message.add(lambda m: self.message_callback(m))
        self.conn.run_forever()

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
            self.set_state( state, remote_current_time, remote_elapsed_time )
        elif code == Protocol.ROOM_STATE_PATCH:
            self.patch( message[1] )
        elif code == Protocol.ROOM_DATA:
            self.on_message.dispatch(message[1])
        elif code == Protocol.LEAVE_ROOM:
            self.leave()


    def set_state(self, encoded_state, remote_current_time=None, remote_elapsed_time=None):
        super().set_state(msgpack.unpackb(encoded_state, raw=False))

        self._previousState = encoded_state

        # set remote clock properties
        """ if remote_current_time is not None and remote_elapsed_time is not None:
            self.remoteClock.currentTime = remote_current_time
            self.remoteClock.elapsedTime = remote_elapsed_time

        self.clock.start() """

        self.on_state_change.dispatch(self.state)


    def patch(self, binaryPatch ):
        # apply patch
        self._previousState = Compression.hydrate(self._previousState, bytes(binaryPatch))
        # trigger state callbacks
        super().set_state(msgpack.unpackb(self._previousState, raw=False))

        if "hasStarted" in self.state:
            print("Has started?", str(self.state["hasStarted"]))
        self.on_state_change.dispatch(self.state)

    def has_joined(self):
        return self.sessionId is not None

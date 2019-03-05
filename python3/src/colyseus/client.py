from colyseus.connection import Connection
from colyseus.room import Room
from colyseus.protocol import Protocol
from colyseus.signal import Signal
from config import PLAYER_ID

class Client:

    def __init__(self, url, options = {}):
        # id -> room
        self.rooms = {}
        self.connecting_rooms = {}

        self.hostname = url

        self.on_open = Signal()
        self.on_message = Signal()
        self.on_close = Signal()
        self.on_error = Signal()
        self.connect(PLAYER_ID, options)

    def join(self, room_name, options = {}):
        return self.create_room_request(room_name, options)

    def connect(self, colyseusid, options = {}):
        self.id = colyseusid if colyseusid is not None else ""
        self.conn = Connection(self.build_endpoint('', options))
        # Setting up listeners
        self.conn.on_open.add(lambda: self.dispatch_connection_opened())
        self.conn.on_message.add(lambda m: self.on_message_callback(m))
        self.conn.on_error.add(lambda e: self.on_error.dispatch(e))
        self.conn.on_close.add(lambda: self.on_close.dispatch())


    def dispatch_connection_opened(self):
        if self.id is not None:
            self.on_open.dispatch()


    def create_room(self, room_name, options = {}):
        return Room(room_name, options)


    def create_room_request(self, room_name, options, reuse_room_instance=None, retry_count=0):
        if "requestId" in options:
            options["requestId"] += 1
        else:
            options["requestId"] = 1

        room = reuse_room_instance if reuse_room_instance is not None else self.create_room(room_name, options)

        # remove references on leaving
        room.on_leave.add_once(lambda: self.remove_room(room.id, options["requestId"]))

        # retry joining the room in case the server couldn't matchmake into it
        if "retryTimes" in options:
            room.on_error.add_once(lambda e: self.retry_create_room_request(room_name, options, reuse_room_instance, retry_count))

        self.connecting_rooms[ options["requestId"] ] = room
        self.conn.on_open.add_once(lambda: self.conn.send([Protocol.JOIN_ROOM, room_name, options]))

        return room


    def remove_room(self, roomId, requestId):
        del self.rooms[roomId]
        del self.connecting_rooms[requestId]


    def retry_create_room_request(self, room_name, room, options, retry_count=0):
        if not room.has_joined and retry_count <= options["retryTimes"]:
            self.create_room_request(room_name, options, room, retry_count + 1)


    def build_endpoint(self, path = "", options = {}):
        # append colyseusid to connection string.
        params = ["colyseusid=" + str(self.id)]

        for name in options:
            to_string = str(options[name])
            value = to_string if not isinstance(options[name], bool) else to_string.lower()
            params.append(name + "=" + value)

        return self.hostname + "/" + path + "?$" + '&'.join(params)


    # TODO: Gerer les methodes suivantes
    def on_message_callback(self, message):
        code = message[0]

        if code == Protocol.USER_ID:
            if self.id == None or self.id == "":
                self.id = message[1]
            self.on_open.dispatch()
        elif code == Protocol.ROOM_LIST:
            pass
        elif code == Protocol.JOIN_ROOM:
            requestId = message[2]
            if requestId not in self.connecting_rooms:
                print("colyseus.py: client left room before receiving session id.")
                return
            room = self.connecting_rooms[ requestId ]
            room.id = message[1]
            self.rooms[room.id] = room
            room.connect(self.build_endpoint(room.id, room.options))
            del self.connecting_rooms[ requestId ]
        elif code == Protocol.JOIN_ERROR:
            print('colyseus.py: server error:', message[2])
            self.on_error.dispatch(message[2])


        print("on_message_callback client", message)
        self.on_message.dispatch(message)

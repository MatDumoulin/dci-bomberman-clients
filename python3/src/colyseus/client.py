from colyseus.connection import Connection
from colyseus.room import Room
from colyseus.protocol import Protocol

class Client:
    # TODO:
    id = None

    connection = None

    # id -> room
    rooms = {}
    connecting_rooms = {}

    def __init__(self, url, options = {}):
        self.hostname = url
        # getItem('colyseusid', (colyseusid) => this.connect(colyseusid, options));


    def connect(self, colyseusid, options = {}):
        self.id = colyseusid if colyseusid is not None else ""

        self.connection = Connection(self.build_endpoint('', options))
        self.connection.onmessage = lambda: self.on_message_callback()
        """
        self.connection.onclose = (e) => self.onClose.dispatch(e)
        self.connection.onerror = (e) => self.onError.dispatch(e)
        """
        # check for id on cookie
        self.connection.on_open() => {
            if (self.id) {
                self.onOpen.dispatch()
            }
        }

    def dispatch_connection_opened(self):
        if self.id is not None:
            self.onOpen.dispatch()


    def create_room(self, room_name, options = {}):
        return Room(room_name, options)


    def create_room_request(self, room_name, options, reuse_room_instance=None, retry_count=0):
        options.requestId += 1
        room = reuse_room_instance if reuse_room_instance is not None else self.create_room(room_name, options)

        # remove references on leaving
        room.on_leave.add_once(lambda: self.remove_room(room.id, options.requestId))

        # retry joining the room in case the server couldn't matchmake into it
        if options.retryTimes:
            room.on_error.add_once(lambda: self.retry_create_room_request(room_name, options, reuse_room_instance, retry_count))

        self.connecting_rooms[ options.requestId ] = room
        self.connection.send([Protocol.JOIN_ROOM, room_name, options])
        return room


    def remove_room(self, roomId, requestId):
        del self.rooms[roomId]
        del self.connecting_rooms[requestId]


    def retry_create_room_request(self, room_name, room, options, retry_count=0):
        if not room.has_joined and retry_count <= options.retry_times:
            self.create_room_request(room_name, options, room, retry_count + 1)


    def build_endpoint(self, path = "", options = {}):
        # append colyseusid to connection string.
        params = ["colyseusid=" + str(self.id)]

        for name in options:
            params.append("name=" + options[name])

        return self.hostname + "/" + path + "?$" + '&'.join(params)


    # TODO: Gerer les methodes suivantes
    def on_message_callback(self):
        # USER_ID
        # Protocol.ROOM_LIST
        pass

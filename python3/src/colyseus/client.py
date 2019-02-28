from colyseus.connection import Connection
from colyseus.room import Room
from colyseus.protocol import Protocol

class Client:
    # TODO:
    id = None

    connection = None

    # id -> room
    rooms = {}

    def __init__(self, url, options = {}):
        self.hostname = url
        # getItem('colyseusid', (colyseusid) => this.connect(colyseusid, options));


    def connect(self, colyseusid, options = {}):
        self.id = colyseusid if colyseusid is not None else ""

        self.connection = Connection(self.buildEndpoint('', options))
"""         self.connection.onmessage = self.onMessageCallback.bind(self)
        self.connection.onclose = (e) => self.onClose.dispatch(e)
        self.connection.onerror = (e) => self.onError.dispatch(e)

        # check for id on cookie
        self.connection.onopen = () => {
            if (self.id) {
                self.onOpen.dispatch()
            }
        } """


    def createRoom(self, room_name, options = {}):
        return Room(room_name, options)


    def createRoomRequest(self, room_name, options, reuse_room_instance=None, retryCount=0):
        options.requestId += 1
        room = reuse_room_instance if reuse_room_instance is not None else self.createRoom(room_name, options)

        # remove references on leaving
        room.on_leave.add_once(lambda: self.removeRoom(room.id, options.requestId))

        # retry joining the room in case the server couldn't matchmake into it
        if options.retryTimes:
            room.on_error.add_once(lambda: self.retryCreateRoomRequest(room_name, options, reuse_room_instance, retryCount))

        self.connectingRooms[ options.requestId ] = room
        self.connection.send([Protocol.JOIN_ROOM, roomName, options])
        return room


    def removeRoom(self, roomId, requestId)
        del self.rooms[roomId]
        del self.connectingRooms[requestId]


    def retryCreateRoomRequest(self, room_name, room, options, retry_count=0):
        if not room.has_joined and retry_count <= options.retry_times:
            self.createRoomRequest(room_name, options, room, retry_count + 1)


    def buildEnpoint(self, path = "", options = {}):
        # append colyseusid to connection string.
        params = ["colyseusid=" + str(self.id)]

        for name in options:
            params.append("name=" + options[name])

        return self.hostname + "/" + path + "?$" + '&'.join(params)


    # TODO: Gerer les methodes suivantes
    def onMessageCallback(self):
        # USER_ID
        # Protocol.ROOM_LIST
        pass

import msgpack
from colyseus.signal import Signal
from colyseus.webSocketClient import WebSocketClient

# Wraps the socket client into its own thread
class Connection:
    def __init__(self, url):
        self.on_open = Signal()
        self.on_message = Signal()
        self.on_close = Signal()
        self.on_error = Signal()

        self.ws = WebSocketClient(
            url,
            on_open=lambda ws: self.on_open.dispatch(),
            on_message=lambda ws, m: self.on_message_callback(m),
            on_error=lambda ws, e: self.on_error.dispatch(e),
            on_close=lambda *ws: self.on_close.dispatch())

    def send(self, message):
        encodedMessage = msgpack.packb(message)
        self.ws.send(encodedMessage)
        print("Message: ", message, "sent!")

    def run_forever(self):
        self.ws.run_forever()

    def on_message_callback(self, message):
        decodedMessage = msgpack.unpackb(message, ext_hook=ext_hook, raw=False)
        self.on_message.dispatch(decodedMessage)

# Handle undefined and null and map them to None
def ext_hook(code, data):
    if code == 0:
        return None
    return msgpack.ExtType(code, data)

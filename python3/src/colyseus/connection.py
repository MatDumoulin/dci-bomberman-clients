import msgpack
from colyseus.signal import Signal
from colyseus.webSocketClient import WebSocketClient

# Wraps the socket client into its own thread
class Connection:
    def __init__(self, url, on_error=None, on_close=None):
        self.on_message = Signal()
        self.ws = WebSocketClient(url, on_message=lambda ws, m: self.on_message_callback(m), on_error=on_error, on_close=on_close)

    def send(self, message):
        encodedMessage = msgpack.packb(message)
        self.ws.send(encodedMessage)
        print("Message: ", message, "sent!")

    def run_forever(self):
        self.ws.run_forever()

    def on_open(self, on_open_callback):
        self.ws.on_open(on_open_callback)

    def on_message_callback(self, message):
        decodedMessage = msgpack.unpackb(message, raw=False)
        print(decodedMessage)
        self.on_message.dispatch(decodedMessage)

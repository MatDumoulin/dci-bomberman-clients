import websocket

class WebSocketClient:
    connected = False

    def __init__(self, url, on_open=None, on_message=None, on_error=None, on_close=None):
        self.url = url
        websocket.enableTrace(True)

        self.ws = websocket.WebSocketApp(url,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
        self.ws.on_open = on_open

    def __del__(self):
        self.ws.close()

    def send(self, message):
        self.ws.send(message)

    def run_forever(self):
        self.ws.run_forever()
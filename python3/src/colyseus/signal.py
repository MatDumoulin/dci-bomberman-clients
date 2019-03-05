# Observer pattern wrapped in an object.
class Signal:
    def __init__(self):
        self.add_listeners = []
        self.add_once_listeners = []

    def add(self, callback):
        self.add_listeners.append(callback)

    def add_once(self, callback):
        self.add_once_listeners.append(callback)

    def dispatch(self, data=None):
        callback = lambda cb: cb(data) if data is not None else cb()

        for listener in self.add_once_listeners:
            callback(listener)

        self.add_once_listeners = []

        for listener in self.add_listeners:
            callback(listener)

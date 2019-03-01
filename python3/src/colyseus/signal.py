class Signal:
    def __init__(self):
        self.listeners = []
        self.listeners_once = []

    def add(self, listener):
        self.listeners.append(listener)

    def add_once(self, listener):
        self.listeners_once.append(listener)

    def dispatch(self, data = None):
        for listener in self.listeners:
            listener(data)
        for listener in self.listeners_once:
            listener(data)
        self.listeners_once = []

    def remove_all(self):
        self.listeners = []
        self.listeners_once = []

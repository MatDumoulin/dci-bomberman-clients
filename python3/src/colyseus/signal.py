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
            listener(data) if data is not None else listener()
        for listener in self.listeners_once:
            listener(data) if data is not None else listener()
        self.listeners_once = []

    def remove_all(self):
        self.listeners = []
        self.listeners_once = []

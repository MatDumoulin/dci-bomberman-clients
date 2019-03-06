class StateListener:
    def __init__(self):
        self.state = None
        self.listeners = {}

    # Takes into consideration that the segments given are always in the state.
    # If not, an unhandled error will be raised by python.
    def listen(self, segments, callback):
        if segments in self.listeners:
            self.listeners[segments].append(callback)
        else:
            self.listeners[segments] = [callback]


    def set_state(self, new_state):
        # For each listened to attribute, check if it has changed
        for attribute in self.listeners:
            change_descriptor = self.attribute_change_descriptor(self.state, new_state, attribute)
            if change_descriptor[0]:
                self.notify_listeners(attribute, change_descriptor[1])
        # then, update the state.
        self.state = new_state

        if "hasJoined" in self.state and self.state["hasJoined"] == True:
            print("test")


    def attribute_change_descriptor(self, old_state, new_state, attribute):
        segment_array = attribute.split('/')
        old_value = old_state
        new_value = new_state

        for segment in segment_array:
            if old_value is not None:
                if segment not in old_value or segment not in new_value:
                    raise Exception("Invalid path given to listen method. One attribute is missing in the state.")
                old_value = old_value[segment]
            new_value = new_value[segment]

        return (old_value != new_value, {"value": new_value, "previousValue": old_value})

    def notify_listeners(self, attribute, param):
        for listener in self.listeners[attribute]:
            listener(param)

class Storage:
    items = {}

    @staticmethod
    def set_item(key, value):
        Storage.items[key] = value

    @staticmethod
    def get_item(key):
        return Storage.items[key] if key in Storage.items else None


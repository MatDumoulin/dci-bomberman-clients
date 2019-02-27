from enum import Enum

class Directions(Enum):
    UP = {"row":-1, "col":0}
    DOWN = {"row":1, "col": 0}
    LEFT = {"row":0, "col": -1}
    RIGHT = {"row":0, "col": 1}

    @staticmethod
    def asIterable():
        return [Directions.UP, Directions.DOWN, Directions.LEFT, Directions.RIGHT]
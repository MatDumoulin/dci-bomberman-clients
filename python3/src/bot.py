import random

LEFT  = "a"
DOWN  = "s"
UP    = "w"
RIGHT = "d"
BOMB  = "b"

class Bot:
    @staticmethod
    def do_action(game_state):
        # try this if you want to die:
        return random.choice([LEFT, DOWN, UP, RIGHT, BOMB])

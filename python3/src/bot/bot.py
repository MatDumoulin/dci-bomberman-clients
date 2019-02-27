import math
from random import random
from models.player import PlayerAction

class Bot:
    def __init__(self):
        pass

    # Insert the code for your bot here.
    def doAction(self):
        return self.getRandomMove()

    # This method does not return plant bomb moves in order to protect the player.
    def getRandomMove(self):
        randomMove = math.floor(random() * 5)
        action = PlayerAction()

        if randomMove == 0:
            action.move_down = True
        elif randomMove == 1:
            action.move_up = True
        elif randomMove == 2:
            action.move_left = True
        elif randomMove == 3:
            action.move_right = True

        return action

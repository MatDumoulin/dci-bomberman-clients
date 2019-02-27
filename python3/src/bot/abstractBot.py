import time
from abc import ABC, abstractmethod
from colyseus.room import Room
from models import PlayerAction, GameState
from src.config import PLAYER_ID

"""
The parent class of the bot. This is where all the mechanic is put
in place in order to have the but up and running with the server.
"""
class AbstractBot(ABC):

    """
    The request for player action call rate, in ms.
    You can change this value if you want your bot to be more
    responsive to game state changes, but be aware that it will
    limit your decision time frame.
    """
    CALL_RATE = 1000 / 5

    def __init__(self, game):
        self.id = PLAYER_ID
        self._game = game
        self.listenOnStateChange()

    def __del__(self):
        self.leaveGame()

    # This is where the magic happens. This method will be inherited by the children
    @abstractmethod
    def doAction(self):
        pass

    def start(self):
        # Check for an action right away instead of waiting for CALL_RATE ms.
        self.handleAction()

        # Every CALL_RATE ms, check for another action.
        self._checkForAction = True
        while self._checkForAction:
            self.handleAction()
            currentTime = time.time()
            lastActionTime = currentTime

            sleepTime = self.CALL_RATE - (currentTime - lastActionTime)
            if sleepTime > 0:
                time.sleep(sleepTime)

    def leaveGame(self):
        self._checkForAction = False

        if self._game and self._game.hasJoined:
            self._game.leave()


    def handleAction(self):
        action = self.doAction()

        # Comment this function if you don't want moves to be logged.
        self.logAction(action)
        # Action sent to
        self._game.send({
            'type': "PlayerAction",
            'payload': { 'playerId': self.id, 'action': action }
        })

    def logAction(self, action):
        if action.move_down:
            print("Down")
        elif action.move_up:
            print("Up")
        elif action.move_left:
            print("Left")
        elif action.move_right:
            print("Right")
        elif action.plant_bomb:
            print("Plant Bomb")
        else:
            print("Stand still")

    def listenOnStateChange(self):
        if self._game and self._game.hasJoined:
            # TODO: Implement state change listener
            pass
            """ self._game.onStateChange.add((state: GameState) => {
                self.state = state;
            }) """


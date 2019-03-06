from models.gameObject import GameObject
from models.bomb import Bomb

class Player(GameObject):
    # playerId: PlayerId;
    # actions: PlayerAction;
    # /** The amount of pixels that the player moves at every game tick */
    # speed: number;
    # /** Maximum number of bombs that the player can drop at a time. */
    # maxBombCount: number;
    # /** All the bombs currently in the map that were dropped by the player */
    # bombs: Bomb[];
    # isAlive: boolean;
    pass


# Moves that the player can do.
class PlayerAction:
    # move_up = False
    # move_down = False
    # move_left = False
    # move_right = False
    # plant_bomb = False
    pass

def player_action_factory():
    action = {}
    action["move_up"] = False
    action["move_down"] = False
    action["move_left"] = False
    action["move_right"] = False
    action["plant_bomb"] = False
    return action

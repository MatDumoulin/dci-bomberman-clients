from models.gameObject import GameObject
from models.gameMap import GameMap
from models.bomb import Bomb
from models.player import Player
from models.upgrade import Upgrade

class GameState:
    # /** Can be used to quickly iterate though bombs. */
    # bombs: { [id: string]: Bomb };
    # /** Can be used to quickly iterate though items to collect. */
    # collectibles: Upgrade[];
    # /** A unique id for the game. This can be used to track which game you have joined. */
    # gameId: string;
    # /** The map you are playing on for this game. */
    # gameMap: GameMap;
    # /** If the game has started. */
    # hasStarted: boolean;
    # /** If the game is over. The game can be over without any winner (ex: A draw). In that case, nobody wins. */
    # isOver: boolean;
    # /** The players of the game, including you. */
    # players: { [id: string]: Player };
    # /** If the game is paused or not. */
    # paused: boolean;
    # /** The time elapsed since the beginning of the game, in ms. */
    # time: number;
    # /** The maximum duration of a game, in ms. If time >= maxTime, there is a draw so nobody wins. */
    # maxTime: number;
    # /** If isOver is true and this is null, it means that there's a draw. */
    # winner: PlayerId;
    pass


import { GameMap } from "./game-map";
import { Player, PlayerId } from "./player";
import { Upgrade } from "./upgrade";
import { Bomb } from "./bomb";

export interface GameState {
    /** Can be used to quickly iterate though bombs. */
    bombs: { [id: string]: Bomb };
    /** Can be used to quickly iterate though items to collect. */
    collectibles: Upgrade[];
    gameId: string;
    gameMap: GameMap;
    hasStarted: boolean;
    isOver: boolean;
    players: { [id: string]: Player };
    paused: boolean;
    time: number;
    winner: PlayerId;
}

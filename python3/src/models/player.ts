import { GameObject } from "./game-object";
import { Bomb } from "./bomb";

export type PlayerId = string;

export interface Player extends GameObject {
    playerId: PlayerId;
    /** The inputs of this player. */
    actions: PlayerAction;
    /** The amount of pixels that the player moves at every game tick */
    speed: number;
    /** Maximum number of bombs that the player can drop at a time. */
    maxBombCount: number;
    /** All the bombs currently in the map that were dropped by the player */
    bombs: Bomb[];
    isAlive: boolean;

    /**
     * The power of the explosion for this bomb, in map cell.
     * This power is the number of cells that will be affected by the bomb,
     * starting from the position of the bomb to the end of one side of the explosion.
     */
    bombPower:number;
}

// Moves that the player can do.
export class PlayerAction {
    move_up = false;
    move_down = false;
    move_left = false;
    move_right = false;
    plant_bomb = false;
}

/** Used to describe the action of a given player for the socket communication */
export interface PlayerActionWrapper {
    playerId: PlayerId;
    actions: PlayerAction;
}

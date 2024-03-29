import { GameObject, ObjectType } from "./game-object";
import { PlayerId } from "./player";

export interface Bomb extends GameObject {
    /** In seconds */
    TIME_BEFORE_EXPLOSION: number;
    /** In seconds */
    EXPLOSION_DURATION: number;
    /** The identifier of the bomb. */
    id: number;
    /** The user that planted the bomb. */
    plantedBy: PlayerId;
    /** The time where the bomb was planted. */
    plantedAt: number;
    /** The row of the bomb in the game map */
    row: number;
    /** The column of the bomb in the game map */
    col: number;

    /**
     * The power of the explosion for this bomb, in map cell.
     * This power is the number of cells that will be affected by the bomb,
     * starting from the position of the bomb to the end of one side of the explosion.
     */
    bombPower: number;
}

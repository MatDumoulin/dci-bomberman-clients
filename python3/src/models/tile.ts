import { GameObject } from "./game-object";
import { Bomb } from "./bomb";

export const OUT_OF_BOUND: Tile = null;

export interface Tile {
    info: GameObject;
    bombs: Bomb[];
    isOnFire: boolean;
    row: number;
    col: number;
}

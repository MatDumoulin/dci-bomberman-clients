import { Tile } from "./tile";
import { Point } from "./point";

export interface GameMap {
    /** All the cells of the map. */
    _tiles: Tile[][];
    /** The height of the map, in tiles. */
    height: number;
    /** The width of the map, in tiles. */
    width: number;
}

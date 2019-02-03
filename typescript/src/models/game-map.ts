import { Tile } from "./tile";

export interface GameMap {
    /** All the cells of the map. */
    _tiles: Tile[][];
    /** In pixels. */
    _tileWidth: number;
    /** In pixels. */
    _tileHeight: number;
}

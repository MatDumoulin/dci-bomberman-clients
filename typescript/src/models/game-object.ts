import { Point } from "./point";

export enum ObjectType {
    Wall = "WALL",
    Walkable = "WALKABLE",
    BreakableItem = "BREAKABLE",
    Player = "PLAYER",
    Bomb = "BOMB",
    PowerUp = "POWER-UP",
    SpeedUp = "SPEED-UP",
    BombUp = "BOMB-UP"
}

/** Any object that can be displayed on the map has these properties. */
export class GameObject {
    type: ObjectType;
    coordinates: Point;
    width: number;
    height: number;
}

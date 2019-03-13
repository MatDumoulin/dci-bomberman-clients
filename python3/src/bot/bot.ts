import { PlayerAction } from "../models";
import { AbstractBot } from "./abstract-bot";
import { Room } from "colyseus.js";

export class Bot extends AbstractBot {
    constructor(game: Room) {
        super(game);
    }

    /** Insert the code for your bot here.  */
    doAction(cmd:string): PlayerAction {
        const action = new PlayerAction();

        if (cmd === "s") {
            action.move_down = true;
        } else if (cmd === "w") {
            action.move_up = true;
        } else if (cmd === "a") {
            action.move_left = true;
        } else if (cmd === "d") {
            action.move_right = true;
        } else if (cmd === "b") {
            action.plant_bomb = true;
        }

        return action;
    }
}

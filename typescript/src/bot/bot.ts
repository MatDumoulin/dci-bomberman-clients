import { PlayerAction } from "../models";
import { AbstractBot } from "./abstract-bot";
import { Room } from "colyseus.js";

export class Bot extends AbstractBot {
    constructor(game: Room) {
        super(game);
    }

    /** Insert the code for your bot here.  */
    doAction(): PlayerAction {
        return this.getRandomMove();
    }

    /** This method does not return plant bomb moves in order to protect the player. */
    getRandomMove() {
        const randomMove = Math.floor(Math.random() * 5);
        const actions = new PlayerAction();

        if (randomMove === 0) {
            actions.move_down = true;
        } else if (randomMove === 1) {
            actions.move_up = true;
        } else if (randomMove === 2) {
            actions.move_left = true;
        } else if (randomMove === 3) {
            actions.move_right = true;
        }

        return actions;
    }
}

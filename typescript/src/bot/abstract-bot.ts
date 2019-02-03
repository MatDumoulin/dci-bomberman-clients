import { PlayerAction, GameState } from "../models";
import { Room } from "colyseus.js";
import { config } from "../config";

/**
 * The parent class of the bot. This is where all the mechanic is put
 * in place in order to have the but up and running with the server.
 */
export abstract class AbstractBot {
    /**
     * The request for player action call rate, in ms.
     * You can change this value if you want your bot to be more
     * responsive to game state changes, but be aware that it will
     * limit your decision time frame.
     */
    private readonly CALL_RATE = 1000 / 5;
    private _interval: NodeJS.Timer;
    private _game: Room;

    protected readonly id = config.playerId;
    /** The current state of the game. DO NOT MUTATE THIS OBJECT. */
    protected state: GameState;

    constructor(game: Room) {
        this._game = game;
        this.listenOnStateChange();
    }

    /** This is where the magic happens. */
    abstract doAction(): PlayerAction;

    start(): void {
        // Check for an action right away instead of waiting for CALL_RATE ms.
        this.handleAction();
        // Every CALL_RATE ms, check for another action.
        this._interval = setInterval(() => this.handleAction(), this.CALL_RATE);
    }

    leaveGame(): void {
        if (this._interval) {
            clearInterval(this._interval);
        }

        if (this._game && this._game.hasJoined) {
            this._game.leave();
        }
    }

    private handleAction(): void {
        const actions = this.doAction();

        // Comment this function if you don't want moves to be logged.
        this.logAction(actions);

        this._game.send({
            type: "PlayerAction",
            payload: { playerId: this.id, actions }
        });
    }

    private logAction(action: PlayerAction): void {
        if (action.move_down) {
            console.log("Down");
        } else if (action.move_up) {
            console.log("Up");
        } else if (action.move_left) {
            console.log("Left");
        } else if (action.move_right) {
            console.log("Right");
        } else if (action.plant_bomb) {
            console.log("Plant Bomb");
        } else {
            console.log("Stand still");
        }
    }

    private listenOnStateChange(): void {
        if (this._game && this._game.hasJoined) {
            this._game.onStateChange.add((state: GameState) => {
                this.state = state;
            });
        }
    }
}

import "./colyseusjs.polyfill";

import { GameFinder } from "./game-finder";
import { Client, Room, DataChange } from "colyseus.js";
import { config } from "./config";
import { Bot } from "./bot";

let client: Client;
let game: Room;
const botId = config.playerId;
let bot: Bot;

async function joinGame() {
    console.log("Trying to join a game...");
    try {
        const serverUrl = await GameFinder.next();
        client = new Client("ws:" + serverUrl);
        client.id = config.playerId;

        game = client.join("dci", { isPlaying: true, id: botId });

        game.onJoin.add(() => {
            console.log("Bot has joined game ", game.id);
            bot = new Bot(game);
        });

        client.onError.add((error: ErrorEvent) => {
            console.error("An error occurred: ", error.message);
        });

        game.listen("hasStarted", (change: DataChange) => {
            if (change.value === true) {
                console.log("Game has started.");
                bot.start();
            }
        });

        game.listen("isOver", (change: DataChange) => {
            if (change.value === true) {
                console.log("Game is over.");
                cleanUpResources();
                joinGame();
            }
        });
    } catch (err) {
        console.error(err);
    }
}

joinGame();

function cleanUpResources(ex?: any) {
    if (ex) {
        console.error(ex);
    }

    console.log("Cleaning up resources...");

    if (bot) {
        bot.leaveGame();
    }

    if (game && game.hasJoined) {
        game.leave();
    }

    // If the client does not have an id, he has not yet joined a game.
    if (client && client.id) {
        client.close();
    }
}

function closeEverything(ex?: any) {
    cleanUpResources(ex);
    process.exit();
}

// Clean up when app is closing
process.on("exit", closeEverything);

// catches ctrl+c event
process.on("SIGINT", closeEverything);

// catches "kill pid" (for example: nodemon restart)
process.on("SIGUSR1", closeEverything);
process.on("SIGUSR2", closeEverything);

// catches uncaught exceptions
process.on("uncaughtException", closeEverything);
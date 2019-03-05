from bot.bot import Bot
from colyseus.client import Client
from colyseus.room import Room
from config import LOAD_BALANCER_HOST, LOAD_BALANCER_PORT, PLAYER_ID
import threading

thread = None

def doAction(game):
    pass
    # game.send("Hi there!")

def on_error(error):
    print("[Game] An error occurred with the socket:", error)

def on_close():
    print("### closed ###")

def on_join(game):
    print("Socket connection opened!")
    print("Bot has joined game ", game.id)
    # TODO: spawn bot -->  bot = Bot(game)
    thread = threading.Thread(target=lambda: doAction(game))
    thread.start()


def join_game():
    client = Client("ws://localhost:3000")

    game = client.join("dci", { "isPlaying": True, "id": PLAYER_ID })

    game.on_join.add(lambda: on_join(game))
    game.on_error.add(on_error)
    client.conn.run_forever()
    """ game.listen("hasStarted", (change: DataChange) => {
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
    }); """

join_game()

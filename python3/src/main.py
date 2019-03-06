import threading
import time
from bot.bot import Bot
from colyseus.client import Client
from colyseus.room import Room
from config import LOAD_BALANCER_HOST, LOAD_BALANCER_PORT, PLAYER_ID



def on_game_start(game, change):
    print("Game has started:", str(change))
    if change["value"] == True:
        bot = Bot(game)
        bot.start()

def on_game_over(change):
    print("Game is over:", str(change))
    # Once the game of the player is over, wait for 5 seconds then join another game.
    if change["value"] == True:
        time.sleep(5)
        join_game()


def on_error(error):
    print("[Game] An error occurred with the socket:", error)

def on_close():
    print("### closed ###")

def on_join(game):
    print("Socket connection opened!")
    print("Bot has joined game ", game.id)



def join_game():
    client = Client("ws://192.168.0.103:3000")

    game = client.join("dci", { "isPlaying": True, "id": PLAYER_ID })

    game.on_join.add(lambda: on_join(game))
    game.on_error.add(on_error)
    game.listen("hasStarted", lambda change: on_game_start(game, change))
    game.listen("isOver", on_game_over)
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

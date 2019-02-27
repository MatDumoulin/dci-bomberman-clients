import urllib.request
from config import LOAD_BALANCER_HOST, LOAD_BALANCER_PORT

class GameFinder:
    LOAD_BALANCER_URL = "http://" + LOAD_BALANCER_HOST + ":" + LOAD_BALANCER_PORT

    @staticmethod
    def next():
        return urllib.request.urlopen(GameFinder.LOAD_BALANCER_URL + "/join-game").read()

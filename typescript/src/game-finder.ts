import fetch from "node-fetch";
import { config } from "./config";

export class GameFinder {
    // prettier-ignore
    private static readonly LOAD_BALANCER_URL = `http://${config.loadBalancerHost}:${config.loadBalancerPort}`;

    static async next(): Promise<string> {
        return fetch(this.LOAD_BALANCER_URL + "/join-game").then(response =>
            response.text()
        );
    }
}

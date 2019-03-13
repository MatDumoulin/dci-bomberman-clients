/**
 * Configuration used for the bomberman bot.
 */

function makeid() {
    var text = "";
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  
    for (var i = 0; i < 8; i++)
      text += possible.charAt(Math.floor(Math.random() * possible.length));
  
    return text;
}

export const config = {
    loadBalancerHost: "shopiflag.com",
    loadBalancerPort: 2999,
    playerId: makeid()
};

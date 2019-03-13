# dci-bomberman-clients
Clients to use for AI development in order to play the dci-bomberman game.

## typescript
Your code goes in typescript/src/bot/bot.ts
`cd typescript`
`npm install`
`npm start`

## python3
Your code goes in python3/src/bot.py
`cd python3`
`npm install`
`python3 src/main.py`

## docker
From either the python3 or typescript folder:
`docker build -t dci-bomberman-client .`
`docker run -it --rm dci-bomberman-client`

# game_state
```
{
  "gameId": "7lpPOrz1yq",
  "gameMap": {
    "tileWidth": 32,
    "tileHeight": 32,
    "tilesOnFire": [],
    "_tiles": [
      [
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALKABLE",
            "coordinates": {
              "col": 0,
              "row": 0
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALKABLE",
            "coordinates": {
              "col": 1,
              "row": 0
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 2,
              "row": 0
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 3,
              "row": 0
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 4,
              "row": 0
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 5,
              "row": 0
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 6,
              "row": 0
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 7,
              "row": 0
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 8,
              "row": 0
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 9,
              "row": 0
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 10,
              "row": 0
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 11,
              "row": 0
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 12,
              "row": 0
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALKABLE",
            "coordinates": {
              "col": 13,
              "row": 0
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALKABLE",
            "coordinates": {
              "col": 14,
              "row": 0
            }
          }
        }
      ],
      [
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALKABLE",
            "coordinates": {
              "col": 0,
              "row": 1
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 1,
              "row": 1
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 2,
              "row": 1
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 3,
              "row": 1
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 4,
              "row": 1
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 5,
              "row": 1
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 6,
              "row": 1
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 7,
              "row": 1
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 8,
              "row": 1
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 9,
              "row": 1
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 10,
              "row": 1
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 11,
              "row": 1
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 12,
              "row": 1
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 13,
              "row": 1
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALKABLE",
            "coordinates": {
              "col": 14,
              "row": 1
            }
          }
        }
      ],
      [
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 0,
              "row": 2
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 1,
              "row": 2
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 2,
              "row": 2
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 3,
              "row": 2
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 4,
              "row": 2
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 5,
              "row": 2
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 6,
              "row": 2
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 7,
              "row": 2
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 8,
              "row": 2
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 9,
              "row": 2
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 10,
              "row": 2
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 11,
              "row": 2
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 12,
              "row": 2
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 13,
              "row": 2
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 14,
              "row": 2
            }
          }
        }
      ],
      [
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 0,
              "row": 3
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 1,
              "row": 3
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 2,
              "row": 3
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 3,
              "row": 3
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 4,
              "row": 3
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 5,
              "row": 3
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 6,
              "row": 3
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 7,
              "row": 3
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 8,
              "row": 3
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 9,
              "row": 3
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 10,
              "row": 3
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 11,
              "row": 3
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 12,
              "row": 3
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 13,
              "row": 3
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 14,
              "row": 3
            }
          }
        }
      ],
      [
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 0,
              "row": 4
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 1,
              "row": 4
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 2,
              "row": 4
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 3,
              "row": 4
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 4,
              "row": 4
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 5,
              "row": 4
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 6,
              "row": 4
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 7,
              "row": 4
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 8,
              "row": 4
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 9,
              "row": 4
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 10,
              "row": 4
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 11,
              "row": 4
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 12,
              "row": 4
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 13,
              "row": 4
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 14,
              "row": 4
            }
          }
        }
      ],
      [
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 0,
              "row": 5
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 1,
              "row": 5
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 2,
              "row": 5
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 3,
              "row": 5
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 4,
              "row": 5
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 5,
              "row": 5
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 6,
              "row": 5
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 7,
              "row": 5
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 8,
              "row": 5
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 9,
              "row": 5
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 10,
              "row": 5
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 11,
              "row": 5
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 12,
              "row": 5
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 13,
              "row": 5
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 14,
              "row": 5
            }
          }
        }
      ],
      [
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 0,
              "row": 6
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 1,
              "row": 6
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 2,
              "row": 6
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 3,
              "row": 6
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 4,
              "row": 6
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 5,
              "row": 6
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 6,
              "row": 6
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 7,
              "row": 6
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 8,
              "row": 6
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 9,
              "row": 6
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 10,
              "row": 6
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 11,
              "row": 6
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 12,
              "row": 6
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 13,
              "row": 6
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 14,
              "row": 6
            }
          }
        }
      ],
      [
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 0,
              "row": 7
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 1,
              "row": 7
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 2,
              "row": 7
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 3,
              "row": 7
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 4,
              "row": 7
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 5,
              "row": 7
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 6,
              "row": 7
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 7,
              "row": 7
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 8,
              "row": 7
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 9,
              "row": 7
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 10,
              "row": 7
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 11,
              "row": 7
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 12,
              "row": 7
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 13,
              "row": 7
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 14,
              "row": 7
            }
          }
        }
      ],
      [
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 0,
              "row": 8
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 1,
              "row": 8
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 2,
              "row": 8
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 3,
              "row": 8
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 4,
              "row": 8
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 5,
              "row": 8
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 6,
              "row": 8
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 7,
              "row": 8
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 8,
              "row": 8
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 9,
              "row": 8
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 10,
              "row": 8
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 11,
              "row": 8
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 12,
              "row": 8
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 13,
              "row": 8
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 14,
              "row": 8
            }
          }
        }
      ],
      [
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 0,
              "row": 9
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 1,
              "row": 9
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 2,
              "row": 9
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 3,
              "row": 9
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 4,
              "row": 9
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 5,
              "row": 9
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 6,
              "row": 9
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 7,
              "row": 9
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 8,
              "row": 9
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 9,
              "row": 9
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 10,
              "row": 9
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 11,
              "row": 9
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 12,
              "row": 9
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 13,
              "row": 9
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 14,
              "row": 9
            }
          }
        }
      ],
      [
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 0,
              "row": 10
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 1,
              "row": 10
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 2,
              "row": 10
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 3,
              "row": 10
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 4,
              "row": 10
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 5,
              "row": 10
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 6,
              "row": 10
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 7,
              "row": 10
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 8,
              "row": 10
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 9,
              "row": 10
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 10,
              "row": 10
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 11,
              "row": 10
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 12,
              "row": 10
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 13,
              "row": 10
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 14,
              "row": 10
            }
          }
        }
      ],
      [
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 0,
              "row": 11
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 1,
              "row": 11
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 2,
              "row": 11
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 3,
              "row": 11
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 4,
              "row": 11
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 5,
              "row": 11
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 6,
              "row": 11
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 7,
              "row": 11
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 8,
              "row": 11
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 9,
              "row": 11
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 10,
              "row": 11
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 11,
              "row": 11
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 12,
              "row": 11
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 13,
              "row": 11
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 14,
              "row": 11
            }
          }
        }
      ],
      [
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 0,
              "row": 12
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 1,
              "row": 12
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 2,
              "row": 12
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 3,
              "row": 12
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 4,
              "row": 12
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 5,
              "row": 12
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 6,
              "row": 12
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 7,
              "row": 12
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 8,
              "row": 12
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 9,
              "row": 12
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 10,
              "row": 12
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 11,
              "row": 12
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 12,
              "row": 12
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 13,
              "row": 12
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 14,
              "row": 12
            }
          }
        }
      ],
      [
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALKABLE",
            "coordinates": {
              "col": 0,
              "row": 13
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 1,
              "row": 13
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 2,
              "row": 13
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 3,
              "row": 13
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 4,
              "row": 13
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 5,
              "row": 13
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 6,
              "row": 13
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 7,
              "row": 13
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 8,
              "row": 13
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 9,
              "row": 13
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 10,
              "row": 13
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 11,
              "row": 13
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 12,
              "row": 13
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALL",
            "coordinates": {
              "col": 13,
              "row": 13
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALKABLE",
            "coordinates": {
              "col": 14,
              "row": 13
            }
          }
        }
      ],
      [
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALKABLE",
            "coordinates": {
              "col": 0,
              "row": 14
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALKABLE",
            "coordinates": {
              "col": 1,
              "row": 14
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 2,
              "row": 14
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 3,
              "row": 14
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 4,
              "row": 14
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 5,
              "row": 14
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 6,
              "row": 14
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 7,
              "row": 14
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 8,
              "row": 14
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 9,
              "row": 14
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 10,
              "row": 14
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 11,
              "row": 14
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "BREAKABLE",
            "coordinates": {
              "col": 12,
              "row": 14
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALKABLE",
            "coordinates": {
              "col": 13,
              "row": 14
            }
          }
        },
        {
          "bombs": [],
          "isOnFire": false,
          "collectible": null,
          "info": {
            "width": 32,
            "height": 32,
            "type": "WALKABLE",
            "coordinates": {
              "col": 14,
              "row": 14
            }
          }
        }
      ]
    ],
    "_spawnPositions": [
      {
        "col": 0,
        "row": 0
      },
      {
        "col": 14,
        "row": 0
      },
      {
        "col": 0,
        "row": 14
      },
      {
        "col": 14,
        "row": 14
      }
    ]
  },
  "players": {
    "gThm9eLo": {
      "width": 24,
      "height": 24,
      "type": "PLAYER",
      "maxBombCount": 1,
      "bombs": [],
      "isAlive": true,
      "timeBetweenMoves": 600,
      "lastMove": 134,
      "canMove": true,
      "bombPower": 2,
      "playerId": "gThm9eLo",
      "actions": {
        "move_up": false,
        "move_down": false,
        "move_left": false,
        "move_right": false,
        "plant_bomb": false
      },
      "joinOrder": 1,
      "coordinates": {
        "col": 0,
        "row": 1
      }
    },
    "uVEKKiK9": {
      "width": 24,
      "height": 24,
      "type": "PLAYER",
      "maxBombCount": 1,
      "bombs": [],
      "isAlive": true,
      "timeBetweenMoves": 600,
      "lastMove": 741,
      "canMove": false,
      "bombPower": 2,
      "playerId": "uVEKKiK9",
      "actions": {
        "move_up": false,
        "move_down": true,
        "move_left": false,
        "move_right": false,
        "plant_bomb": false
      },
      "joinOrder": 2,
      "coordinates": {
        "col": 14,
        "row": 0
      }
    },
    "LC3UmFgr": {
      "width": 24,
      "height": 24,
      "type": "PLAYER",
      "maxBombCount": 1,
      "bombs": [],
      "isAlive": true,
      "timeBetweenMoves": 600,
      "lastMove": -9007199254740991,
      "canMove": true,
      "bombPower": 2,
      "playerId": "LC3UmFgr",
      "actions": {
        "move_up": false,
        "move_down": false,
        "move_left": true,
        "move_right": false,
        "plant_bomb": false
      },
      "joinOrder": 3,
      "coordinates": {
        "col": 0,
        "row": 14
      }
    },
    "53rjCVqV": {
      "width": 24,
      "height": 24,
      "type": "PLAYER",
      "maxBombCount": 1,
      "bombs": [],
      "isAlive": true,
      "timeBetweenMoves": 600,
      "lastMove": 410,
      "canMove": false,
      "bombPower": 2,
      "playerId": "53rjCVqV",
      "actions": {
        "move_up": false,
        "move_down": false,
        "move_left": false,
        "move_right": true,
        "plant_bomb": false
      },
      "joinOrder": 4,
      "coordinates": {
        "col": 13,
        "row": 14
      }
    }
  },
  "bombs": {},
  "collectibles": [],
  "paused": false,
  "isOver": false,
  "hasStarted": true,
  "time": 900,
  "maxTime": 300000,
  "winner": null,
  "maxPlayerCount": 4
}
```
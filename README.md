# psychic-telegram
A Game of Hieroglyphs and Telepathy


## Game States
### Lobby
#### RC
LOBBY_WAITING
LOBBY_READY

#### PC
LOBBY_PREJOIN
LOBBY_JOINED
LOBBY_READY

#### Server
LOBBY_REQUESTED
LOBBY_WAITING
LOBBY_READY

### Game
#### RC
GAME_INTRO
GAME_ROUND_DISPLAY
GAME_ROUND_REVEAL
GAME_END

#### PC
GAME_INTRO
GAME_ROUND_DISPLAY
GAME_ROUND_REVEAL
GAME_END

#### Server
GAME_INTRO
GAME_ROUND_DISPLAY
GAME_ROUND_REVEAL
GAME_END

## Structure Sequence

### Creating New Room
1. Room Client (RC) sends connect request to server
2. Server allows connection
3. RC states it's a room client
4. Server registers RC and gives it a room_id
5. Server loops until RC states readiness
   a. server sends id of player clients(PC) to RC
   b. RC responds with list of current PCs
6. RC states readiness to server
7. Server starts gameplay phase notifying all clients in room

### In Room Game-Loop
1. Server assigns a phrase and itemset to each PC
2. Server starts countdown timer display on RC
3. Server loops and waits until each player submits back a product or for
   timeout
    a. Server sends signal that PC is done to RC
4. Server loops through each product randomly
    a. Server sends product to RC

const defaultHexagon = {
          life: 0,
          selected: false,
          player: 0,
          dragging: false,
          mark: '',
          image: '',
          position: {},
          surroundings: []
        };
const hexagonPositions = [
  {x:20,y:7},
  {x:20,y:21.3},
  {x:20,y:64.2},
  {x:20,y:78.5},
  {x:27.5,y:14.3},
  {x:27.5,y:28.6},
  {x:27.5,y:42.9},
  {x:27.5,y:57.2},
  {x:27.5,y:71.5},
  {x:35,y:7},
  {x:35,y:21.3},
  {x:35,y:35.6},
  {x:35,y:49.9},
  {x:35,y:64.2},
  {x:35,y:78.5},

  {x:70,y:7},
  {x:70,y:21.3},
  {x:70,y:64.2},
  {x:70,y:78.5},
  {x:62.5,y:14.3},
  {x:62.5,y:28.6},
  {x:62.5,y:42.9},
  {x:62.5,y:57.2},
  {x:62.5,y:71.5},
  {x:55,y:7},
  {x:55,y:21.3},
  {x:55,y:35.6},
  {x:55,y:49.9},
  {x:55,y:64.2},
  {x:55,y:78.5}];







const hexagonSurroundings = [
  [1,4],
  [0,4,5],
  [7,8,3],
  [2,8],
  [0,1,5,9,10],
  [1,4,6,10,11],
  [5,7,11,12],
  [2,6,8,12,13],
  [2,3,7,13,14],
  [4,10,24,25,26,27,28,29],
  [9,4,5,24,25,26,27,28,29],
  [5,6,10,12,24,25,26,27,28,29],
  [6,7,11,12,24,25,26,27,28,29],
  [7,8,12,14,24,25,26,27,28,29],
  [8,13,24,25,26,27,28,29],
  [16,19],
  [15,19,20],
  [18,22,23],
  [17,23],
  [15,16,20,24,25],
  [16,19,21,25,26],
  [20,22,26,27],
  [17,21,23,27,28],
  [17,18,22,28,29],
  [19,25,9,10,11,12,13,14],
  [19,20,24,26,9,10,11,12,13,14],
  [20,21,25,27,9,10,11,12,13,14],
  [21,22,26,28,9,10,11,12,13,14],
  [22,23,27,29,9,10,11,12,13,14],
  [23,28,9,10,11,12,13,14],
];

let defaulthexagons = [];
for (let i=0; i<hexagonPositions.length; i++)
  defaulthexagons.push({...defaultHexagon, position: hexagonPositions[i], surroundings: hexagonSurroundings[i]});

function checkSurroundings(surroundings,value,hexagons) {
  for (let i=0; i<surroundings.length; i++)
    if (hexagons[surroundings[i]].player == value)
      return true;
  return false;
}

export default function reducer(state={
    player1Data: {
      playerSide: 'left',
      name: 'Daniel',
      playerImg: "https://scontent-frt3-1.xx.fbcdn.net/v/t1.0-9/10269434_942199432476034_6147352969057776589_n.jpg?oh=27dc22d84743428346340e3a1b7603da&oe=59AFFE16",
      totalLife: 5000,
      life: 5000,
      marked: ''
    },
    player2Data: {
      playerSide: 'right',
      name: 'Raluca',
      playerImg: "https://scontent-frt3-1.xx.fbcdn.net/v/t1.0-9/10269434_942199432476034_6147352969057776589_n.jpg?oh=27dc22d84743428346340e3a1b7603da&oe=59AFFE16",
      totalLife: 8000,
      life: 8000,
      marked: ''
    },
    hexagons: defaulthexagons,
    currentPlayer: 1,
    webSocket: 0,
    gameStatus: "zero",
    fetching: false,
    fetched: false,
    error: null,
  }, action) {

    switch (action.type) {

      case 'NEW_SOCKET': {
          return {...state,
            webSocket: action.payload,
            gameStatus: "waiting"
          }
      }

      case 'SELECT_TWITTER_USER': {
          return {...state,
            gameStatus: "select_twitter_user"
          }
      }

      case 'SET_TWITTER_USER': {
          const data = action.payload
          if (data.player==1)
            return {...state,
              gameStatus: "waiting_for_opponent",
              currentPlayer: 1,
              player1Data: {...state.player1Data,
                name: data.name,
                playerImg: data.image,
                totalLife: data.followers_count,
                life: data.followers_count,
                followers: data.followers
              }
            }
            else
            return {...state,
              gameStatus: "waiting_for_opponent",
              currentPlayer: 2,
              player2Data: {...state.player2Data,
                name: data.name,
                playerImg: data.image,
                totalLife: data.followers_count,
                life: data.followers_count,
                followers: data.followers
              }
            }
      }

      case 'SET_OPPONENT': {
          const data = action.payload
          const hexagons = [...state.hexagons]
          for (let i=0; i<15; i++)
            {
            if (data.player==1)
              hexagons[i] = {...hexagons[i],
                image: data.followers[i]
              }
              else
              hexagons[i] = {...hexagons[i],
                image: state.player1Data.followers[i]
              }
            }
          for (let i=15; i<30; i++)
            {
            if (data.player==2)
              hexagons[i] = {...hexagons[i],
                image: data.followers[i-15]
              }
              else
              hexagons[i] = {...hexagons[i],
                image: state.player2Data.followers[i-15]
              }
            }
          if (data.player==1)
            return {...state,
              gameStatus: "start",
              hexagons: hexagons,
              player1Data: {...state.player1Data,
                name: data.name,
                playerImg: data.image,
                totalLife: data.followers_count,
                life: data.followers_count,
                followers: data.followers
              }
            }
            else
            return {...state,
              gameStatus: "start",
              hexagons: hexagons,
              player2Data: {...state.player2Data,
                name: data.name,
                playerImg: data.image,
                totalLife: data.followers_count,
                life: data.followers_count,
                followers: data.followers
              }
            }
      }

      case "SOCKET_MESSAGE": {
        return {...state,
          gameStatus: "select_user"
        }
      }


      case "START_GAME": {
        return {...state,
          gameStatus: "select_phase"
        }
      }

      case "SELECT": {
        const {id} = action.payload;
        const hexagons = [...state.hexagons]
        if (state.currentPlayer==1) {
          if (id<15)
            hexagons[id] = {...hexagons[id], selected : true}
          }
          else {
          if (id>=15)
            hexagons[id] = {...hexagons[id], selected : true}
          }

        return {...state,
          hexagons: hexagons
        }
      }

      case "SELECTED": {
        const hexagons = [...state.hexagons]
        let ok_mine = 0;
        for (let i=0; i<hexagons.length; i++)
            {
            if (hexagons[i].selected)
              ok_mine ++;
            }
        if (ok_mine>0)
          return {...state,
            gameStatus: "selected"
          }
          else
          return {...state}
      }

      case "DISTRIBUTE_LIFE": {
        const hexagons = [...state.hexagons]
        for (let i=0; i<hexagons.length; i++)
          if (hexagons[i].selected)
            hexagons[i] = {...hexagons[i], life : action.payload.lifePerHex, player: action.payload.currentPlayer}
        const message = {
              type: "lifeDistributed",
              data: {
                playerLife: action.payload.remainingLife,
                hexagons: hexagons,
                lifePerHex: action.payload.lifePerHex
              }
        }
        state.webSocket.send(JSON.stringify(message))

        if (action.payload.currentPlayer==1)
          return {...state,
            player1Data: {...state.player1Data,
              life: action.payload.remainingLife,
              lifePerHex: action.payload.lifePerHex
            },
            hexagons: hexagons,
            gameStatus: 'waiting_opponent_selection'
          }
          else
          return {...state,
            player2Data: {...state.player2Data,
              life: action.payload.remainingLife,
              lifePerHex: action.payload.lifePerHex
            },
            hexagons: hexagons,
            gameStatus: 'waiting_opponent_selection'
          }
      }


      case "OPPONENT_SELECTED": {
        const data = action.payload
        const hexagons = [...state.hexagons]
        if (state.currentPlayer==1) {
          for (let i=15; i<30; i++)
            hexagons[i] = {...hexagons[i],
              life: data.hexagons[i].life,
              player: data.hexagons[i].player
            }
          return {...state,
            hexagons: hexagons,
            player2Data: {...state.player2Data,
              life: data.playerLife
            },
            gameStatus: "game_phase"
          }
          }
          else {
          for (let i=0; i<15; i++)
            hexagons[i] = {...hexagons[i],
              life: data.hexagons[i].life,
              player: data.hexagons[i].player
            }
          return {...state,
            hexagons: hexagons,
            player1Data: {...state.player1Data,
              life: data.playerLife
            },
            gameStatus: "game_phase"
          }
          }
          console.log(11);
      }

      case "DIRECTLY_TO": {
        const data = action.payload
        const hexagons = [...state.hexagons]
        const player1Data = {...state.player1Data}
        const player2Data = {...state.player2Data}
        let me,him;
        if (data.player==1) {
          me = data.mine;
          him = data.his;
          }
          else {
          me = data.his;
          him = data.mine;
          }
        for (let i=0; i<15; i++)
          hexagons[i] = {...hexagons[i],
            life: me.gameboard.hexagons[i].life,
            player: me.gameboard.hexagons[i].player,
            image: me.gameboard.hexagons[i].image,
            selected: me.gameboard.hexagons[i].selected,
          }
        for (let i=15; i<30; i++)
          hexagons[i] = {...hexagons[i],
            life: him.gameboard.hexagons[i].life,
            player: him.gameboard.hexagons[i].player,
            image: him.gameboard.hexagons[i].image,
            selected: him.gameboard.hexagons[i].selected,
          }
          hexagons[21] = {...hexagons[21],
            life: 180792,
            player: 1,
            selected: true
          };
          player1Data.totalLife = me.followers_count;
          player1Data.life = me.gameboard.playerLife;
          player1Data.name = me.name;
          player1Data.playerImg = me.image;
          player1Data.lifePerHex = me.lifePerHex;
          player2Data.totalLife = him.followers_count;
          player2Data.life = him.gameboard.playerLife;
          player2Data.name = him.name;
          player2Data.playerImg = him.image;
          player2Data.lifePerHex = him.lifePerHex;
        return {...state,
          currentPlayer: data.player,
          hexagons: hexagons,
          player1Data: player1Data,
          player2Data: player2Data,
          gameStatus: 'game_phase'
        }
      }
      //game_phase
      case "START_ATTACK": {
        return {...state,
          gameStatus: "attack_select",
        }
      }
      case "START_DEFEND": {
        return {...state,
          gameStatus: "defend_select",
        }
      }

      case "ATTACK_SELECT": {
        const {id} = action.payload;
        const hexagons = [...state.hexagons]

        let hexagon = {...hexagons[id]}

        if (state.currentPlayer != hexagon.player)
          {
          if (checkSurroundings(hexagon.surroundings,state.currentPlayer,hexagons))
              {
              hexagon.mark = 'attack';

              for (let i=0; i<hexagons.length; i++)
                if (hexagons[i].mark=='attack' && hexagons[i].player!=state.currentPlayer && i!=id)
                    hexagons[i] = {...hexagons[i], mark:''}
              }
          }
        if (state.currentPlayer == hexagon.player)
            {
            hexagon.mark = 'attack';
            for (let i=0; i<hexagons.length; i++)
              if (hexagons[i].mark=='attack' && hexagons[i].player==hexagon.player && i!=id)
                  hexagons[i] = {...hexagons[i], mark:''}
            }


        hexagons[id] = {...hexagon}
        return {...state,
          hexagons: hexagons
        }
      }

      case "ATTACK_SELECT_PLAYER": {
        const hexagons = [...state.hexagons];
        let playerSide = action.payload;

        if (state.currentPlayer==1 && playerSide=='right')
          {
          if (checkSurroundings([15,16,17,18,20,21,22],state.currentPlayer,hexagons))
            return {...state,
              player2Data: {...state.player2Data,
                marked: 'attack'
              }
            }
          }

        if (state.currentPlayer==2 && playerSide=='left')
          {
          if (checkSurroundings([0,1,2,3,5,6,7],state.currentPlayer,hexagons))
            return {...state,
              player1Data: {...state.player1Data,
                marked: 'attack'
              }
            }
          }

        return {...state}
      }


      case "FINISH_ATTACK": {
        const hexagons = [...state.hexagons]
        let ok_mine = 0;
        let ok_his = 0;
        let ok_neutre = 0;
        let ok_direct_player = 0;
        let attacker = 0;
        let attacked = 0;
        for (let i=0; i<hexagons.length; i++)
            {
            if (hexagons[i].player == state.currentPlayer && hexagons[i].mark=='attack')
              {
              ok_mine = 1;
              attacker = i;
              }
            if (hexagons[i].player != state.currentPlayer && hexagons[i].mark=='attack')
              {
              attacked = i;
              if (hexagons[i].player == 0 )
                ok_neutre = 1;
                else
                ok_his = 1;
              }
            }
        if (state.currentPlayer==1 && state.player2Data.marked=='attack')
          ok_direct_player = 1;
        if (state.currentPlayer==2 && state.player1Data.marked=='attack')
          ok_direct_player = 1;


        if (ok_mine && (ok_his || ok_neutre || ok_direct_player))
          {
          let playerLife = 0;
          let lifePerHex = 0;
          if (state.currentPlayer==1) {
            playerLife = state.player1Data.life;
            lifePerHex = state.player1Data.lifePerHex;
            }
            else {
            playerLife = state.player2Data.life;
            lifePerHex = state.player2Data.lifePerHex;
            }
          let directAttack = ok_direct_player;
          let message = {
            type: "attacking",
            data: {
              me: state.currentPlayer,
              attacker: attacker,
              attacked: attacked,
              lifePerHex: lifePerHex,
              playerLife: playerLife,
              hexagons: state.hexagons,
              directAttack: directAttack
            }
          }
          console.log(11);

          state.webSocket.send(JSON.stringify(message))

          return {...state,
            gameStatus: "attacking",
            }
          }
          else {
            return {...state}
          }
      }

      case "DEFEND_SELECT": {
        const {id} = action.payload;
        const hexagons = [...state.hexagons]

        let hexagon = {...hexagons[id]}

        if (state.currentPlayer == hexagon.player)
            {
            if (hexagon.mark == '')
              hexagon.mark = 'defend';
              else
              hexagon.mark = '';
            }


        hexagons[id] = {...hexagon}
        return {...state,
          hexagons: hexagons
        }
      }


      case "FINISH_DEFEND": {
        const hexagons = [...state.hexagons]
        let ok_mine = 0;
        let defenders = [];
        for (let i=0; i<hexagons.length; i++)
            {
            if (hexagons[i].player == state.currentPlayer && hexagons[i].mark=='defend')
              {
              ok_mine ++;
              defenders.push(i);
              }
            }
        if (ok_mine>1) {

          let playerLife = 0;
          let lifePerHex = 0;
          if (state.currentPlayer==1) {
            playerLife = state.player1Data.life;
            lifePerHex = state.player1Data.lifePerHex;
            }
            else {
            playerLife = state.player2Data.life;
            lifePerHex = state.player2Data.lifePerHex;
            }

          let message = {
            type: "defending",
            data: {
              me: state.currentPlayer,
              defenders: defenders,
              lifePerHex: lifePerHex,
              playerLife: playerLife,
              hexagons: state.hexagons
            }
          }

          state.webSocket.send(JSON.stringify(message))

          return {...state,
            gameStatus: "defending",
            }
          }
          else {
            return {...state}
          }
      }

      case "2_STEP_PHASE": {
        console.log(action.payload);
        const step = action.payload["STEP_1"];
        const hexagons = [...state.hexagons]
        hexagons[step.attacker] = step.hexagons[step.attacker]
        hexagons[step.attacked] = step.hexagons[step.attacked]
        if (step.directAttack==1) {
          if (step.player==1)
            return {...state,
              hexagons: hexagons,
              player1Data: {...state.player1Data,
                life: step.playerLife,
                marked: ''
              },
              player2Data: {...state.player2Data,
                life: step.otherPlayerLife,
                marked: ''
              },
              gameStatus: "attack_step_1",
              step_2: action.payload["STEP_2"]
            }
            else
            return {...state,
              hexagons: hexagons,
              player2Data: {...state.player2Data,
                life: step.playerLife,
                marked: ''
              },
              player1Data: {...state.player1Data,
                life: step.otherPlayerLife,
                marked: ''
              },
              gameStatus: "attack_step_1",
              step_2: action.payload["STEP_2"]
            }
        }
        else {
          if (step.player==1)
            return {...state,
              hexagons: hexagons,
              player1Data: {...state.player1Data,
                life: step.playerLife
              },
              gameStatus: "attack_step_1",
              step_2: action.payload["STEP_2"]
            }
            else
            return {...state,
              hexagons: hexagons,
              player2Data: {...state.player2Data,
                life: step.playerLife
              },
              gameStatus: "attack_step_1",
              step_2: action.payload["STEP_2"]
            }
          }
      }

      case "2_STEP_PHASE_2": {
        const step = action.payload;
        const hexagons = [...state.hexagons]
        hexagons[step.attacker] = step.hexagons[step.attacker]
        hexagons[step.attacked] = step.hexagons[step.attacked]

        if (state.gameStatus=='game_over')
          return {...state}

        if (step.directAttack==1) {
          if (step.player==1)
            return {...state,
              hexagons: hexagons,
              player1Data: {...state.player1Data,
                life: step.playerLife,
                marked: ''
              },
              player2Data: {...state.player2Data,
                life: step.otherPlayerLife,
                marked: ''
              },
              gameStatus: "game_phase",
              step_2: {}
            }
            else
            return {...state,
              hexagons: hexagons,
              player2Data: {...state.player2Data,
                life: step.playerLife,
                marked: ''
              },
              player1Data: {...state.player1Data,
                life: step.otherPlayerLife,
                marked: ''
              },
              gameStatus: "game_phase",
              step_2: {}
            }
        }
        else {
          if (step.player==1)
            return {...state,
              hexagons: hexagons,
              player1Data: {...state.player1Data,
                life: step.playerLife
              },
              gameStatus: "game_phase",
              step_2: {}
            }
            else
            return {...state,
              hexagons: hexagons,
              player2Data: {...state.player2Data,
                life: step.playerLife
              },
              gameStatus: "game_phase",
              step_2: {}
            }
          }
      }

      case "1_STEP_ATTACK_DEFENSE": {
        const data = action.payload;
        const hexagons = [...state.hexagons];

        if (state.gameStatus=='game_over')
          return {...state}

        hexagons[data.attacker] = data.hexagons[data.attacker];
        for (let i=0; i<data.defenders.length; i++)
          hexagons[data.defenders[i]] = data.hexagons[data.defenders[i]];

        if (data.player==1)
          return {...state,
            hexagons: hexagons,
            player1Data: {...state.player1Data,
              life: data.playerLife
            },
            gameStatus: "game_phase"
          }
          else
          return {...state,
            hexagons: hexagons,
            player2Data: {...state.player2Data,
              life: data.playerLife
            },
            gameStatus: "game_phase"
          }
      }

      case "1_STEP_PHASE_CLASH": {
        const data = action.payload;
        const hexagons = [...state.hexagons];

        hexagons[data.attacker1] = data.hexagons[data.attacker1];
        hexagons[data.attacker2] = data.hexagons[data.attacker2];
        hexagons[data.attacked1] = data.hexagons[data.attacked1];
        hexagons[data.attacked2] = data.hexagons[data.attacked2];

        return {...state,
          hexagons: hexagons,
          player1Data: {...state.player1Data,
            life: data.player1Life
          },
          player2Data: {...state.player2Data,
            life: data.player2Life
          },
          gameStatus: "game_phase"
        }
      }

      case "GAME_OVER": {
        return {...state,
          gameStatus: 'game_over',
          gameWon: action.payload
        }
      }


    }

    return state
}

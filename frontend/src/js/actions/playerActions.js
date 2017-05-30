import axios from "axios";


export function clickLife() {
  return {
    type: 'LIFE',
    payload: 500,
  }
}

export function clickPlayer(player) {
  return {
    type: 'ATTACK_SELECT_PLAYER',
    payload: player,
  }
}


export function start() {
  return {
    type: 'START_GAME'
  }
}


export function selected_done() {
  return {
    type: 'SELECTED'
  }
}


export function attackStart() {
  return {
    type: 'START_ATTACK'
  }
}


export function attackFinish() {
  return {
    type: 'FINISH_ATTACK'
  }
}

export function defendStart() {
  return {
    type: 'START_DEFEND'
  }
}

export function defendFinish() {
  return {
    type: 'FINISH_DEFEND'
  }
}

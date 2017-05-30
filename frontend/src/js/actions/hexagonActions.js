import axios from "axios";


export function click(data) {
  let type = 'SELECT';
  switch (data.gameStatus) {
    case 'select_phase':
      type = 'SELECT';
      break;
    case 'attack_select':
      type = 'ATTACK_SELECT';
      break;
    case 'defend_select':
      type = 'DEFEND_SELECT';
      break;
    default:

  }
  return {
    type: type,
    payload: {
      id: data.id
    },
  }
}


export function start_drag(data) {
  return {
    type: 'START_DRAG',
    payload: {
      id: data.id
    },
  }
}


export function mouseIn(data) {
  return {
    type: 'MOUSE_IN',
    payload: {
      id: data.id
    },
  }
}

import React from "react"
import { connect } from "react-redux"


import {click} from "../actions/hexagonActions"
import {start, selected_done, attackStart, defendStart, attackFinish, defendFinish} from "../actions/playerActions"
import {distributeLife} from "../actions/gameboardActions"


@connect((store) => {
  return {

  };
})
export default class PlayerInteraction extends React.Component {

  start() {
    this.props.dispatch(start())
  }

  selected_done() {
    this.props.dispatch(selected_done())
  }

  attack_start() {
    this.props.dispatch(attackStart())
  }

  attack_finish() {
    this.props.dispatch(attackFinish())
  }

  defend_start() {
    this.props.dispatch(defendStart())
  }

  defend_finish() {
    this.props.dispatch(defendFinish())
  }

  render() {
    const { gameStatus } = this.props.data;
    let content = '';
    switch (gameStatus) {
      case 'start':
        content = <button onClick={this.start.bind(this)} class="start_button">Start</button>
        break;
      case 'select_phase':
        content = <div>Select your things<button onClick={this.selected_done.bind(this)}>Done</button></div>
        break;
      case 'waiting_opponent_selection':
        content = <div>Waiting on opponent</div>
        break;
      case 'game_phase':
        content = <div>
              <button onClick={this.attack_start.bind(this)}>Attack</button>
              <button onClick={this.defend_start.bind(this)}>Defend</button>
            </div>
        break;
      case 'attack_select':
        content = <div>
              <button onClick={this.attack_finish.bind(this)}>Done</button>
            </div>
        break;
      case 'defend_select':
        content = <div>
              <button onClick={this.defend_finish.bind(this)}>Done</button>
            </div>
        break;
      case 'attacking':
      case 'attack_step_1':
        content = <div>
              Attacking
            </div>
        break;
      case 'defending':
        content = <div>
              Defending
            </div>
        break;
      default:
          content = <button onClick={this.start.bind(this)} class="start_button">Start</button>
    }

    return <div class="player_interaction">
      {content}
    </div>;
  }
}

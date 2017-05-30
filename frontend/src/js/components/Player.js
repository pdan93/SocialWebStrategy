import React from "react"
import { connect } from "react-redux"

import { clickLife } from "../actions/playerActions"

@connect((store) => {
  return {

  };
})
export default class Player extends React.Component {

  clickLife() {
    this.props.dispatch(clickLife())
  }

  render() {
    const { player } = this.props;

    const lifeLineStyle = {
      width: ((player.life/player.totalLife)*100)+"%"
    }
    let class_add = ' '+player.playerSide;
    if (this.props.currentPlayer==1 && player.playerSide=="left")
      class_add += ' current_player';
    if (this.props.currentPlayer==2 && player.playerSide=="right")
      class_add += ' current_player';
    return <div class={"player" + class_add}>
      <div class="img" onClick={this.clickLife.bind(this)}>
        <img src={player.playerImg} />
      </div>
      <div class="name">{player.name}</div>
      <div class="life">
        <div class="life_line" style={lifeLineStyle}></div>
        <span>{player.life.toLocaleString()}</span>
      </div>
    </div>;
  }
}

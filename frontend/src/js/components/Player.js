import React from "react"
import { connect } from "react-redux"

import { clickLife, clickPlayer } from "../actions/playerActions"

@connect((store) => {
  return {

  };
})
export default class Player extends React.Component {

  clickLife() {
    this.props.dispatch(clickLife())
  }

  clickPlayer() {
    this.props.dispatch(clickPlayer(this.props.player.playerSide))
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

    if (player.marked)
      class_add += ' '+player.marked;

    let click = null;
    if (this.props.gameStatus=='attack_select')
      click = this.clickPlayer.bind(this);

    return <div class={"player" + class_add}>
      <div class="img" onClick={click}>
        <img src={player.playerImg} />
        <div class="colorize"></div>
      </div>
      <div class="name">{player.name}</div>
      <div class="life">
        <div class="life_line" style={lifeLineStyle}></div>
        <span>{player.life.toLocaleString()}</span>
      </div>
    </div>;
  }
}

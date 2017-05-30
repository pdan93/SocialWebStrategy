import React from "react"
import { connect } from "react-redux"


import {click, start_drag, mouseIn} from "../actions/hexagonActions"


@connect((store) => {
  return {

  };
})
export default class Hexagon extends React.Component {

  click() {
    this.props.dispatch(click(this.props))
  }

  render() {
    const { data, gameStatus } = this.props;
    const hexStyle = {
      left: data.position.x+'%',
      top: data.position.y+'%'
    };
    let class_add = '';
    if (data.selected) class_add = ' selected';
    let click = null;
    let mousedown = null;

    if (gameStatus == 'select_phase' || gameStatus == 'attack_select' || gameStatus == 'defend_select')
      click = this.click.bind(this);

    if (data.player>0)
      class_add+= ' active player-'+data.player;


    switch (data.mark) {
      case 'attack':
          class_add += ' attack';
        break;
      case 'defend':
          class_add += ' defend';
        break;
      default:

    }

    let colorizeStyle = null;
    if (data.player>0)
      colorizeStyle = {
        height: (data.life*100/this.props.lifePerHex)+'%'
      }

    return <div class={"hexagon " + this.props.id + class_add} style={hexStyle}>
      <div>
        <div>
          <div onClick={click}>
            <img src={data.image} alt=""/>
            <div class="colorize" style={colorizeStyle}></div>
            <span class="hex_life">{data.life.toLocaleString()}</span>
          </div>
        </div>
      </div>
    </div>;
  }
}

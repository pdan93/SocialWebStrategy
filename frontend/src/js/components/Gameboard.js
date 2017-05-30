import React from "react"
import { connect } from "react-redux"

import Hexagon from "./Hexagon"
import Player from "./Player"
import PlayerInteraction from "./PlayerInteraction"
import {distributeLife, attack_step_2} from "../actions/gameboardActions"

@connect((store) => {
  return {
    hexagons : store.gameboard.hexagons,
    gameboard : store.gameboard
  };
})
export default class Gameboard extends React.Component {

  distributeLife() {
    this.props.dispatch(distributeLife(this.props))
  }
  attack_step_2() {
    this.props.dispatch(attack_step_2(this.props))
  }

  render() {
    const {gameboard, hexagons} = this.props;
    const hexList = [];
    for (let i=0; i<15; i++)
        hexList.push(<Hexagon key={i} id={i} data={hexagons[i]} lifePerHex={gameboard.player1Data.lifePerHex} gameStatus={gameboard.gameStatus} />);
    for (let i=15; i<30; i++)
        hexList.push(<Hexagon key={i} id={i} data={hexagons[i]} lifePerHex={gameboard.player2Data.lifePerHex} gameStatus={gameboard.gameStatus} />);

    const Wwidth = window.innerWidth;
    const Wheight = window.innerHeight;
    let Gw = 0;
    let Gh = 0;
    const Gproportion = 1.6496;
    if (Wwidth/Wheight < Gproportion) {
      Gw = Wwidth;
      Gh = Wwidth/Gproportion;
      }
      else {
      Gh = Wheight;
      Gw = Gh*Gproportion;
      }
    const GameStyle = {
      width: Gw,
      height: Gh,
      marginLeft: (Wwidth-Gw)/2,
      marginTop: (Wheight-Gh)/2,
    }

    let additional = null;
    if (gameboard.gameStatus=='selected')
      this.distributeLife();
    if (gameboard.gameStatus=='attack_step_1')
      this.attack_step_2();


    return <div id="gameboard" class="gameboard" style={GameStyle}>
      {hexList}
      <PlayerInteraction data={gameboard} />
      <Player player={gameboard.player1Data} gameStatus={gameboard.gameStatus} currentPlayer={gameboard.currentPlayer} />
      <Player player={gameboard.player2Data} gameStatus={gameboard.gameStatus} currentPlayer={gameboard.currentPlayer} />
      {additional}
    </div>
  }

  addLine() {
    const gPosition = document.getElementById('gameboard').getBoundingClientRect();
    let x1 = this.props.hexagons[this.props.gameboard.currentHex].position.x;
    let y1 = this.props.hexagons[this.props.gameboard.currentHex].position.y;
    x1 = (gPosition.width * x1)/100;
    y1 = (gPosition.height * y1)/100;
    x1 += gPosition.width*0.05;
    y1 += gPosition.height*0.07;
    let x2 = x1;
    let y2 = y1;

    var length = Math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
    var angle  = Math.atan2(y2 - y1, x2 - x1) * 180 / Math.PI;
    var transform = 'rotate('+angle+'deg)';
    var lineStyle = {
        transform: transform,
        width: length,
        left: x1+'px',
        top: y1+'px'
    };
    return lineStyle;
  }


  updateLine(x1,y1, x2,y2){
        var length = Math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
        var angle  = Math.atan2(y2 - y1, x2 - x1) * 180 / Math.PI;
        var transform = 'rotate('+angle+'deg)';
        var lineStyle = {
            transform: transform,
            width: length
        };

        document.getElementById('connectionLine').style.transform = lineStyle.transform;
        document.getElementById('connectionLine').style.width = lineStyle.width+'px';


    }
}

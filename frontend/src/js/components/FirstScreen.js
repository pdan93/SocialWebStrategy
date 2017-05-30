import React from "react"
import { connect } from "react-redux"

import {createSocket} from "../actions/firstActions"

@connect((store) => {
  return {
    gameboard : store.gameboard
  };
})
export default class FirstScreen extends React.Component {

  choose() {
    const message = {
      type: "getTwitterUser",
      data: document.getElementById('twitter_user').value
    };
    console.log("sending");
    this.props.gameboard.webSocket.send(JSON.stringify(message));
  }

  createSocket() {
    this.props.dispatch(createSocket(this.props));
  }

  render() {
    const {gameboard, hexagons} = this.props;

    if (gameboard.gameStatus=='zero')
      {
      this.createSocket();
      }
    switch (gameboard.gameStatus) {
      case 'zero':
        return <div id="first_screen">Connecting</div>
        break;
      case 'waiting':
        return <div id="first_screen">Connecting</div>
        break;
      case 'select_twitter_user':
        return <div id="first_screen">
          <input id="twitter_user" type="text" class="awesomeplete" list="mytwitterlist" />
          <button onClick={this.choose.bind(this)}>Choose</button>
        </div>
        break;
      case 'waiting_for_opponent':
        return <div id="first_screen">Waiting for Opponent</div>
        break;
      case 'game_over':
        return <div id="first_screen">{gameboard.gameWon}</div>
        break;
      default:
        return <div id="first_screen">Connecting</div>
    }

  }

}

import React from "react"
import { connect } from "react-redux"

import Gameboard from "./Gameboard"
import FirstScreen from "./FirstScreen"

@connect((store) => {
  return {
      gameboard : store.gameboard
  };
})
export default class Layout extends React.Component {
    render() {
    if (this.props.gameboard.gameStatus=='zero' || this.props.gameboard.gameStatus=='select_twitter_user' || this.props.gameboard.gameStatus=='waiting' || this.props.gameboard.gameStatus=='waiting_for_opponent' || this.props.gameboard.gameStatus=='game_over')
      return <FirstScreen />
      else
      return <Gameboard />
    /*const { user, tweets } = this.props;

    if (!tweets.length) {
      return <button onClick={this.fetchTweets.bind(this)}>load tweets</button>
    }

    const mappedTweets = tweets.map(tweet => <li key={tweet.id}>{tweet.text}</li>)

    return <div>
      <h1>{user.name}</h1>
      <ul>{mappedTweets}</ul>
    </div>*/




  }
}

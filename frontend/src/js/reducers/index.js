import { combineReducers } from "redux"

import tweets from "./tweetsReducer"
import user from "./userReducer"
import gameboard from "./gameboardReducer"

export default combineReducers({
  tweets,
  user,
  gameboard
})

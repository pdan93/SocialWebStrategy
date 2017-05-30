
export function distributeLife(data) {
  setTimeout(function(){
    data = this;
    let totalLife = 0;
    if (data.gameboard.currentPlayer==1)
      totalLife = data.gameboard.player1Data.totalLife;
      else
      totalLife = data.gameboard.player2Data.totalLife;

    let life = totalLife/2;
    let selected_nr = 0;
    for (var i=0; i<data.hexagons.length; i++)
      if (data.hexagons[i].selected)
        selected_nr++;

    const life_per_hex = parseInt(life/selected_nr);

    this.dispatch({
      type: 'DISTRIBUTE_LIFE',
      payload: {
        lifePerHex: life_per_hex,
        remainingLife: (totalLife-(life_per_hex*selected_nr)),
        currentPlayer: data.gameboard.currentPlayer
      }
    });
  }.bind(data),1000);
  return {type: "NONE"};
}

export function attack_step_2(data) {
  setTimeout(function(){
    this.dispatch({
      type: '2_STEP_PHASE_2',
      payload: this.gameboard.step_2
    });
  }.bind(data)
  ,1000);
  return {type: "NONE"};
}


export function mouseUp() {

  return {
    type: 'STOP_DRAG',
    payload: {
    }
  }
}

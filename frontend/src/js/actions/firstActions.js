export function createSocket(data) {
  let socket = new WebSocket("ws://localhost:8888");
  socket.onopen = function(evt) {
    //console.log(evt);
  }
  socket.onmessage = function(evt) {
    data = JSON.parse(evt.data);
    this.dispatch({type: data.type, payload: data.data});
  }.bind(data);


  return {
    type: 'NEW_SOCKET',
    payload: socket,
  }
}

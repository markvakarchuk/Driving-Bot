const WebSocket = require("ws");

const ws = new WebSocket("ws://localhost:8080?bot=true");

ws.on("open", function open() {
  ws.send("Bot Connected");
});

ws.on("message", function incoming(data) {
  console.log(data);
});

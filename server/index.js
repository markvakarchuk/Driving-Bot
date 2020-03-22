const WebSocket = require("ws");
const uuid = require("uuid").v4;
const parse = require("url-parse");
const blessed = require("blessed");
const contrib = require("blessed-contrib");
const screen = blessed.screen();
const moment = require("moment");

var grid = new contrib.grid({ rows: 4, cols: 4, screen: screen });

var log = grid.set(0, 0, 4, 2, blessed.log, { label: "Server Log" });

var bar = grid.set(0, 2, 2, 2, contrib.bar, {
  label: "Connections",
  barWidth: 10,
  barSpacing: 0,
  xOffset: 0,
  maxHeight: 5
});

var table = grid.set(2, 2, 2, 2, contrib.table, {
  keys: true,
  fg: "white",
  selectedFg: "white",
  selectedBg: "blue",
  label: "Messages By ID",
  width: "30%",
  height: "30%",
  border: { type: "line", fg: "cyan" },
  columnSpacing: 10,
  columnWidth: [50, 12]
});

// var bar = contrib.bar({
//   label: "Connections",
//   barWidth: 4,
//   barSpacing: 6,
//   xOffset: 0,
//   maxHeight: 5
// });
// screen.append(bar);

// var log = contrib.log({
//   fg: "green",
//   selectedFg: "green",
//   label: "Server Log"
// });

// screen.append(log);

const wss = new WebSocket.Server({ port: 8080 });

let barGraph = {
  titles: [],
  data: []
};

let messages = {};

function updateBarGraph() {
  barGraph.titles.push(moment().format("h:mm:ss a"));
  barGraph.data.push(wss.clients.size);
  barGraph.titles.splice(0, barGraph.titles.length - 6);
  barGraph.data.splice(0, barGraph.data.length - 6);
  bar.setData(barGraph);
}

wss.on("connection", function connection(ws, req) {
  const {
    query: { bot }
  } = parse(req.url, true);
  ws.id = uuid();
  if (bot) {
    ws.bot = true;
  }
  log.log(ws.id + ":connected:bot=" + Boolean(bot));
  ws.on("message", function incoming(message) {
    //console.log(ws.id, "received:", message);
    log.log(ws.id + ":received:" + message);
    messages[ws.id] = messages[ws.id] + 1 || 1;
    wss.clients.forEach(client => {
      if (client !== ws && client.readyState === WebSocket.OPEN) {
        //console.error("sentTo:", client.id);
        log.log("sentTo:" + client.id);

        client.send(message);
      }
    });
    table.setData({
      headers: ["ID", "Messages"],
      data: Object.keys(messages)
        .sort((a, b) => messages[b] - messages[a])
        .map(key => [key, messages[key]])
    });
  });

  ws.send(ws.id);

  updateBarGraph();
});

wss.on("close", function closed(ws, req) {
  updateBarGraph();
});

screen.key(["escape", "q", "C-c"], function(ch, key) {
  return process.exit(0);
});

screen.render();

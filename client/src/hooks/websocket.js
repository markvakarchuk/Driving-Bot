import { useEffect, useState } from "react";

export default function WebSocketClient(url) {
  const [ws, setws] = useState(null);
  useEffect(() => {
    const ws = new WebSocket("ws://76.104.83.26:9001/");

    ws.onopen = function() {
      console.log("onopen");
    };

    ws.onmessage = function(e) {
      // e.data contains received string.
      console.log("onmessage: " + e.data);
    };
  }, []);

  return [{}, ws];
}

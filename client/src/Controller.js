import React, { useEffect, useState } from "react";
import useWebSocket, { ReadyState } from "react-use-websocket";

const keyCodes = {
  KeyW: "w",
  KeyA: "a",
  KeyS: "s",
  KeyD: "d",
  Space: null
};

export default function Controller() {
  const [sendMessage, lastMessage, readyState, getWebSocket] = useWebSocket(
    "ws://localhost:8080/"
  );

  console.log(lastMessage);

  const connectionStatus = {
    [ReadyState.CONNECTING]: "Connecting",
    [ReadyState.OPEN]: "Open",
    [ReadyState.CLOSING]: "Closing",
    [ReadyState.CLOSED]: "Closed"
  }[readyState];
  console.log(connectionStatus);

  const [currentAction, setCurrentAction] = useState(null);

  useEffect(() => {
    if (ReadyState.OPEN === readyState) {
      sendMessage(currentAction);
    }
  }, [currentAction]);

  const keySelected = e => {
    if (keyCodes[e.code]) {
      setCurrentAction(keyCodes[e.code]);
    }
  };

  const keyDeselect = e => {
    console.log(keyCodes[e.code], currentAction);
    if (keyCodes[e.code] === currentAction) {
      setCurrentAction(null);
    }
  };

  useEffect(() => {
    document.addEventListener("keypress", keySelected);

    return () => document.removeEventListener("keypress", keySelected);
  }, []);

  //! Stop on button release
  useEffect(() => {
    document.addEventListener("keyup", keyDeselect);

    return () => document.removeEventListener("keyup", keyDeselect);
  }, [currentAction]);

  return <div>{currentAction}</div>;
}

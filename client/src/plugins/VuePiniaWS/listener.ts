import { DefaultEventsMap } from "@socket.io/component-emitter";
import { Socket } from "socket.io-client";
import Emitter from "./emitter";

export default class Listener {
  static staticEvents = [
    "connect",
    "error",
    "disconnect",
    "reconnect",
    "reconnect_attempt",
    "reconnecting",
    "reconnect_error",
    "reconnect_failed",
    "connect_error",
    "connect_timeout",
    "connecting",
    "ping",
    "pong",
  ];

  emitter: Emitter;

  constructor(emitter: Emitter) {
    this.emitter = emitter;
  }

  register(io: Socket<DefaultEventsMap, DefaultEventsMap>) {
    io["onevent"] = (packet: { data: any }) => {
      const event = packet.data[0];
      let [, ...args] = packet.data;
      if (args.length === 1) args = args[0];

      this.onEvent(event, args);
    };
    Listener.staticEvents.forEach((event) =>
      io.on(event, (args) => this.onEvent(event, args))
    );
  }

  onEvent(event: string, args: any) {
    this.emitter.emit(event, args);
  }
}

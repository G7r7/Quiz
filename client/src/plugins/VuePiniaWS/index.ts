import Listener from "./listener";
import Emitter from "./emitter";
import SocketIO, { Socket } from "socket.io-client";
import { StoreDefinition } from "pinia";
import { DefaultEventsMap } from "@socket.io/component-emitter";
import Mixin from "./mixin";

export interface pinia {
  store?: StoreDefinition;
  actionPrefix?: string;
  options?: {
    useConnectionNamespace?: boolean;
  };
}

interface VuePiniaWSOptions {
  connection: string;
  pinia?: pinia;
  // type declarations for optional options
  options?: {
    path?: string;
  };
}

export default class VuePiniaWS {
  io: Socket<DefaultEventsMap, DefaultEventsMap> | undefined;
  emitter: Emitter;
  listener: Listener;
  options: { path?: string } | undefined;
  connection: string;

  constructor({ connection, pinia, options }: VuePiniaWSOptions) {
    this.io = undefined;
    this.options = options;
    this.connection = connection;
    this.emitter = new Emitter(pinia);
    this.listener = new Listener(this.emitter);
  }

  install(Vue: any) {
    const version = Number(Vue.version.split(".")[0]);

    if (version >= 3) {
      Vue.provide("vuePiniaWS", this);
      Vue.config.globalProperties.vuePiniaWS = this;
    } else {
      Vue.prototype.$socket = this.io;
      Vue.prototype.$vuePiniaWS = this;
    }

    Vue.mixin(Mixin);
  }

  connect(connection: string, options: { path?: string } | undefined) {
    if (connection && typeof connection === "object") {
      return connection;
    } else if (typeof connection === "string") {
      return (this.io = SocketIO(connection, options));
    } else {
      throw new Error("Unsupported connection type");
    }
  }

  mount() {
    this.io = this.connect(this.connection, this.options);
    this.listener.register(this.io);
  }
}

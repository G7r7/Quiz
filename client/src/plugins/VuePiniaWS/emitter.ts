import { mapActions, Store, StoreDefinition } from "pinia";
import { pinia } from "./index";

interface listener {
  callback: any;
  component: any;
}

export default class Emitter {
  store: StoreDefinition | undefined;
  actionPrefix: string;
  listeners: Map<string, listener[]>;
  constructor(pinia: pinia | undefined) {
    this.store = pinia?.store;
    this.actionPrefix = pinia?.actionPrefix ? pinia.actionPrefix : "SOCKET_";
    this.listeners = new Map();
  }

  addListener(event: string, callback: any, component: any) {
    if (typeof callback === "function") {
      if (!this.listeners.has(event)) this.listeners.set(event, []);
      this.listeners.get(event)?.push({ callback, component });
    } else {
      throw new Error(`callback must be a function`);
    }
  }

  removeListener(event: string, component: any) {
    if (this.listeners.has(event)) {
      const listeners = this.listeners
        .get(event)
        ?.filter((listener: listener) => listener.component !== component);

      if (listeners && listeners.length > 0) {
        this.listeners.set(event, listeners);
      } else {
        this.listeners.delete(event);
      }
    }
  }

  emit(event: string, args: any) {
    if (this.listeners.has(event)) {
      this.listeners.get(event)?.forEach((listener) => {
        listener.callback.call(listener.component, args);
      });
    }

    if (event !== "ping" && event !== "pong") {
      this.dispatchStore(event, args);
    }
  }

  dispatchStore(event: string, args: any) {
    if (this.store != undefined) {
      const s = this.store();
      const keys = Object.keys(s).filter(
        (key: string) => !key.startsWith("_") && !key.startsWith("$")
      );

      const fns: any[] = keys
        .map((key) => s[key])
        .filter((fn) => typeof fn === "function");

      if (s && fns && fns.length > 0) {
        const prefixed_event = this.actionPrefix + event;

        for (const key in fns) {
          const action = key.split("/").pop();

          if (action === prefixed_event) {
            s[key](args);
          }
        }
      }
    }
  }
}

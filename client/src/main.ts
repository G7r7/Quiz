import { createApp } from "vue";
import App from "./App.vue";
import VuePiniaWS from "./plugins/VuePiniaWS";
import { createPinia } from "pinia";
import useQuizStore from "./stores/useQuizStore";

const app = createApp(App);
app.use(createPinia());
app.use(
  new VuePiniaWS({
    connection: "http://localhost:7000",
    pinia: { store: useQuizStore, actionPrefix: "" },
  })
);
app.mount("#app");

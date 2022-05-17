import { createApp } from "vue";
import App from "./App.vue";
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import "@mdi/font/css/materialdesignicons.css";
import { aliases, mdi } from "vuetify/iconsets/mdi";
import { fa } from "vuetify/iconsets/fa";
import VuePiniaWS from "./plugins/VuePiniaWS";
import { createPinia } from "pinia";
import useQuizStore from "./stores/useQuizStore";

const app = createApp(App);
const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: "mdi",
    sets: {
      fa,
      mdi,
    },
  },
});

app.use(vuetify);

app.use(createPinia());
app.use(
  new VuePiniaWS({
    connection: "http://localhost:7000",
    pinia: { store: useQuizStore, actionPrefix: "" },
  })
);
app.mount("#app");

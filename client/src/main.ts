import { createApp } from "vue";
import App from "./App.vue";
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import "@mdi/font/css/materialdesignicons.css";
import { aliases, mdi } from "vuetify/iconsets/mdi";
import { fa } from "vuetify/iconsets/fa";

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

app.mount("#app");

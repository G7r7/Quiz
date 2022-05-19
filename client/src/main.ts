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
import { createRouter, createWebHashHistory } from "vue-router";
import HelloWorld from "./components/HelloWorld.vue";
import Lobby from "./pages/Lobby.vue";

const routes = [
  { path: "/", component: Lobby },
  { path: "/signin", component: { template: "<div>Signin</div>" } },
  { path: "/signup", component: { template: "<div>Signup</div>" } },
  { path: "/lobby/:id", component: { template: "<div>Lobby</div>" } },
  { path: "/quiz/:id", component: { template: "<div>Quiz</div>" } },
  { path: "/quiz/create", component: { template: "<div>Create Quiz</div>" } },
  { path: "/quiz/update", component: { template: "<div>Signin</div>" } },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

const app = createApp(App);

app.use(router);

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

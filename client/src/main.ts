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
import Lobby from "./pages/Lobby.vue";
import FormUser from "./components/FormUser.vue";
import FormQuiz from "./components/FormQuiz.vue";
import EndQuiz from "./components/EndQuiz.vue";
import CreateRoom from "./pages/CreateRoom.vue";
import GameLobby from "./pages/GameLobby.vue";
import Question from "./components/Question.vue";

const routes = [
  { path: "/", component: Lobby },
  { path: "/signin", component: FormUser },
  { path: "/signup", component: FormUser },
  { path: "/lobby/create", component: CreateRoom },
  { path: "/lobby/:id", component: GameLobby },
  { path: "/quiz/:id", component: Question },
  { path: "/quiz/create", component: FormQuiz },
  { path: "/quiz/update", component: { template: "<div>Signin</div>" } },
  { path: "/quiz/end", component: EndQuiz },
];

export const router = createRouter({
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
    connection: "http://localhost:5000",
    pinia: { store: useQuizStore, actionPrefix: "" },
    options: { path: "/ws/socket.io/" },
  })
);
app.mount("#app");

<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import { inject } from "vue";
import { useRouter } from "vue-router";
import { DefaultService, OpenAPI } from "./providers";
import useQuizStore from "./stores/useQuizStore";
const vuePiniaWS: any = inject("vuePiniaWS");
vuePiniaWS.mount();
OpenAPI.BASE = import.meta.env.VITE_API_ENDPOINT;

const store = useQuizStore();
const token = window.localStorage.getItem("TOKEN");

if (token) {
  store.isSignedIn = true;
  OpenAPI.TOKEN = token;
  (async () => {
    try {
      const me = await DefaultService.userMeUsersMePost();
      store.name = me.user_name;
      store.userId = me.id;
    } catch (error) {
      store.isSignedIn = false;
      OpenAPI.TOKEN = "";
      window.localStorage.setItem("TOKEN", "");
    }
  })();
}
store.io = vuePiniaWS.io;
const router = useRouter();

const signin = () => {
  router.push("/signin");
};

const signup = () => {
  router.push("/signup");
};

const lobby = () => {
  router.push("/");
};

const createQuiz = () => {
  router.push("/quiz/create");
};
</script>

<template>
  <!-- <Question
    :props="{
      question: {
        quiz_id: 0,
        id: 0,
        content: 'Bonjour comment allez-vous ?',
        multipleAnswers: false,
        answers: [
          { question_id: 0, id: 1, content: 'lorem ipsum', is_true: true },
          { question_id: 0, id: 2, content: 'lorem ipsum', is_true: true },
          { question_id: 0, id: 3, content: 'lorem ipsum', is_true: false },
        ],
      },
    }"
  /> -->
  <v-card class="mx-auto">
    <v-layout>
      <v-app-bar color="primary" density="compact">
        <v-app-bar-title @click="lobby">Quizie</v-app-bar-title>
        <template v-slot:append>
          <v-btn
            v-if="!store.isSignedIn"
            icon="mdi-login"
            @click="signin"
          ></v-btn>
          <v-btn
            v-if="!store.isSignedIn"
            icon="mdi-account-plus"
            @click="signup"
          ></v-btn>
          <v-btn v-if="store.isSignedIn" @click="createQuiz"
            >Créer un Quiz</v-btn
          >
        </template>
      </v-app-bar>

      <v-main>
        <v-container fluid>
          <router-view :key="$route.fullPath"></router-view>
        </v-container>
      </v-main>
    </v-layout>
  </v-card>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

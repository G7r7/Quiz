<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import { inject } from "vue";
import { useRoute } from "vue-router";
import Question from "./components/Question.vue";
import useQuizStore from "./stores/useQuizStore";
const vuePiniaWS: any = inject("vuePiniaWS");
vuePiniaWS.mount();
const store = useQuizStore();
store.io = vuePiniaWS.io;
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
        <template v-slot:prepend>
          <v-app-bar-nav-icon></v-app-bar-nav-icon>
        </template>
        <v-app-bar-title>Quizie</v-app-bar-title>
        <template v-slot:append>
          <v-btn icon="mdi-dots-vertical"></v-btn>
        </template>
      </v-app-bar>

      <v-main>
        <v-container fluid>
          <v-row dense>
            <!-- <v-col v-for="n in 8" :key="n" cols="3">
              <v-sheet color="grey-lighten-2" height="96"></v-sheet>
            </v-col> -->
            <router-view></router-view>
          </v-row>
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

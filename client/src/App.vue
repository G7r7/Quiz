<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import Question from "./components/Question.vue";
import useQuizStore from "./stores/useQuizStore";
import FormUser from "./components/FormUser.vue";

const store = useQuizStore();
</script>

<template>
  <Question
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
  />
  <FormUser :props="{ signin: false }" />
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

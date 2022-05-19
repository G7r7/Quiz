<script setup lang="ts">
import { ref } from "vue";
import useQuizStore from "../stores/useQuizStore";
import { useRouter } from "vue-router";
const router = useRouter();

const home = () => {
  router.push("/");
};

const store = useQuizStore();
</script>

<template>
  <v-container>
    <v-row justify="center">
      <v-col md="4">
        <v-card :title="store.quizName + ' Finished'" class="ma-4"></v-card>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-container
        v-for="(player, index) in store.players"
        :key="player.userId"
        md="8"
      >
        #{{ index + 1 }}
        <v-avatar color="info">
          <v-icon icon="mdi-account-circle"></v-icon>
        </v-avatar>
        PlayerName
      </v-container>
    </v-row>
    <v-row justify="end">
      <v-col md="8">
        <v-btn color="success" size="large" @click="home">
          <v-icon start icon="mdi-home"></v-icon>Go to Home</v-btn
        >
      </v-col>
    </v-row>
  </v-container>
</template>

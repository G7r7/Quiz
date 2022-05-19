<script setup lang="ts">
import useQuizStore from "../stores/useQuizStore";
import { useRoute } from "vue-router";
import { ref } from "vue";
const store = useQuizStore();
const route = useRoute();
const path = ref(window.location.href);
</script>

<template>
  <a :href="route.path">{{ path }}</a>
  <v-list lines="one">
    <v-list-subheader inset>Liste des joueurs</v-list-subheader>

    <v-list-item
      v-for="player in store.players"
      :key="player.userId"
      :title="player.name"
    >
    </v-list-item>
  </v-list>
  <v-btn v-if="store.isRoomAdmin" @click="store.launchGame">Launch Game</v-btn>
</template>

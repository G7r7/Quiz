<script setup lang="ts">
import useQuizStore from "../stores/useQuizStore";
import { useRouter, useRoute } from "vue-router";
import { ref, watch } from "vue";
import { computed, reactive } from "@vue/reactivity";
const store = useQuizStore();
const route = useRoute();
const router = useRouter();
const path = ref(window.location.href);
if (!store.isGameJoined) {
  store.isGameJoined = true;
  store.joinLobby(route.params.id as string);
}
let loading = ref(false);
const launchGame = () => {
  loading.value = true
  store.launchGame()
}
</script>

<template>
  <a :href="route.path">{{ path }}</a>
  <v-list lines="three">
    <v-list-subheader inset>Liste des joueurs</v-list-subheader>

    <v-list-item
      v-for="player in (store.players as any)"
      :key="player"
      :title="player"
    >
    </v-list-item>
  </v-list>
  <v-btn color="primary" v-if="store.isRoomAdmin" @click="launchGame" :disabled="loading">
    <span v-if="loading">Chargement <v-progress-circular size="20" indeterminate></v-progress-circular></span>
    <span v-else>Démarrer le quiz</span>
  </v-btn>
</template>

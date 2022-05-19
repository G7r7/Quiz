<script lang="ts">
import useQuizStore from "../stores/useQuizStore";
import { mapStores } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  computed: {
    ...mapStores(useQuizStore),
  },
});
</script>

<template>
  <v-card class="mx-auto">
    <h1>Game Lobby</h1>
  </v-card>
</template>

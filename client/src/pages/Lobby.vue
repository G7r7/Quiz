<script lang="ts">
import useQuizStore from "../stores/useQuizStore";
import { mapStores } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  computed: {
    ...mapStores(useQuizStore),
  },
  sockets: {
    quizjoin() {
      this.$router.push({ path: `/lobby/${this.QuizStore.lobbyToken}` });
    },
  },
});
</script>

<template>
  <v-card class="mx-auto">
    <v-form ref="form">
      <v-text-field
        v-model="QuizStore.name"
        label="Nom du joueur"
      ></v-text-field>
    </v-form>
    <v-list lines="three">
      <v-list-subheader inset>Liste des lobbies</v-list-subheader>

      <v-list-item
        v-for="lobby in QuizStore.lobbies"
        :key="lobby.lobbyToken"
        :title="lobby.quizName"
        :subtitle="`${lobby.numberPlayers} joueurs || Code d'invitation : ${lobby.lobbyToken}`"
      >
        <template v-slot:append>
          <v-list-item-avatar end>
            <v-btn
              variant="text"
              color="grey lighten-1"
              icon="mdi-arrow-right-bold-circle"
              @click="() => QuizStore.joinLobby(lobby.lobbyToken)"
            ></v-btn>
          </v-list-item-avatar>
        </template>
      </v-list-item>
    </v-list>
    <v-btn color="success">Créer une room</v-btn>
  </v-card>
</template>

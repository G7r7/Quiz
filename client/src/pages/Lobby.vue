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
  methods: {
    createRoom() {
      this.$router.push("/lobby/create");
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
        v-for="lobby in (QuizStore.lobbies as any)"
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
    <v-btn v-if="QuizStore.isSignedIn" color="success" @click="createRoom"
      >Créer une room</v-btn
    >
  </v-card>
</template>

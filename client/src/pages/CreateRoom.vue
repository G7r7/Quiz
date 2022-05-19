<script setup lang="ts">
import { computed, ref } from "vue";
import { useRouter } from "vue-router";
import { DefaultService } from "../providers";
import useQuizStore from "../stores/useQuizStore";
const store = useQuizStore();
DefaultService.getQuizsQuizListUserIdGet(store.userId).then((quizes) => {
  store.userQuizes = quizes.map(({ date_creation, id, quiz_name }) => ({
    quiz_name,
    date_creation,
    id: Number(id),
  }));
});
const router = useRouter();
const select = ref("");
const validate = async () => {
  const index = store.userQuizes.findIndex(
    (quiz) => quiz.quiz_name === select.value
  );
  const id = store.userQuizes[index].id;
  const response = await DefaultService.generateTokenTokenPost(
    store.userId,
    id
  );
  store.lobbyToken = response.player_token;
  store.isRoomAdmin = true;
  store.adminToken = response.admin_token;
  store.quizName = store.userQuizes[index].quiz_name;
  store.addRoom(store.lobbyToken);
  router.push(`/lobby/${store.lobbyToken}`);
};
const items = computed(() => {
  return store.userQuizes.map((quiz) => quiz.quiz_name);
});

const valid = computed(() => {
  return !!select.value;
});
</script>
<template>
  <v-form ref="form" lazy-validation>
    <v-select
      v-model="select"
      :items="items"
      :rules="[(v:any) => !!v || 'Item is required']"
      label="Quiz"
      required
    ></v-select>

    <v-btn :disabled="!valid" color="success" class="mr-4" @click="validate">
      Créer une room
    </v-btn>
  </v-form>
</template>

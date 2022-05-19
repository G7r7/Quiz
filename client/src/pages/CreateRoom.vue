<script setup lang="ts">
import { storeToRefs } from "pinia";
import { computed, ref } from "vue";
import useQuizStore from "../stores/useQuizStore";
const store = useQuizStore();
const select = ref("");
const items: string[] = [];
const validate = () => {};
// const items = computed(() => {
//   return store.userQuizes;
// });
</script>
<template>
  <v-form ref="form" lazy-validation>
    <v-select
      v-model="select"
      :items="items"
      :rules="[(v:any) => !!v || 'Item is required']"
      label="Item"
      required
    ></v-select>

    <v-btn color="success" class="mr-4" @click="validate"> Validate </v-btn>
  </v-form>
</template>

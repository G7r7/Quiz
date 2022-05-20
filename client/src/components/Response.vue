<script setup lang="ts">
import { computed } from "vue";
import { QuizResponse } from "../model/QuizResponse";
import useQuizStore from "../stores/useQuizStore";

interface ResponseProps {
  response: QuizResponse;
  multipleResponse: boolean;
  selected: string[];
}
const store = useQuizStore();
const props2 = defineProps<{ props: ResponseProps }>();
const isFinished = computed(() => store.correctResponse.length > 0);
const correct = computed(() =>
  store.correctResponse.includes(props2.props.response.id)
);
const color = computed(() =>
  isFinished.value ? (correct.value ? "success" : "error") : "primary"
);

const style = computed(() =>
  isFinished.value ? (correct.value ? "green" : "red") : "black"
);
</script>

<template>
  <v-radio :color="color" :value="props.response.id">
    <template #label>
      <span :style="`color : ${style};`">{{ props.response.content }}</span>
    </template>
  </v-radio>
</template>

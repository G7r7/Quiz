<script setup lang="ts">
import { QuizResponse } from "../model/QuizResponse";

interface ResponseProps {
  response: QuizResponse;
  multipleResponse: boolean;
  selected: string[];
}

defineProps<{ props: ResponseProps }>();
</script>

<template>
  <v-checkbox
    v-if="props.multipleResponse"
    :v-model="props.selected"
    :label="props.response.content"
    :value="props.response.id"
  />
  <v-radio v-else :label="props.response.content" :value="props.response.id" />
</template>

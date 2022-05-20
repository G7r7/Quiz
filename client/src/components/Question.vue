<script setup lang="ts">
import { ref } from "vue";
import { Question } from "../model/Question";
import Response from "./Response.vue";
import { inject } from "vue";
import useQuizStore from "../stores/useQuizStore";
import { computed } from "@vue/reactivity";

const store = useQuizStore();

const selected = ref([]);

function handleValidation() {
  store.respondQuestion(selected.value["0"]);
  store.hasResponded = true;
}
const progress = computed(() => 10 - store.timer);
</script>

<template>
  <v-container>
    <div v-if="store.timer !== 0">{{ store.timer }}</div>
    <v-progress-linear
      v-if="store.timer !== 0"
      max="10"
      :model-value="progress"
    />
    <v-row justify="center">
      <v-col md="8">
        <v-card :title="store.question.question.content" class="ma-8"></v-card>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col md="8">
        <v-container>
          <v-row
            class="ml-6"
            v-for="response in store.question.responses"
            :key="response.id"
          >
            <v-col md="4">
              <v-radio-group v-model="selected">
                <Response
                  :props="{
                    response: response,
                    multipleResponse: false,
                    selected: selected,
                  }"
                />
              </v-radio-group>
            </v-col>
          </v-row>
        </v-container>
      </v-col>
    </v-row>
    <v-row justify="end">
      <v-col md="8">
        <v-btn
          :disabled="store.hasResponded"
          @click="handleValidation"
          color="success"
          size="large"
        >
          <v-icon start icon="mdi-check"></v-icon>valider</v-btn
        >
      </v-col>
    </v-row>
  </v-container>
</template>

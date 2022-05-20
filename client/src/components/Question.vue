<script setup lang="ts">
import { ref } from "vue";
import { Question } from "../model/Question";
import Response from "./Response.vue";
import { inject } from "vue";
import useQuizStore from "../stores/useQuizStore";

const store = useQuizStore();

const selected = ref([]);

function handleValidation() {
  store.respondQuestion(selected.value["0"]);
  store.hasResponded = true;
}
</script>

<template>
  <v-container>
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
              <!-- <Response
                v-if="props.question.multipleAnswers"
                :props="{
                  response: response,
                  multipleResponse: props.question.multipleAnswers,
                  selected: selected,
                }"
              /> -->
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

<script setup lang="ts">
import { ref } from "vue";
import { Question } from "../model/Question";
import Response from "./Response.vue";

interface QuestionProps {
  question: Question;
}
defineProps<{ props: QuestionProps }>();

const selected = ref([]);

function handleValidation(event: any) {
  console.log(event.target.value);

  //todo send to server
}
</script>

<template>
  <v-container>
    <v-row justify="center">
      <v-col md="8">
        <v-card :title="props.question.content" class="ma-8"></v-card>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col md="8">
        <v-container>
          <v-row
            class="ml-6"
            v-for="response in props.question.answers"
            :key="response.id"
          >
            <v-col md="4">
              <Response
                v-if="props.question.multipleAnswers"
                :props="{
                  response: response,
                  multipleResponse: props.question.multipleAnswers,
                  selected: selected,
                }"
              />
              <v-radio-group v-else v-model="selected">
                <Response
                  :props="{
                    response: response,
                    multipleResponse: props.question.multipleAnswers,
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
        <v-btn @clic="handleValidation" color="success" size="large">
          <v-icon start icon="mdi-check"></v-icon>valider</v-btn
        >
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";
import { Quiz } from "../model/Quiz";
import { DefaultService } from "../providers";
import useQuizStore from "../stores/useQuizStore";
const router = useRouter();

const home = () => {
  router.push("/");
};
const store = useQuizStore();

let quiz = ref<Quiz>({
  name: "",
  user_id: store.userId,
  date_creation: new Date(Date.now()),
  questions: [],
});

const nameRules = [
  (v: any) => !!v || "Name is required",
  (v: any) => (v && v.length <= 100) || "Name must be less than 100 characters",
];

const valid = ref(true);
const form = ref<any>(null);
const isCreate = ref(false);

async function handleSubmit(validate: any) {
  const validation = await validate;

  if (validation.valid) {
    const newQuiz = await DefaultService.createQuizQuizPost({
      quiz_name: quiz.value.name,
      user_id: store.userId,
      date_creation: [
        quiz.value.date_creation.getFullYear(),
        quiz.value.date_creation.getMonth(),
        quiz.value.date_creation.getDay(),
      ].join("-"),
    });
    const promises = [];
    for (const question of quiz.value.questions) {
      promises.push(
        DefaultService.createQuestionQuestionPost({
          number_question: quiz.value.questions.length,
          quiz_id: parseInt(newQuiz.id),
          content: question.content,
        }).then((newQuestion) => {
          for (const response of question.answers) {
            DefaultService.createResponseResponsePost({
              question_id: newQuestion.id,
              content: response.content,
              is_true: response.is_true,
            });
          }
        })
      );
    }

    try {
      await Promise.all(promises);
      isCreate.value = true;
    } catch (error) {
      console.log(error);
    }
  }
}
</script>

<template>
  <div v-if="!isCreate">
    <v-form ref="form" v-model="valid" lazy-validation>
      <v-container>
        <v-row justify="center">
          <v-col md="10">
            <v-text-field
              v-model="quiz.name"
              :rules="nameRules"
              label="Quiz name"
              required
            ></v-text-field></v-col
        ></v-row>
        <v-row justify="center">
          <v-col md="9">
            <v-container
              v-for="question in quiz.questions"
              :key="question.id"
              class="rounded-pill"
            >
              <v-row>
                <v-text-field
                  label="Question"
                  v-model="question.content"
                  class="ma-4"
                  required
                ></v-text-field>
              </v-row>
              <v-row>
                <v-col md="7">
                  <v-container
                    v-for="response in question.answers"
                    :key="response.id"
                  >
                    <v-row>
                      <v-text-field
                        v-model="response.content"
                        label="Answer"
                        require
                      ></v-text-field>
                    </v-row>
                    <v-row>
                      <v-checkbox label="Is true" v-model="response.is_true"
                    /></v-row>
                  </v-container>
                </v-col>
              </v-row>
              <v-row justify="end">
                <v-col>
                  <v-btn
                    color="success"
                    size="large"
                    @click="
                      (event) => {
                        question.answers.push({
                          question_id: -1,
                          id: -1,
                          content: '',
                          is_true: false,
                        });
                      }
                    "
                    ><v-icon start icon="mdi-plus-circle"></v-icon>Add
                    answers</v-btn
                  ></v-col
                >
              </v-row>
            </v-container>
          </v-col>
        </v-row>
        <v-row justify="end">
          <v-col>
            <v-btn
              @click="
                (event) => {
                  quiz.questions.push({
                    quiz_id: -1,
                    id: -1,
                    content: '',
                    multipleAnswers: false,
                    answers: [],
                  });
                }
              "
              ><v-icon start icon="mdi-plus-circle"></v-icon>Add Question</v-btn
            >
          </v-col>
        </v-row>
        <v-row v-if="!isCreate" justify="end">
          <v-col md="8">
            <v-btn
              color="success"
              size="large"
              :valid="!isCreate"
              class="mr-4"
              @click="
                (event) => {
                  handleSubmit(form.validate());
                }
              "
              >Créer</v-btn
            >
          </v-col>
        </v-row>
      </v-container>
    </v-form>
  </div>
  <div v-else>
    <v-container>
      <v-row justify="end">
        <v-col md="4">
          <v-alert type="success">Quiz created !</v-alert>
        </v-col>
        <v-col md="4">
          <v-btn @click="home">Return to home</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

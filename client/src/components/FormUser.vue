<script setup lang="ts">
import { ref } from "vue";
import { ApiError, DefaultService } from "../providers";
import { useRoute, useRouter } from "vue-router";
import { computed } from "vue";
import useQuizStore from "../stores/useQuizStore";
import { OpenAPI } from "../providers";
const route = useRoute();
const router = useRouter();

const isSignin = computed(() => {
  return route.path === "/signin";
});

const user = ref({ name: "", password: "" });
const nameRules = [
  (v: any) => !!v || "Name is required",
  (v: any) => (v && v.length <= 100) || "Name must be less than 100 characters",
];
const passwordRules = [
  (v: any) => (v && v.length >= 8) || "At least 8 characters",
  (v: any) => (v && v.length <= 100) || "Name must be less than 100 characters",
];
const valid = ref(true);
const showPass = ref(false);
const store = useQuizStore();
let error = ref("");
async function handleValidation() {
  try {
    const newUser = await DefaultService.createUserUsersPost({
      user_name: user.value.name,
      user_password: user.value.password,
    });

    const log = await DefaultService.logUserUsersLoginPost({
      user_name: user.value.name,
      user_password: user.value.password,
    });
    OpenAPI.TOKEN = log.user_token;
    window.localStorage.setItem("TOKEN", log.user_token);
    store.userId = newUser.id;
    store.isSignedIn = true;
    store.name = newUser.user_name;
    router.push("/");
  } catch (err: any) {
    store.isSignedIn = false;
    OpenAPI.TOKEN = "";
    window.localStorage.setItem("TOKEN", "");
    error.value = err.body.detail;
    console.error("Failed to create user !");
  }
}

async function handleConnexion() {
  try {
    const log = await DefaultService.logUserUsersLoginPost({
      user_name: user.value.name,
      user_password: user.value.password,
    });
    OpenAPI.TOKEN = log.user_token;
    window.localStorage.setItem("TOKEN", log.user_token);
    store.userId = log.id;
    store.isSignedIn = true;
    store.name = log.user_name;
    router.push("/");
  } catch (err: any) {
    store.isSignedIn = false;
    OpenAPI.TOKEN = "";
    window.localStorage.setItem("TOKEN", "");
    error.value = err.body.detail;
    console.error("Failed to log in.");
  }
}
</script>

<template>
  <v-form ref="form" v-model="valid" lazy-validation>
    <v-container>
      <v-row justify="center">
        <v-col md="8">
          <v-text-field
            v-model="user.name"
            :rules="nameRules"
            label="Name"
            required
          ></v-text-field></v-col
      ></v-row>
      <v-row justify="center">
        <v-col md="8">
          <v-text-field
            v-model="user.password"
            :append-icon="showPass ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="passwordRules"
            :type="showPass ? 'text' : 'password'"
            label="Password"
            required
            @click:append="showPass = !showPass"
          ></v-text-field></v-col
      ></v-row>
      <v-row justify="end">
        <v-col md="8">
          <v-btn
            v-if="isSignin"
            :disabled="!valid"
            color="success"
            size="large"
            class="mr-4"
            @click="handleConnexion"
          >
            Sign in
          </v-btn>
          <v-btn
            v-else
            :disabled="!valid"
            color="success"
            size="large"
            class="mr-4"
            @click="
              (event) => {
                handleValidation();
              }
            "
            >Sign up</v-btn
          >
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-alert v-if="error != ''" type="error">{{ error }}</v-alert>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

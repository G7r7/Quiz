<script setup lang="ts">
import { ref } from "vue";
import { DefaultService } from "../providers";

interface formUserProps {
  signin: boolean;
}

defineProps<{ props: formUserProps }>();

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
async function handleValidation() {
  const newUser = await DefaultService.createUserUsersPost({
    user_name: user.value.name,
    user_password: user.value.password,
  });
}

async function handleConnexion() {
  //
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
            v-if="props.signin"
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
            @click="handleValidation"
            >Sign up</v-btn
          >
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

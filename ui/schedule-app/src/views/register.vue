<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-back-button default-href="/login"></ion-back-button>
        </ion-buttons>
        <ion-title>Crie sua conta</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="false" mode="md">
      <div class="form-container">
        <form @submit.prevent="onSubmit">
          <div class="input-container">
            <ion-input
              label="Primeiro Nome"
              label-placement="stacked"
              v-model="form.first_name"
              @keydown="blockNumbers($event)"
              type="text"
              fill="outline"
              :clear-input="true"
            />
          </div>
          <div class="input-container">
            <ion-input
              label="Último Nome"
              label-placement="stacked"
              v-model="form.last_name"
              @keydown="blockNumbers($event)"
              type="text"
              fill="outline"
              :clear-input="true"
            />
          </div>
          <div class="input-container">
            <ion-input
              ref="emailInput"
              label="Email"
              helper-text="Ex: samuel@gmail.com"
              error-text="Email Inválido"
              v-model="form.email"
              type="email"
              placeholder="Seu email"
              label-placement="stacked"
              fill="outline"
              :clear-input="true"
            />
          </div>
          <div class="input-container">
            <ion-input
              label="Senha"
              helper-text="No mínimo 8 caracteres"
              v-model="form.password"
              type="password"
              autocomplete="new-password"
              placeholder="Crie uma senha"
              label-placement="stacked"
              fill="outline"
              :clear-input="true"
            />
          </div>
          <div class="input-container">
            <ion-input
              label="Endereço"
              v-model="form.address"
              type="text"
              autocomplete="street-address"
              placeholder="Seu endereço"
              label-placement="stacked"
              fill="outline"
              :clear-input="true"
            />
          </div>
          <div class="input-container">
            <ion-input
              ref="phoneInput"
              label="Telefone"
              error-text="Número Inválido"
              v-model="form.phone_number"
              type="tel"
              placeholder="(00) 00000-0000"
              label-placement="stacked"
              fill="outline"
              :clear-input="true"
            />
          </div>

          <ion-button type="submit" expand="block" class="submit-btn">
            Cadastrar
          </ion-button>
          <ion-note color="danger" v-if="errorExists">{{
            errorMessage
          }}</ion-note>
        </form>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { reactive, ref } from "vue";
import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonInput,
  IonButton,
  IonBackButton,
  IonButtons,
  IonNote,
} from "@ionic/vue";
import router from "@/router";
import apiClient from "@/services/apiClient";

//TODO: fix validações dos inputs, tá querbrado do phone

const form = reactive({
  first_name: "",
  last_name: "",
  email: "",
  password: "",
  address: "",
  phone_number: "",
});

const errorExists = ref<boolean>(false);
const errorMessage = ref<string>("");
const emailInput = ref<InstanceType<typeof IonInput> | null>(null);
const phoneInput = ref<InstanceType<typeof IonInput> | null>(null);

function blockNumbers(ev: any) {
  const char = ev.key;
  if (!/^[a-zA-Z\s]$/.test(char) && ev.key !== "Backspace") {
    ev.preventDefault();
  }
}

function handleSubmit() {
  errorExists.value = false;
  return router.replace("/login");
}

function hideError(): void {
  errorExists.value = false;
}

function handleEmailInput(value: string): string {
  let input = value
    .replace(/\s/g, "")
    .replace(/@+/g, "@")
    .replace(/@(.+)?@/, "@$1")
    .replace(/(\..+)?\./, ".$1");
  return input;
}

async function onSubmit(): Promise<void> {
  const formattedFirstName = form.first_name.replace(/\s+/g, " ").trim();
  const formattedLastName = form.last_name.replace(/\s+/g, " ").trim();
  // const formattedPhoneNumber = handlePhoneInput(form.phone_number);
  form.email = handleEmailInput(form.email);

  console.log(formattedFirstName);
  console.log(formattedLastName);
  console.log(form.phone_number);
  console.log(form.email);

  if (
    !form.first_name ||
    !form.last_name ||
    !form.email ||
    !form.password ||
    !form.address ||
    !form.phone_number
  ) {
    errorExists.value = true;
    errorMessage.value = "Preencha todos os campos.";
    setTimeout(hideError, 3000);
    return;
  }

  try {
    await apiClient.registerUser({
      ...form,
      first_name: formattedFirstName,
      last_name: formattedLastName,
      // phone_number: phoneDigits,
    });
    form.first_name = "";
    form.last_name = "";
    form.email = "";
    form.password = "";
    form.address = "";
    form.phone_number = "";
    await handleSubmit();
  } catch (error: any) {
    errorExists.value = true;
    setTimeout(hideError, 3000);
    errorMessage.value =
      error?.response?.data || "Falha ao cadastrar. Tente novamente.";
    if (error.response) {
      console.error("Resposta do servidor:", error.response?.data?.detail);
    }
  }
}
</script>

<style scoped>
.form-container {
  max-width: 640px;
  margin: 0 auto;
  padding: 20px;
}

h2 {
  margin: 8px 0 16px;
  font-size: 20px;
  font-weight: 600;
  color: var(--ion-color-primary);
}

.input-container {
  margin-top: 25px;
  margin-bottom: 25px;
}

.submit-btn {
  margin-top: 16px;
}

ion-note {
  font-size: 12px;
}
</style>

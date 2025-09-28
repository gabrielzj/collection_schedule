<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-back-button default-href="/home"></ion-back-button>
        </ion-buttons>
        <ion-title>Informações do Usuário</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="false" mode="md">
      <div class="form-container">
        <form @submit.prevent="onSubmit">
          <div class="input-container">
            <ion-input
              label="Primeiro Nome"
              placeholder="Seu primeiro nome"
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
              placeholder="Seu último nome"
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

          <ion-button
            shape="round"
            type="submit"
            expand="block"
            class="submit-btn"
          >
            Editar
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
import { reactive, ref, computed, onMounted } from "vue";
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

const form = reactive({
  first_name: "",
  last_name: "",
  email: "",
  address: "",
  phone_number: "",
});

const errorExists = ref<boolean>(false);
const errorMessage = ref<string>("");
const emailInput = ref<InstanceType<typeof IonInput> | null>(null);
const phoneInput = ref<InstanceType<typeof IonInput> | null>(null);

onMounted(async () => {
  try {
    const data = await apiClient.getUser(
      localStorage.getItem("user_id") || sessionStorage.getItem("user_id")
    );
    form.first_name = data["first_name"];
    form.last_name = data["last_name"];
    form.email = data["email"];
    form.address = data["address"];
    form.phone_number = data["phone_number"];
  } catch (error: any) {
    console.log(error?.response?.data);
    console.log(error.response);
    console.log(error);
    return;
  }
});

function handleEmailInput(value: string): string {
  let input = value
    .replace(/\s/g, "")
    .replace(/@+/g, "@")
    .replace(/@(.+)?@/, "@$1")
    .replace(/(\..+)?\./, ".$1");
  return input;
}

function handlePhoneInput(value: string): string {
  let input = value
    .replace(/\D/g, "")
    .replace(/(\d{2})(\d)/, "($1) $2")
    .replace(/(\d{4})(\d)/, "$1-$2")
    .replace(/(\d{4})-(\d)(\d{4})/, "$1$2-$3")
    .replace(/(-\d{4})\d+?$/, "$1");
  return input;
}

function blockNumbers(ev: any) {
  const char = ev.key;
  if (!/^[a-zA-Z\s]$/.test(char) && ev.key !== "Backspace") {
    ev.preventDefault();
  }
}

function hideError(): void {
  errorExists.value = false;
}

async function onSubmit(): Promise<void> {
  {
    form.phone_number = handlePhoneInput(form.phone_number);
    form.email = handleEmailInput(form.email);
    try {
      await apiClient.updateUser(
        localStorage.getItem("user_id") || sessionStorage.getItem("user_id"),
        "PUT",
        form
      );
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

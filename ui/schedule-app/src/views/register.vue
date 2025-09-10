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
              label="Nome Completo"
              label-placement="stacked"
              v-model="form.username"
              @keydown="blockNumbers($event)"
              type="text"
              autocomplete="name"
              placeholder="Seu nome completo"
              fill="outline"
              :clear-input="true"
              required
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
              @ionInput="onEmailInput"
              @ionBlur="markEmailTouched"
              required
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
              required
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
              required
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
              @ionInput="onPhoneInput"
              @ionBlur="markPhoneTouched"
              required
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

const form = reactive({
  username: "",
  email: "",
  password: "",
  address: "",
  phone_number: "",
});

const errorExists = ref<boolean>(false);
const errorMessage = ref<string>("");
const emailInput = ref<InstanceType<typeof IonInput> | null>(null);
const phoneInput = ref<InstanceType<typeof IonInput> | null>(null);

function isValidEmail(email: any): boolean {
  return /^(?=.{1,254}$)(?=.{1,64}@)[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/.test(
    email
  );
}

function onEmailInput(ev: CustomEvent): void {
  const value = String((ev as any).detail?.value ?? "");
  const el = emailInput.value?.$el as HTMLElement | undefined;
  if (!el) return;

  el.classList.remove("ion-valid", "ion-invalid");

  if (value === "") return;

  if (isValidEmail(value)) {
    el.classList.add("ion-valid");
  } else {
    el.classList.add("ion-invalid");
  }
}

function markEmailTouched() {
  const el = emailInput.value?.$el as HTMLElement | undefined;
  el?.classList.add("ion-touched");
}

function isPhoneValid(phone: any): boolean {
  const regex =
    /^(\+?55\s?)?((\([1-9]{2}\))|\d{2}\s?)([9]\d{4}|\d{4})[\s.-]?(\d{4})$/;
  const digits = phone.replace(/\D/g, "");
  return regex.test(digits);
}

function onPhoneInput(ev: CustomEvent): void {
  const value = String((ev as any).detail?.value ?? "");
  const hostEl = ev.target as HTMLElement | undefined;
  if (!hostEl) return;

  hostEl.classList.remove("ion-valid", "ion-invalid");

  if (value === "") return;

  if (isPhoneValid(value)) {
    hostEl.classList.add("ion-valid");
  } else {
    hostEl.classList.add("ion-invalid");
  }
}

function markPhoneTouched(ev: Event): void {
  (ev.target as HTMLElement | null)?.classList.add("ion-touched");
}

function blockNumbers(ev: any) {
  const char = ev.key;
  if (!/^[a-zA-Z\s]$/.test(char) && ev.key !== "Backspace") {
    ev.preventDefault();
  }
}

async function handleSubmit(): Promise<any> {
  errorExists.value = false;
  await router.push("/login");
}

function hideError(): void {
  errorExists.value = false;
}

async function onSubmit(): Promise<void> {
  form.username = form.username.replace(/\s+/g, " ");

  try {
    const data = await apiClient.registerUser({ ...form });
    console.log("3:", data);
    console.log("Registrando usuário:", { ...form });
    await handleSubmit();
    form.username = "";
    form.email = "";
    form.password = "";
    form.address = "";
    form.phone_number = "";
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

<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Crie sua conta</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="false" mode="md">
      <div class="form-container">
        <!-- <h2>Crie sua conta</h2> -->

        <form @submit.prevent="onSubmit">
          <div class="input-container">
            <ion-input
              label="Nome Completo"
              label-placement="stacked"
              v-model="form.username"
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
              label="Email"
              v-model="form.email"
              type="email"
              autocomplete="email"
              inputmode="email"
              placeholder="Seu email"
              label-placement="stacked"
              fill="outline"
              :clear-input="true"
              required
            />
          </div>
          <div class="input-container">
            <ion-input
              label="Senha"
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
              label="Telefone"
              v-model="form.phone_number"
              type="tel"
              inputmode="tel"
              autocomplete="tel"
              placeholder="(00) 00000-0000"
              label-placement="stacked"
              fill="outline"
              :clear-input="true"
              required
            />
          </div>

          <ion-button type="submit" expand="block" class="submit-btn">
            Cadastrar
          </ion-button>
        </form>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { reactive } from "vue";
import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonInput,
  IonButton,
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

async function onSubmit() {
  // Validação simples
  if (
    !form.username ||
    !form.email ||
    !form.password ||
    !form.address ||
    !form.phone_number
  ) {
    window.alert("Preencha todos os campos!");
    return;
  }

  if (form.password.length < 8) {
    window.alert("A senha deve ter mais de 8 caracteres!");
    return;
  }

  //TODO: adicionar validação phone number, email
  form.username = form.username.replace(/\s/g, "");

  try {
    await apiClient.registerUser({ ...form });
    console.log("Registrando usuário:", { ...form });
  } catch (error: any) {
    console.error("Erro ao logar", error);
    if (error.response) {
      console.error("Resposta do servidor:", error.response.data);
      console.error("Status:", error.response.status);
      console.error("Headers:", error.response.headers);
    }
  }

  // Limpa o formulário após enviar
  form.username = "";
  form.email = "";
  form.password = "";
  form.address = "";
  form.phone_number = "";

  router.push("/login");
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
</style>

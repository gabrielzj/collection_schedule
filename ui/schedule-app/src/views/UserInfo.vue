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
          <!-- <div class="input-container">
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
            />
          </div> -->
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

// transforma o objeto 'form' em array e aplica função interna (arrow function)
// para verificar se algum valor é vazio
const isKeyEmpty = computed(() =>
  Object.values(form).some((value) => value === "")
);

async function onSubmit(): Promise<void> {
  {
    // const formattedUsername = form.username.replace(/\s+/g, " ").trim();
    form.phone_number = handlePhoneInput(form.phone_number);
    // const phoneDigits = form.phone_number.replace(/\D/g, "");
    form.email = handleEmailInput(form.email);

    // if (form.phone_number.length < 10 || form.phone_number.length > 11) {
    //   errorExists.value = true;
    //   errorMessage.value = "Número de telefone inválido.";
    //   setTimeout(hideError, 3000);
    //   return;
    // }

    // remover campos vazios do arrary do payload
    if (
      form.first_name != "" &&
      form.last_name != "" &&
      form.email != "" &&
      form.address != "" &&
      form.phone_number != ""
    ) {
      try {
        console.log(form);
        console.log({ ...form });
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
    } else if (isKeyEmpty.value) {
      console.log(form);
      console.log({ ...form });
      // cria uma lista chave-valor sem "", null e undefined e transforma em objeto
      const new_form = Object.fromEntries(
        Object.entries(form).filter(
          ([_, value]) => value !== "" && value !== null && value !== undefined
        )
      );
      console.log(new_form);
      try {
        await apiClient.updateUser(
          localStorage.getItem("user_id") || sessionStorage.getItem("user_id"),
          "PATCH",
          new_form
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
}

const errorExists = ref<boolean>(false);
const errorMessage = ref<string>("");
const emailInput = ref<InstanceType<typeof IonInput> | null>(null);
const phoneInput = ref<InstanceType<typeof IonInput> | null>(null);
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

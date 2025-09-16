<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-back-button default-href="/home"></ion-back-button>
        </ion-buttons>
        <ion-title>Criar um chamado</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true" mode="md">
      <div class="title">
        <h5>Como funciona</h5>
        <ion-icon
          :icon="helpOutline"
          size="large"
          aria-hidden="true"
        ></ion-icon>
      </div>
      <ion-label class="intro-text">
        Deseja descartar algo específico? Crie um <b>chamado de coleta</b> e
        informe os órgãos de coleta sobre sua necessidade.
      </ion-label>
      <ion-item-divider></ion-item-divider>
      <form @submit.prevent="submitCall">
        <div class="form-container">
          <ion-select
            label="Tipo de Resíduo"
            label-placement="stacked"
            aria-label="waste-type"
            interface="alert"
            fill="outline"
            placeholder="Selecione"
            v-model="type"
          >
            <ion-select-option value="plastic">Plástico</ion-select-option>
            <ion-select-option value="paper">Papel</ion-select-option>
            <ion-select-option value="metal">Metal</ion-select-option>
            <ion-select-option value="glass">Vidro</ion-select-option>
            <ion-select-option value="organic">Orgânico</ion-select-option>
            <ion-select-option value="electronic">Eletrônico</ion-select-option>
            <ion-select-option value="other">Outro</ion-select-option>
          </ion-select>
          <br />
          <ion-input
            label="Endereço"
            label-placement="stacked"
            :clear-input="true"
            placeholder="Informe o endereço completo"
            helper-text="Rua, número, bairro, cidade e CEP"
            fill="outline"
            v-model="address"
          ></ion-input>
          <br />
          <ion-textarea
            label="Descrição"
            label-placement="stacked"
            :clear-on-edit="true"
            placeholder="Detalhe o resíduo a ser coletado"
            helper-text="Informe detalhes dos resíduos para facilitar a coleta"
            :auto-grow="true"
            :rows="5"
            :counter="true"
            :maxlength="100"
            fill="outline"
            v-model="description"
          ></ion-textarea>
          <br />
          <ion-input
            label="Quantidade"
            label-placement="stacked"
            :clear-input="true"
            placeholder="Quantidade aproximada"
            helper-text="Informe uma estimativa em kg"
            fill="outline"
            v-model="amount_to_collect"
          ></ion-input>
          <br />
          <ion-select
            label="Urgência"
            label-placement="stacked"
            aria-label="waste-urgency"
            fill="outline"
            interface="alert"
            placeholder="Selecione"
            v-model="urgency"
          >
            <ion-select-option value="low">Baixa</ion-select-option>
            <ion-select-option value="medium">Moderada</ion-select-option>
            <ion-select-option value="high">Alta</ion-select-option>
          </ion-select>
          <br />
          <ion-label position="stacked" color="dark"
            >Escolha a data e horário da coleta</ion-label
          >
          <div class="date-button">
            <ion-datetime-button datetime="schedule-datetime">
              >
            </ion-datetime-button>
          </div>
          <ion-modal :keep-contents-mounted="true">
            <ion-datetime
              id="schedule-datetime"
              presentation="date-time"
              :format-options="formatOptions"
              v-model="best_time_for_collect"
            ></ion-datetime>
          </ion-modal>
          <div class="button-container">
            <ion-button
              type="submit"
              expand="block"
              color="primary"
              class="submit-button"
            >
              Enviar
            </ion-button>
          </div>
        </div>
      </form>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonInput,
  IonTextarea,
  IonIcon,
  IonDatetimeButton,
  IonDatetime,
  IonModal,
  IonItemDivider,
  IonSelect,
  IonSelectOption,
  IonLabel,
  IonButton,
  IonButtons,
  IonBackButton,
} from "@ionic/vue";
import { helpOutline } from "ionicons/icons";
import apiClient from "@/services/apiClient";
import { ref } from "vue";

type WasteType =
  | "plastic"
  | "paper"
  | "metal"
  | "glass"
  | "organic"
  | "electronic"
  | "other";
type Urgency = "low" | "medium" | "high";

const type = ref<WasteType | null>(null);
const address = ref<string | null>(null);
const description = ref<string | null>(null);
const urgency = ref<Urgency | null>(null);
const amount_to_collect = ref<string | null>(null);
const best_time_for_collect = ref<string | null>(null);

// const requestValues = computed<
//   (WasteType | Urgency | string | number | null)[]
// >(() => [
//   type.value,
//   address.value,
//   description.value,
//   urgency.value,
//   amount_to_collect.value != null && amount_to_collect.value !== ""
//     ? Number(amount_to_collect.value)
//     : null,
//   best_time_for_collect.value,
// ]);

const submitCall = async () => {
  if (!type.value || !address.value || !urgency.value) {
    console.warn("Preencha tipo, endereço e data/hora.");
    return;
  }

  const date = new Date(best_time_for_collect.value || "");
  if (isNaN(date.getTime())) {
    console.warn("Data e hora inválidas.");
    return;
  }

  const payload = {
    type: type.value,
    address: address.value,
    description: description.value,
    urgency: urgency.value,
    amount_to_collect:
      amount_to_collect.value != null && amount_to_collect.value !== ""
        ? Number(amount_to_collect.value)
        : null,
    best_time_for_collect: date.toISOString(),
  };
  // tem q manualmente selecionar a data se não é enviado null
  try {
    await apiClient.createCall(payload);
  } catch (error: any) {
    console.error("Erro ao enviar chamado:", error);
  }
};

const formatOptions = {
  date: {
    weekday: "short",
    month: "short",
    day: "2-digit",
  },
  time: {
    hour: "2-digit",
    minute: "2-digit",
    hour12: false,
  },
} as const;
</script>

<style scoped>
ion-list {
  width: auto;
}

.title {
  font-size: 18px;
  margin: 20px 0 0 20px;
  display: flex;
  flex-direction: row;
  align-items: center;
  background-color: var(--ion-color-primary);
  color: white;
  border-radius: 20px 0 0 20px;
  padding-left: 20px;
}

.title h5 {
  margin-top: 10px;
  margin-bottom: 10px;
}

.form-container {
  padding: 20px;
}

/* .form-container ion-select::part(icon) {
  display: none;
} */

.intro-text {
  display: block;
  padding: 12px 20px;
  text-align: justify;
  hyphens: auto;
  margin-top: 20px;
  color: var(--color-light-gray);
}

ion-modal {
  --border-radius: 15px;
}

ion-label {
  color: var(--color-light-gray);
}

.button-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.submit-button {
  width: 100%;
  margin-top: 20px;
}

.date-button {
  margin-top: 10px;
  display: flex;
  align-items: start;
}
</style>

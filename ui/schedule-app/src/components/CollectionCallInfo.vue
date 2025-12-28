<template>
  <ion-modal :is-open="isOpen">
    <ion-page>
      <ion-header>
        <ion-toolbar>
          <ion-title>Informações do Chamado</ion-title>
          <ion-buttons slot="end">
            <ion-button @click="closeModal">
              <ion-icon :icon="closeOutline"></ion-icon>
            </ion-button>
          </ion-buttons>
        </ion-toolbar>
      </ion-header>

      <ion-content :fullscreen="true" mode="md">
        <form @submit.prevent="updateCall">
          <div class="form-container">
            <ion-select
              label="Tipo de Resíduo"
              label-placement="stacked"
              aria-label="waste-type"
              interface="alert"
              fill="outline"
              placeholder="Selecione"
              v-model="form.type"
            >
              <ion-select-option value="plastic">Plástico</ion-select-option>
              <ion-select-option value="paper">Papel</ion-select-option>
              <ion-select-option value="metal">Metal</ion-select-option>
              <ion-select-option value="glass">Vidro</ion-select-option>
              <ion-select-option value="organic">Orgânico</ion-select-option>
              <ion-select-option value="electronic"
                >Eletrônico</ion-select-option
              >
              <ion-select-option value="residual_waste"
                >Rejeito</ion-select-option
              >
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
              v-model="form.address"
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
              v-model="form.description"
            ></ion-textarea>
            <br />
            <ion-input
              label="Quantidade"
              label-placement="stacked"
              :clear-input="true"
              placeholder="Quantidade aproximada"
              helper-text="Informe uma estimativa em kg"
              fill="outline"
              v-model="form.amount_to_collect"
            ></ion-input>
            <br />
            <ion-select
              label="Urgência"
              label-placement="stacked"
              aria-label="waste-urgency"
              fill="outline"
              interface="alert"
              placeholder="Selecione"
              v-model="form.urgency"
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
                v-model="form.best_time_for_collect"
              ></ion-datetime>
            </ion-modal>
            <div class="button-container">
              <ion-button
                shape="round"
                type="submit"
                expand="block"
                color="primary"
                class="submit-button"
              >
                Atualizar
              </ion-button>
              <ion-note color="danger" v-if="errorExists">{{
                errorMessage
              }}</ion-note>
            </div>
          </div>
        </form>
      </ion-content>
    </ion-page>
  </ion-modal>
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
  IonNote,
  IonSelect,
  IonSelectOption,
  IonLabel,
  IonButton,
  IonButtons,
} from "@ionic/vue";
import apiClient from "@/services/apiClient";
import { closeOutline } from "ionicons/icons";
import { reactive, ref } from "vue";

const props = defineProps<{
  isOpen: boolean;
  call?: any;
}>();

function hideError(): void {
  errorExists.value = false;
}

const errorExists = ref<boolean>(false);
const errorMessage = ref<string>("");

const form = reactive({
  type: "",
  address: "",
  description: "",
  urgency: "",
  amount_to_collect: "",
  best_time_for_collect: "",
});

form.type = props.call["type"];
form.address = props.call["address"];
form.description = props.call["description"];
form.urgency = props.call["urgency"];
form.amount_to_collect = props.call["amount_to_collect"];
form.best_time_for_collect = props.call["best_time_for_collect"];

const emit = defineEmits(["dismiss"]);

const closeModal = () => {
  emit("dismiss");
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

async function updateCall() {
  try {
    await apiClient.updateCall(props.call["id"], form);
    closeModal();
  } catch (error: any) {
    errorExists.value = true;
    setTimeout(hideError, 3000);
    errorMessage.value =
      error?.response?.data || "Falha ao atualizar. Tente novamente.";
    if (error.response) {
      console.error("Resposta do servidor:", error.response?.data?.detail);
    }
  }
}
</script>
<style scoped>
.form-container {
  padding: 20px;
}

ion-modal {
  --border-radius: 15px 15px 0 0;
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

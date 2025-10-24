<template>
  <ion-card mode="md">
    <ion-card-header>
      <div class="header-container">
        <ion-toolbar>
          <ion-card-title color="medium">{{ typeLabel }}</ion-card-title>
          <ion-buttons slot="end">
            <ion-button @click.stop="deleteCall">
              <ion-icon :icon="closeOutline"></ion-icon>
            </ion-button>
          </ion-buttons>
        </ion-toolbar>
      </div>
      <ion-card-subtitle>
        Urgência: <b :class="['urgency', urgency]">{{ urgencyLabel }}</b>
      </ion-card-subtitle>
    </ion-card-header>
    <ion-card-content>
      <div class="row">
        <ion-icon class="icon" :icon="locationOutline" aria-hidden="true" />
        <span class="text">{{ address }}</span>
      </div>
      <div class="row" v-if="bestTime">
        <ion-icon class="icon" :icon="timeOutline" aria-hidden="true" />
        <span class="text">{{ formattedBestTime }}</span>
      </div>
      <!-- Adicionar Status -->
      <div class="row" v-if="status">
        <ion-icon class="icon" :icon="readerOutline" aria-hidden="true" />
        <span class="text">{{ status }}</span>
      </div>
    </ion-card-content>
  </ion-card>
</template>

<script setup lang="ts">
import {
  IonCard,
  IonCardHeader,
  IonCardTitle,
  IonCardSubtitle,
  IonCardContent,
  IonIcon,
  IonButtons,
  IonButton,
  IonToolbar,
} from "@ionic/vue";
import {
  locationOutline,
  timeOutline,
  closeOutline,
  readerOutline,
} from "ionicons/icons";
import { computed } from "vue";
import apiClient from "@/services/apiClient";
import { parseISO } from "date-fns";
import { formatInTimeZone } from "date-fns-tz";
import { ptBR } from "date-fns/locale";

const emit = defineEmits(["deleted"]);

type WasteType =
  | "paper"
  | "metal"
  | "plastic"
  | "electronic"
  | "organic"
  | "glass"
  | "residual_waste"
  | "other";

type Urgency = "low" | "medium" | "high";

const props = defineProps<{
  type: WasteType;
  address: string;
  urgency: Urgency;
  bestTime?: string | null;
  callID: number;
  status: string;
}>();

const TYPE_LABEL: Record<WasteType, string> = {
  paper: "Papel",
  metal: "Metal",
  plastic: "Plástico",
  electronic: "Eletrônico",
  organic: "Orgânico",
  glass: "Vidro",
  residual_waste: "Resíduo Sólido",
  other: "Outro",
};

const URGENCY_LABEL: Record<Urgency, string> = {
  low: "Baixa",
  medium: "Moderada",
  high: "Alta",
};

const STATUS_LABEL: Record<string, string> = {
  pending: "Pendente",
  completed: "Concluído",
  failed: "Cancelado",
};

const typeLabel = computed(() => TYPE_LABEL[props.type] ?? props.type);
const urgencyLabel = computed(
  () => URGENCY_LABEL[props.urgency] ?? props.urgency
);
const status = computed(() => STATUS_LABEL[props.status] ?? props.status);

const formattedBestTime = computed(() => {
  if (!props.bestTime) return "";
  console.log("Best time no card:", props.bestTime);
  // const date = new Date(props.bestTime);
  // console.log("Date no card:", date);
  // if (Number.isNaN(date.getTime())) return props.bestTime as string;
  // return date.toLocaleString("pt-BR", {
  //   weekday: "short",
  //   day: "2-digit",
  //   month: "short",
  //   year: "numeric",
  //   hour: "2-digit",
  //   minute: "2-digit",
  // });
  const formattedBestTime = formatInTimeZone(
    parseISO(props.bestTime),
    "America/Sao_Paulo",
    "EEEE, dd 'de' MMMM 'de' yyyy 'às' HH:mm'h'",
    { locale: ptBR }
  );
  return formattedBestTime;
});

const deleteCall = async () => {
  try {
    await apiClient.deleteCall(props.callID);
    console.log("ID da call deletada:", props.callID);
    emit("deleted", props.callID);
    console.log(`Chamado de ID ${props.callID} deletado`);
  } catch (error: any) {
    console.error("Falha ao deletar o chamado");
  }
};
</script>

<style scoped>
.header-container {
  display: flex;
  flex-direction: row;
}

.header-container ion-card-title {
  width: fit-content;
}

.row {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  margin: 8px 0;
}
.icon {
  flex: 0 0 18px;
  width: 18px;
  height: 18px;
  margin-top: 2px;
  color: var(--ion-color-medium);
}
.text {
  color: var(--ion-color-step-600, #3a3a3a);
  flex: 1 1 auto;
  min-width: 0;
  word-break: break-word;
  overflow-wrap: anywhere;
}
.urgency.low {
  color: var(--ion-color-success);
}
.urgency.medium {
  color: var(--ion-color-warning);
}
.urgency.high {
  color: var(--ion-color-danger);
}
</style>

<template>
  <section>
    <ion-list lines="none">
      <ion-item v-if="loading">
        <ion-label>Carregando seus chamados...</ion-label>
      </ion-item>

      <ion-item v-else-if="error" color="danger">
        <ion-label>Erro: {{ error }}</ion-label>
      </ion-item>

      <template v-else-if="calls.length === 0">
        <div class="empty">
          <h3>Você ainda não criou nenhum chamado</h3>
          <p>Crie seu primeiro chamado de coleta e acompanhe por aqui.</p>
          <ion-button router-link="/home/call" color="primary" expand="block">
            Criar chamado de coleta
          </ion-button>
        </div>
      </template>

      <template v-else>
        <CollectionCallCard
          v-for="call in calls"
          :key="call.id"
          :type="call.type"
          :address="call.address"
          :urgency="call.urgency"
          :best-time="call.best_time_for_collect"
          :callID="call.id"
          :status="call.status"
          :is-open="isModalOpen"
          @click="openModal(call)"
          @deleted="deleteCall"
        />
      </template>
    </ion-list>
    <CollectionCallInfo
      v-if="selectedCall"
      :is-open="isModalOpen"
      :call="selectedCall"
      @dismiss="closeModal"
    />
  </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { IonList, IonItem, IonLabel, IonButton } from "@ionic/vue";
import apiClient from "@/services/apiClient";
import CollectionCallCard from "@/components/CollectionCallCard.vue";
import CollectionCallInfo from "@/components/CollectionCallInfo.vue";

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

interface CollectionCall {
  id: number;
  type: WasteType;
  description?: string;
  address: string;
  urgency: Urgency;
  amount_to_collect?: number;
  best_time_for_collect?: string | null;
  status: string;
}

const loading = ref(true);
const error = ref<string | null>(null);
const calls = ref<CollectionCall[]>([]);
const isModalOpen = ref<boolean>(false);
const selectedCall = ref<CollectionCall | null>(null);

console.log("Calls length list:", calls.value.length);
const emit = defineEmits(["qtdCalls", "updateCalls"]);

const openModal = (call: CollectionCall) => {
  selectedCall.value = call;
  isModalOpen.value = true;
};

const closeModal = () => {
  isModalOpen.value = false;
  selectedCall.value = null;
};

const fetchCalls = async () => {
  loading.value = true;
  error.value = null;
  try {
    const data = await apiClient.getCalls();
    calls.value = Array.isArray(data)
      ? data.map((d) => ({
          id: d.id,
          type: d.type,
          description: d.description,
          address: d.address ?? "Endereço não informado",
          urgency: d.urgency,
          amount_to_collect: d.amount_to_collect,
          best_time_for_collect: d.best_time_for_collect,
          status: d.status,
        }))
      : [];
    emit("qtdCalls", calls.value.length);
  } catch (e: any) {
    error.value = e?.message ?? "Falha ao carregar";
  } finally {
    loading.value = false;
  }
};

onMounted(async () => {
  await fetchCalls();
});

// filho expoe p/ pai
defineExpose({
  refresh: fetchCalls,
});

const deleteCall = (callID: number) => {
  console.log("array antes:", calls.value);
  calls.value = calls.value.filter((call) => call.id !== callID);
  console.log(calls.value.length);
  emit("updateCalls", calls.value.length);
  console.log("array depois:", calls.value);
};
</script>

<style scoped>
section {
  padding: 8px 12px;
}
.empty {
  text-align: center;
  padding: 24px 12px;
  color: var(--ion-color-medium);
}
.empty h3 {
  margin: 0 0 8px 0;
  color: var(--ion-color-dark);
}
.empty p {
  margin: 0 0 16px 0;
}
</style>

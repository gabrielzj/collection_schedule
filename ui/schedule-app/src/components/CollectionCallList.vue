<template>
  <section>
    <ion-list lines="none">
      <template v-if="loading">
        <ion-item>
          <ion-label>Carregando seus chamados...</ion-label>
        </ion-item>
      </template>

      <template v-else-if="error">
        <ion-item color="danger">
          <ion-label>Erro: {{ error }}</ion-label>
        </ion-item>
      </template>

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
        />
      </template>
    </ion-list>
  </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { IonList, IonItem, IonLabel, IonButton } from "@ionic/vue";
import apiClient from "@/services/apiClient";
import CollectionCallCard from "@/components/CollectionCallCard.vue";

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

interface CollectionCallDTO {
  id: number;
  type: WasteType;
  address: string;
  urgency: Urgency;
  best_time_for_collect?: string | null;
}

const loading = ref(true);
const error = ref<string | null>(null);
const calls = ref<CollectionCallDTO[]>([]);

const emit = defineEmits(["qtdCalls"]);

onMounted(async () => {
  try {
    const data = await apiClient.getCalls();
    console.log(data);
    // const currentUserId = Number(localStorage.getItem("user_id"));
    calls.value = Array.isArray(data)
      ? data
          // .filter((d) =>
          //   Number.isFinite(currentUserId) && d.user != null
          //     ? Number(d.user) === currentUserId
          //     : true
          // )
          .map((d) => ({
            id: d.id,
            type: d.type,
            address: d.address || "Endereço não informado",
            urgency: d.urgency,
            best_time_for_collect: d.best_time_for_collect,
          }))
      : [];
    emit("qtdCalls", calls.value.length);
    console.log("Quantidade de chamados:", calls.value.length);
  } catch (e: any) {
    error.value = e?.message ?? "Falha ao carregar";
  } finally {
    loading.value = false;
  }
});
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

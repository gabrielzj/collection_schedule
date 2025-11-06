<template>
  <div class="content">
    <Sidebar />
    <div class="stats">
      <header class="top-bar">
        <div class="left">
          <h1>Estatísticas</h1>
          <div class="meta">
            <span v-if="!loading" class="total">Total: {{ totalCalls }}</span>
            <span v-else class="pulse">Carregando...</span>
          </div>
        </div>
      </header>

      <div v-if="error" class="error-box">
        <p>Erro ao carregar: {{ error }}</p>
        <button @click="fetchCalls">Tentar novamente</button>
      </div>

      <section v-else class="charts">
        <BarChart :types="wasteTypes" title="Chamados por Tipo de Resíduo" />
        <DonutsChart :urgencies="wasteUrgency" title="Chamados por Urgência" />
        <RadialChart :total="total_amount" :target="500" title="Total de Resíduos" />
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import Sidebar from '@/components/Sidebar.vue';
import BarChart from '@/components/BarChart.vue';
import DonutsChart from '@/components/DonutsChart.vue';
import RadialChart from '@/components/RadialChart.vue';
import apiClient from '@/services/apiClient';

interface User {
  id: number;
  first_name?: string;
  last_name?: string;
  email?: string;
}

interface CollectionCall {
  id: number;
  user: User;
  type: string;
  urgency: string;
}

const loading = ref(false);
const error = ref<string | null>(null);
const calls = ref<CollectionCall[]>([]);
const wasteTypes = ref<string[]>([]);
const wasteUrgency = ref<string[]>([]);
const total_amount = ref<number>(0);

const totalCalls = computed(() => calls.value.length);

async function fetchCalls() {
  loading.value = true;
  error.value = null;
  try {
    const resp = await apiClient.listAllCalls();
    wasteTypes.value = resp.map((item: any) => item.type);
    wasteUrgency.value = resp.map((item: any) => item.urgency);
    const wasteAmounts: string[] = resp.map((item: any) => item.amount_to_collect);
    total_amount.value = wasteAmounts.reduce((acc, val) => acc + Number(val), 0);

    calls.value = resp.map((d: any) => ({
      id: d.id,
      user: d.user,
      type: d.type,
      urgency: d.urgency,
    }));
  } catch (e: any) {
    error.value = e.message || 'Falha inesperada';
  } finally {
    loading.value = false;
  }
}

onMounted(fetchCalls);
</script>

<style scoped>
.content {
  display: flex;
  min-height: 100vh;
  padding-left: 216px; /* 200 + 16 */
}

@media (max-width: 900px) {
  .content {
    flex-direction: column;
    padding-left: 0;
  }
}

.stats {
  flex: 1;
  max-width: 1400px;
  margin: 0 auto;
  padding: 1.25rem 1.25rem 2.5rem;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.top-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}

.top-bar h1 {
  font-size: 1.55rem;
  line-height: 1.1;
  margin: 0;
  font-weight: 700;
  color: #1d2b39;
  letter-spacing: -0.5px;
}

.top-bar .left {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.meta {
  margin-top: 5px;
  text-align: center;
  align-items: center;
  font-size: 0.8rem;
  font-weight: 600;
  color: #5a6570;
}

.pulse {
  display: inline-block;
  animation: pulse 1.4s ease-in-out infinite;
}

@keyframes pulse {
  0%,
  100% {
    opacity: 0.4;
  }
  50% {
    opacity: 1;
  }
}

.error-box {
  background: #ffe1e1;
  border: 1px solid #ffb7b7;
  padding: 1rem;
  border-radius: 14px;
  display: flex;
  gap: 1rem;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
}
.error-box p {
  margin: 0;
  font-size: 0.85rem;
  font-weight: 600;
  color: #7a1111;
}
.error-box button {
  background: #7a1111;
  color: #fff;
  border: none;
  padding: 0.55rem 0.9rem;
  border-radius: 8px;
  font-size: 0.7rem;
  letter-spacing: 0.5px;
  cursor: pointer;
  font-weight: 600;
  text-transform: uppercase;
}

.charts {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1rem;
}
</style>

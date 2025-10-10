<!-- src/views/DashboardView.vue -->
<template>
  <div class="dashboard">
    <header class="top-bar">
      <h1>Chamados de Coleta</h1>
      <div class="meta">
        <span v-if="!loading" class="total">Total: {{ filteredCalls.length }}</span>
        <span v-else class="pulse">Carregando...</span>
      </div>
    </header>

    <section class="filters">
      <input
        v-model.trim="search"
        type="text"
        placeholder="Buscar por endereço, usuário ou tipo..."
        class="search"
      />
      <select v-model="statusFilter">
        <option value="">Status (todos)</option>
        <option value="pending">Pendente</option>
        <option value="in_process">Em Andamento</option>
        <option value="completed">Finalizada</option>
        <option value="failed">Cancelada</option>
      </select>
      <select v-model="urgencyFilter">
        <option value="">Urgência (todas)</option>
        <option value="low">Baixa</option>
        <option value="medium">Moderada</option>
        <option value="high">Alta</option>
      </select>
      <button class="refresh" @click="fetchCalls" :disabled="loading">Atualizar</button>
    </section>

    <div v-if="error" class="error-box">
      <p>Erro ao carregar: {{ error }}</p>
      <button @click="fetchCalls">Tentar novamente</button>
    </div>

    <div v-else-if="loading" class="grid skeleton">
      <div v-for="n in 6" :key="n" class="skeleton-card"></div>
    </div>

    <div v-else-if="filteredCalls.length === 0" class="empty">Nenhum chamado encontrado.</div>

    <div v-else class="grid">
      <CollectionCallCard
        v-for="c in filteredCalls"
        :key="c.id"
        :call="c"
        @click="openModal(c.id)"
      />
    </div>
  </div>

  <CollectionInfoModal
    v-if="isModalOpen && selectedCall"
    @close-modal="closeModal"
    :call="selectedCall"
  />
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import CollectionCallCard from '@/components/CollectionCard.vue';
import CollectionInfoModal from '@/components/CollectionInfoModal.vue';
import apiClient from '@/services/apiClient';

interface User {
  id: number;
  first_name?: string;
  last_name?: string;
  email?: string;
  phone_number?: string;
}

interface CollectionCall {
  id: number;
  user: User;
  type: string;
  address: string;
  amount_to_collect: number | string;
  description?: string;
  urgency: string;
  status: string;
  best_time_for_collect?: string | null;
}

const calls = ref<CollectionCall[]>([]);
const loading = ref<boolean>(false);
const error = ref<string | null>(null);

const search = ref<string>('');
const statusFilter = ref<string>('');
const urgencyFilter = ref<string>('');
const isModalOpen = ref<boolean>(false);
const selectedCall = ref<CollectionCall | undefined>();

function openModal(id: number) {
  selectedCall.value = calls.value.find((call) => call.id === id);
  isModalOpen.value = true;
  console.log(selectedCall.value);
}

function closeModal() {
  isModalOpen.value = false;
  selectedCall.value = undefined;
}

async function fetchCalls() {
  loading.value = true;
  error.value = null;
  try {
    const resp = await apiClient.listAllCalls();
    console.log(resp);

    calls.value = resp.map((d: any) => ({
      id: d.id,
      user: d.user,
      type: d.type,
      description: d.description,
      address: d.address ?? 'Endereço não informado',
      urgency: d.urgency,
      amount_to_collect: d.amount_to_collect,
      best_time_for_collect: d.best_time_for_collect,
      status: d.status,
    }));
  } catch (e: any) {
    error.value = e.message || 'Falha inesperada';
  } finally {
    loading.value = false;
  }
}

const filteredCalls = computed(() => {
  const term = search.value.toLowerCase();
  return calls.value.filter((c) => {
    const matchesTerm =
      !term ||
      [c.address, c.type, c.user?.first_name, c.user?.last_name, c.user?.email]
        .filter(Boolean)
        .some((v) => String(v).toLowerCase().includes(term));

    const matchesStatus = !statusFilter.value || c.status === statusFilter.value;
    const matchesUrgency = !urgencyFilter.value || c.urgency === urgencyFilter.value;
    return matchesTerm && matchesStatus && matchesUrgency;
  });
});

onMounted(fetchCalls);
</script>

<style scoped>
.dashboard {
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
.meta {
  margin-top: 5px;
  text-align: center;
  align-items: center;
  font-size: 0.8rem;
  font-weight: 600;
  color: #5a6570;
}
.total {
  background: #eef3f7;
  padding: 0.35rem 0.7rem;
  border-radius: 20px;
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
.filters {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  align-items: center;
}
.filters input,
.filters select {
  padding: 0.55rem 0.75rem;
  border: 1px solid #d7dde2;
  background: #fff;
  border-radius: 10px;
  font-size: 0.8rem;
  outline: none;
  transition: 0.2s;
  min-width: 190px;
}
.filters input:focus,
.filters select:focus {
  border-color: #2f7dd1;
  box-shadow: 0 0 0 3px rgba(47, 125, 209, 0.15);
}
.search {
  flex: 1;
  min-width: 260px;
}
.refresh {
  background: #2f7dd1;
  color: #fff;
  border: none;
  padding: 0.6rem 1rem;
  font-size: 0.75rem;
  font-weight: 600;
  border-radius: 10px;
  letter-spacing: 0.5px;
  cursor: pointer;
  text-transform: uppercase;
  transition: 0.2s;
}
.refresh:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
.refresh:not(:disabled):hover {
  background: #2567ad;
}
.grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  align-items: stretch;
}
.empty {
  padding: 2rem;
  background: #f5f8fa;
  border: 2px dashed #d4dde4;
  border-radius: 18px;
  text-align: center;
  font-size: 0.9rem;
  color: #5a6570;
  font-weight: 500;
  letter-spacing: 0.5px;
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
.skeleton-card {
  height: 230px;
  border-radius: 16px;
  background: linear-gradient(110deg, #eaeef2 8%, #f3f6f9 18%, #eaeef2 33%);
  background-size: 200% 100%;
  animation: shimmer 1.2s linear infinite;
}
@keyframes shimmer {
  to {
    background-position-x: -200%;
  }
}
.skeleton .skeleton-card:nth-child(odd) {
  animation-duration: 1.6s;
}
</style>


<template>
  <div class="call-card" :class="statusClass">
    <header class="card-header">
      <h3 class="title">{{ typeLabel }}</h3>
      <span class="badge status">{{ statusLabel }}</span>
    </header>

    <p class="line">
        <p v-if="call.user.first_name && call.user.last_name"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-fill" viewBox="0 0 16 16">
          <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6"/>
        </svg><strong>Usuário:</strong>
        {{ call.user?.first_name }} {{ call.user?.last_name }}
        </p>
        <p v-else><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-fill" viewBox="0 0 16 16">
          <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6"/>
        </svg><strong>Usuário:</strong> <span>Sem Nome</span>
        </p>
        <div class="email-container"> 
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-envelope-fill" viewBox="0 0 16 16">
            <path d="M.05 3.555A2 2 0 0 1 2 2h12a2 2 0 0 1 1.95 1.555L8 8.414zM0 4.697v7.104l5.803-3.558zM6.761 8.83l-6.57 4.027A2 2 0 0 0 2 14h12a2 2 0 0 0 1.808-1.144l-6.57-4.027L8 9.586zm3.436-.586L16 11.801V4.697z"/>
          </svg>
          <strong>E-mail:</strong>
          <span v-if="call.user?.email" class="email"> {{ call.user.email }}</span>
        </div>
    </p>

    <p class="line">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-telephone-fill" viewBox="0 0 16 16">
        <path fill-rule="evenodd" d="M1.885.511a1.745 1.745 0 0 1 2.61.163L6.29 2.98c.329.423.445.974.315 1.494l-.547 2.19a.68.68 0 0 0 .178.643l2.457 2.457a.68.68 0 0 0 .644.178l2.189-.547a1.75 1.75 0 0 1 1.494.315l2.306 1.794c.829.645.905 1.87.163 2.611l-1.034 1.034c-.74.74-1.846 1.065-2.877.702a18.6 18.6 0 0 1-7.01-4.42 18.6 18.6 0 0 1-4.42-7.009c-.362-1.03-.037-2.137.703-2.877z"/>
      </svg>
      <strong>Telefone:</strong> {{ call.user.phone_number || '-' }}
    </p>
    <p class="line">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-geo-alt-fill" viewBox="0 0 16 16">
        <path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10m0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6"/>
      </svg>
      <strong>Endereço de Residencia:</strong> <br> {{ call.user.address || '-' }}
    </p>
    <!-- <p class="line">
      <strong>Melhor Data/Horário de Coleta:</strong>
      {{ formatDate(call.best_time_for_collect) || '-' }}
    </p> -->

    <footer class="footer">
      <span class="badge light">ID: {{ call.id }}</span>
      <!-- <span class="badge qtd">Quantidade Estimada: {{ call.amount_to_collect }} Kg</span> -->
    </footer>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

interface User {
  id: number
  first_name?: string
  last_name?: string
  email?: string
  phone_number?: string
  address?: string
}

interface CollectionCall {
  id: number
  user: User
  type: string
  address: string
  amount_to_collect: number | string
  description?: string
  urgency: string
  status: string
  best_time_for_collect?: string | null
}

const props = defineProps<{
  call: CollectionCall
}>()

const TYPE_LABELS: Record<string, string> = {
  paper: 'Papel',
  metal: 'Metal',
  plastic: 'Plástico',
  electronic: 'Eletrônico',
  organic: 'Orgânico',
  glass: 'Vidro',
  residual_waste: 'Resíduo Sólido',
  other: 'Outro',
}

const STATUS_LABELS: Record<string, string> = {
  pending: 'Pendente',
  completed: 'Finalizada',
  failed: 'Cancelada',
}

const URGENCY_LABELS: Record<string, string> = {
  low: 'Baixa',
  medium: 'Moderada',
  high: 'Alta',
}

const typeLabel = computed(() => TYPE_LABELS[props.call.type]);
const statusLabel = computed(() => STATUS_LABELS[props.call.status]);
const urgencyLabel = computed(() => URGENCY_LABELS[props.call.urgency]);

const statusClass = computed(() => `status-${props.call.status}`);

function formatDate(value?: string | null) {
  if (!value) return ''
  const d = new Date(value)
  if (isNaN(d.getTime())) return ''
  return d.toLocaleString('pt-BR', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  })
}

</script>

<style scoped>
.call-card {
  background: #fff;
  border-radius: 16px;
  padding: 1rem 1.1rem 0.9rem;
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.06);
  border: 1px solid #d5d8db;
  position: relative;
  transition: 0.2s ease;
}
.call-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 14px -4px rgba(0, 0, 0, 0.15);
}
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 0.25rem;
  gap: 0.75rem;
}
.title {
  font-size: 1.05rem;
  line-height: 1.2;
  margin: 0;
  font-weight: 600;
  color: #032b81;
}
.line {
  margin: 0;
  font-size: 0.85rem;
  line-height: 1.25;
}

.line p .icon{
  align-items: center;
  display: flex;
  gap: 0.25rem;
  margin: 0.15rem 0;
}

.small {
  font-size: 0.72rem;
}
.muted {
  color: #5c6977;
}
.email {
  font-style: italic;
}
.description {
  font-size: 0.75rem;
  line-height: 1.25;
  margin: 0.25rem 0 0.4rem;
  color: #2f3e4d;
  max-height: 3.2em;
  overflow: hidden;
  text-overflow: ellipsis;
}
.footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: auto;
  padding-top: 0.5rem;
  border-top: 1px solid #f1f3f6;
  gap: 0.5rem;
  flex-wrap: wrap;
}
.badge {
  display: inline-block;
  border-radius: 24px;
  font-size: 0.65rem;
  font-weight: 600;
  padding: 0.35rem 0.6rem;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  white-space: nowrap;
}
.qtd {
    background: #8eaff5;
    color: #010d27;
}

.status {
  background: #d0d6dd;
  color: #da3114;
}
.badge.light {
  background: #f3f5f7;
  color: #3d4a57;
}
.badge.warn {
  background: #032b81;
  color: #7a3d00;
}
.status-pending .badge.status {
  background: #ffe8b2;
  color: #7a4b00;
}
.status-completed .badge.status {
  background: #c6f6d5;
  color: #135c26;
}
.status-failed .badge.status {
  background: #ffd3d3;
  color: #7a1313;
}
</style>

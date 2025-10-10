<template>
  <div class="modal-overlay" @click.self="closeModal">
    <div class="modal">
      <header class="modal-header">
        <h2>Informações do Chamado</h2>
        <button class="close-btn" @click="closeModal" aria-label="Fechar modal">×</button>
      </header>

      <div class="content">
        <div class="info-grid">
          <div class="field wide">
            <span class="label">Tipo de Resíduo</span>
            <span class="value">{{ typeLabel || '-' }}</span>
          </div>
          <!-- <div class="field wide">
            <span class="label">Status</span>
            <span class="value status" :class="'status-' + (call?.status || 'pending')">
              {{ statusLabel || '-' }}
            </span>
          </div> -->
          <div class="field wide">
            <span class="label">Urgência</span>
            <span class="value">{{ urgencyLabel || '-' }}</span>
          </div>
          <!-- <div class="field" v-if="call?.description">
            <span class="label">Telefone</span>
            <span class="value">{{ call?.user.phone_number || 'Telefone não informado' }}</span>
          </div> -->
          <div class="field wide">
            <span class="label">Quantidade Estimada (Kg)</span>
            <span class="value">{{ call?.amount_to_collect || '-' }}</span>
          </div>
          <div class="field wide">
            <span class="label">Endereço</span>
            <span class="value">{{ call?.address || 'Endereço não informado' }}</span>
          </div>
          <div class="field wide" v-if="call?.best_time_for_collect">
            <span class="label">Melhor Horário de Coleta</span>
            <span class="value">{{ formatDate(call?.best_time_for_collect || '-') }}</span>
          </div>
          <div class="field wide" v-if="call?.description">
            <span class="label">Descrição</span>
            <span class="value multiline">{{ call?.description || '-' }}</span>
          </div>
        </div>
      </div>

      <footer class="modal-footer">
        <button class="btn neutral" @click="closeModal">Fechar</button>
        <button class="btn secondary" @click="updateStatus">Confirmar</button>
      </footer>
    </div>
  </div>
</template>
<script setup lang="ts">
import { computed } from 'vue';
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
  description?: string;
  urgency: string;
  amount_to_collect: number | string;
  best_time_for_collect?: string | null;
  status: string;
}

const props = defineProps<{
  call: CollectionCall;
}>();

function formatDate(value?: string | null) {
  if (!value) return '';
  const d = new Date(value);
  if (isNaN(d.getTime())) return '';
  return d.toLocaleString('pt-BR', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  });
}

const TYPE_LABELS: Record<string, string> = {
  paper: 'Papel',
  metal: 'Metal',
  plastic: 'Plástico',
  electronic: 'Eletrônico',
  organic: 'Orgânico',
  glass: 'Vidro',
  residual_waste: 'Resíduo Sólido',
  other: 'Outro',
};

const STATUS_LABELS: Record<string, string> = {
  pending: 'Pendente',
  completed: 'Finalizada',
  failed: 'Cancelada',
  in_process: 'Em Andamento',
};

const URGENCY_LABELS: Record<string, string> = {
  low: 'Baixa',
  medium: 'Moderada',
  high: 'Alta',
};

const typeLabel = computed(() => TYPE_LABELS[props.call.type]);
const statusLabel = computed(() => STATUS_LABELS[props.call.status]);
const urgencyLabel = computed(() => URGENCY_LABELS[props.call.urgency]);

const emit = defineEmits(['closeModal']);

const closeModal = () => {
  emit('closeModal', false);
};

const status_in_process = 'in_process';

//  ver pq não altera o status
const updateStatus = async () => {
  try {
    console.log(props.call.id);
    const resp = await apiClient.updateCallStatus(props.call.id, status_in_process);
    console.log(resp);
    closeModal();
  } catch (error: any) {
    error.value = error.message || 'Falha inesperada';
  }
};
</script>
<style scoped>
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(15, 28, 40, 0.45);
  backdrop-filter: blur(3px);
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 3rem 1.25rem 2rem;
  z-index: 1000;
  overflow-y: auto;
}

.modal {
  width: 100%;
  max-width: 720px;
  background: #ffffff;
  border: 1px solid #eef1f4;
  border-radius: 20px;
  box-shadow: 0 18px 40px -10px rgba(0, 25, 60, 0.25);
  display: flex;
  flex-direction: column;
  animation: popIn 0.28s ease;
  overflow: hidden;
}

@keyframes popIn {
  0% {
    opacity: 0;
    transform: translateY(18px) scale(0.96);
  }
  100% {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 1.4rem 0.9rem;
  border-bottom: 1px solid #f0f3f6;
  background: linear-gradient(180deg, #f7f9fb 0%, #fff 100%);
}

.modal-header h2 {
  margin: 0;
  font-size: 1.15rem;
  font-weight: 700;
  color: #032b81;
  letter-spacing: -0.5px;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.55rem;
  line-height: 1;
  cursor: pointer;
  color: #4d5b68;
  padding: 0.25rem 0.45rem;
  border-radius: 10px;
  transition: 0.18s;
}
.close-btn:hover {
  background: #eef3f7;
  color: #1d2b39;
}

.content {
  padding: 1.1rem 1.4rem 0.2rem;
}

.info-grid {
  display: grid;
  gap: 0.95rem 1.1rem;
  grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
}

.field {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  min-width: 0;
}

.field.wide {
  grid-column: 1 / -1;
}

.label {
  font-size: 0.66rem;
  text-transform: uppercase;
  font-weight: 700;
  letter-spacing: 0.9px;
  color: #2c333a;
}

.value {
  font-size: 0.83rem;
  font-weight: 600;
  color: #3d5b7e;
  line-height: 1.25;
  word-break: break-word;
}

.value.multiline {
  white-space: pre-wrap;
  font-weight: 500;
}

.status {
  display: inline-block;
  padding: 0.28rem 0.55rem;
  border-radius: 14px;
  font-size: 0.6rem;
  letter-spacing: 0.7px;
  text-transform: uppercase;
  font-weight: 700;
  background: #d0d6dd;
  color: #324552;
  width: fit-content;
}

.status-pending {
  background: #ffe8b2;
  color: #7a4b00;
}
.status-completed {
  background: #c6f6d5;
  color: #135c26;
}
.status-failed {
  background: #ffd3d3;
  color: #7a1313;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 0.6rem;
  padding: 0.9rem 1.4rem 1.15rem;
  border-top: 1px solid #f0f3f6;
  background: #f9fbfc;
  border-bottom-left-radius: 20px;
  border-bottom-right-radius: 20px;
}

.btn {
  border: none;
  font-size: 0.7rem;
  text-transform: uppercase;
  font-weight: 600;
  letter-spacing: 0.5px;
  padding: 0.65rem 1.05rem;
  border-radius: 12px;
  cursor: pointer;
  transition: 0.18s;
}

.btn.neutral {
  background: #d1d5d8;
  color: #131c25;
}

.btn.neutral:hover {
  background-color: #a7a8a8;
}

.btn.secondary {
  background: #2f7dd1;
  color: #fff;
}
.btn.secondary:hover {
  background: #2567ad;
}

@media (max-width: 560px) {
  .modal {
    border-radius: 18px;
  }
  .info-grid {
    grid-template-columns: 1fr 1fr;
  }
  .field.wide {
    grid-column: span 2;
  }
  .modal-header h2 {
    font-size: 1.05rem;
  }
}
</style>

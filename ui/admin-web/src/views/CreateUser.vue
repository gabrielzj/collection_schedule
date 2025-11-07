<template>
  <div class="page">
    <header class="top-bar">
      <h1>Novo Usuário</h1>
      <div class="actions">
        <RouterLink class="btn secondary" to="/">Voltar</RouterLink>
      </div>
    </header>

    <form class="card" @submit.prevent="onSubmit">
      <div class="stack">
        <div class="field">
          <label for="first_name">Nome</label>
          <input id="first_name" v-model.trim="form.first_name" required />
        </div>
        <div class="field">
          <label for="email">Email</label>
          <input id="email" v-model.trim="form.email" type="email" required />
        </div>
        <div class="field">
          <label for="password">Senha</label>
          <input
            id="password"
            v-model.trim="form.password"
            type="password"
            minlength="8"
            required
          />
        </div>
      </div>

      <div class="form-actions">
        <button class="btn primary" :disabled="loading">
          {{ loading ? 'Salvando...' : 'Salvar' }}
        </button>
        <button class="btn" type="button" @click="clear">Limpar</button>
      </div>

      <p v-if="success" class="success">Usuário criado com sucesso.</p>
      <p v-if="error" class="error">{{ error }}</p>
    </form>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue';
import { RouterLink } from 'vue-router';
import apiClient from '@/services/apiClient';

const form = reactive({
  first_name: '',
  email: '',
  password: '',
});

const loading = ref(false);
const error = ref<string | null>(null);
const success = ref(false);

function clear() {
  form.first_name = '';
  form.email = '';
  form.password = '';
  error.value = null;
  success.value = false;
}

async function onSubmit() {
  loading.value = true;
  error.value = null;
  success.value = false;
  try {
    await apiClient.registerUser({
      first_name: form.first_name,
      email: form.email,
      password: form.password,
    });
    success.value = true;
  } catch (e: any) {
    error.value = formatApiError(e);
  } finally {
    loading.value = false;
  }
}

// formtatar mensagem de erro da API
function formatApiError(err: any): string {
  const fallback = 'Não foi possível criar o usuário.';
  const data = err?.response?.data ?? err?.data ?? err;
  if (!data) return fallback;

  if (typeof data === 'object' && !Array.isArray(data)) {
    // Prioriza mensagens de campos mais comuns
    const preferredFields = ['email', 'password', 'first_name'];
    for (const f of preferredFields) {
      if (data[f]) {
        const v = data[f];
        if (Array.isArray(v)) return String(v[0]);
        return String(v);
      }
    }
    // Caso geral: pega a primeira mensagem disponível
    const firstKey = Object.keys(data)[0];
    if (firstKey) {
      const v = (data as any)[firstKey];
      if (Array.isArray(v)) return String(v[0]);
      if (typeof v === 'object') {
        const innerFirst = Object.values(v)[0] as any;
        if (Array.isArray(innerFirst)) return String(innerFirst[0]);
        if (innerFirst) return String(innerFirst);
      }
      return String(v ?? fallback);
    }
    return fallback;
  }
  if (Array.isArray(data)) return String(data[0] ?? fallback);
  if (typeof data === 'string') return data;
  if (data?.error) return String(data.error);
  if (data?.detail) return String(data.detail);
  return fallback;
}
</script>

<style scoped>
.page {
  max-width: 900px;
  margin: 0 auto;
  padding: 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.top-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.top-bar h1 {
  font-size: 1.55rem;
  margin: 0;
  color: #1d2b39;
}
.card {
  background: var(--card-bg);
  border-radius: 16px;
  padding: 1rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.06);
  border: 1px solid #d5d8db;
}
.stack {
  display: flex;
  flex-direction: column;
  gap: 0.9rem;
}
.grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.9rem;
}
.field.full {
  grid-column: 1 / -1;
}

.field label {
  display: block;
  font-size: 0.8rem;
  color: #415364;
  margin-bottom: 0.35rem;
}
.field input {
  width: 100%;
  padding: 0.6rem 0.75rem;
  border: 1px solid #d7dde2;
  border-radius: 10px;
  outline: none;
  font-size: 0.9rem;
  transition: 0.2s;
  background: #fff;
}
.field input:focus {
  border-color: #2f7dd1;
  box-shadow: 0 0 0 3px rgba(47, 125, 209, 0.15);
}
.form-actions {
  margin-top: 1rem;
  display: flex;
  gap: 0.5rem;
}
.btn {
  border: 1px solid #cfd8e3;
  background: #f7fafc;
  color: #1d2b39;
  padding: 0.6rem 0.9rem;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  text-decoration: none;
}
.btn.secondary {
  background: #eef3f7;
}
.btn.primary {
  background: var(--primary);
  color: #fff;
  border-color: var(--primary);
}
.btn.primary:hover {
  background: var(--primary-hover);
}

.success {
  margin-top: 0.75rem;
  color: #0d5c2f;
  background: #e6f6ec;
  border: 1px solid #b7e2c8;
  padding: 0.5rem 0.7rem;
  border-radius: 10px;
}
.error {
  margin-top: 0.75rem;
  color: #7a1111;
  background: #ffe1e1;
  border: 1px solid #ffb7b7;
  padding: 0.5rem 0.7rem;
  border-radius: 10px;
}

@media (max-width: 640px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>

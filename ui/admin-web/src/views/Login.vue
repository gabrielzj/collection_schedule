<template>
  <div class="auth-wrapper">
    <div class="auth-card">
      <h1>Admin</h1>
      <p class="subtitle">Acesse o painel para gerenciar os chamados</p>

      <form @submit.prevent="onSubmit" class="form">
        <div class="field">
          <label for="email">Email</label>
          <input
            id="email"
            v-model.trim="email"
            type="email"
            placeholder="seu@email.com"
            required
          />
        </div>
        <div class="field">
          <label for="password">Senha</label>
          <input
            id="password"
            v-model.trim="password"
            type="password"
            placeholder="••••••••"
            required
          />
        </div>

        <button class="submit" :disabled="loading">{{ loading ? 'Entrando...' : 'Entrar' }}</button>

        <p v-if="error" class="error">{{ error }}</p>
      </form>

      <div class="actions">
        <RouterLink to="/new">Criar usuário</RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRoute, useRouter, RouterLink } from 'vue-router';
import apiClient from '@/services/apiClient';

const route = useRoute();
const router = useRouter();

const email = ref('');
const password = ref('');
const loading = ref(false);
const error = ref<string | null>(null);

async function onSubmit() {
  error.value = null;
  loading.value = true;
  try {
    await apiClient.login(email.value, password.value);
    const next = (route.query.next as string) || '/';
    router.replace(next);
  } catch (e: any) {
    if (e?.response?.data?.detail) {
      error.value = e.response.data.detail;
    } else if (e?.response?.data?.error) {
      error.value = e.response.data.error;
    } else {
      error.value = 'Falha ao autenticar. Verifique suas credenciais.';
    }
  } finally {
    loading.value = false;
  }
}
</script>

<style scoped>
.auth-wrapper {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  background: transparent;
}
.auth-card {
  width: 100%;
  max-width: 420px;
  background: var(--card-bg);
  border-radius: 18px;
  padding: 2rem 1.5rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.06);
  border: 1px solid #d5d8db;
}
.auth-card h1 {
  margin: 0 0 0.25rem;
  font-size: 1.6rem;
  color: #1d2b39;
}
.subtitle {
  margin: 0 0 1.25rem;
  color: #5a6570;
  font-size: 0.9rem;
}
.form {
  display: flex;
  flex-direction: column;
  gap: 0.9rem;
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
.submit {
  margin-top: 0.2rem;
  background: var(--primary);
  color: #fff;
  border: 0;
  padding: 0.7rem 1rem;
  border-radius: 10px;
  font-weight: 700;
  letter-spacing: 0.5px;
  cursor: pointer;
  transition: 0.2s;
}
.submit:disabled {
  opacity: 0.65;
  cursor: not-allowed;
}
.submit:not(:disabled):hover {
  background: var(--primary-hover);
}

.error {
  margin-top: 0.6rem;
  color: #7a1111;
  background: #ffe1e1;
  border: 1px solid #ffb7b7;
  padding: 0.6rem 0.75rem;
  border-radius: 10px;
  font-size: 0.85rem;
}
.actions {
  margin-top: 1rem;
  text-align: center;
}
.actions a {
  color: #2f7dd1;
  font-weight: 600;
}
</style>

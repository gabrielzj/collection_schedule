<template>
  <div class="content">
    <Sidebar />
    <div class="users">
      <header class="top-bar">
        <div class="left">
          <h1>Usuários do Sistema</h1>
        </div>
      </header>

      <UsersList :users="users" :loading="loading" :error="error" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import Sidebar from '@/components/Sidebar.vue';
import UsersList from '@/components/UsersList.vue';
import apiClient from '@/services/apiClient';

interface UserItem {
  id: number;
  first_name?: string;
  last_name?: string;
  email: string;
}

const users = ref<UserItem[]>([]);
const loading = ref(false);
const error = ref<string | null>(null);

async function fetchUsers() {
  loading.value = true;
  error.value = null;
  try {
    const data = await apiClient.listUsers();
    users.value = (Array.isArray(data) ? data : []).map((u: any) => ({
      id: u.id,
      first_name: u.first_name,
      last_name: u.last_name,
      email: u.email,
    }));
  } catch (e: any) {
    error.value = e?.message || 'Falha ao carregar usuários';
  } finally {
    loading.value = false;
  }
}

onMounted(fetchUsers);
</script>

<style scoped>
.content {
  display: flex;
  min-height: 100vh;
}
.users {
  flex: 1;
  max-width: 1000px;
  margin: 0 auto;
  padding: 1.25rem 1.25rem 2.5rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-left: 216px; /* compensar sidebar fixa */
}
@media (max-width: 900px) {
  .users {
    margin-left: 0;
  }
}
.top-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}
.top-bar h1 {
  font-size: 1.55rem;
  line-height: 1.1;
  margin: 0;
  font-weight: 700;
  color: #1d2b39;
  letter-spacing: -0.5px;
}
</style>

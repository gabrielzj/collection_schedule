<template>
  <div class="users-card">
    <div v-if="error" class="error">{{ error }}</div>

    <table v-else class="table">
      <thead>
        <tr>
          <th>Nome</th>
          <th class="th-with-counter">
            <div class="th-inner">
              <span class="email">E-mail</span>
              <span v-if="!loading" class="count">{{ users.length }} registros</span>
              <span v-else class="pulse">Carregando...</span>
            </div>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="u in users" :key="u.id">
          <td>{{ fullName(u) }}</td>
          <td>
            <a :href="`mailto:${u.email}`">{{ u.email }}</a>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
interface UserItem {
  id: number;
  first_name?: string;
  last_name?: string;
  email: string;
}

const props = defineProps<{
  users: UserItem[];
  loading?: boolean;
  error?: string | null;
}>();

function fullName(u: UserItem) {
  const first = (u.first_name || '').trim();
  const last = (u.last_name || '').trim();
  if (first && last) {
    return `${first} ${last}`;
  }
  if (first) {
    return first;
  }
  return last || '-';
}
</script>

<style scoped>
.users-card {
  background: #ffffff;
  border: 1px solid #e4e8ee;
  border-radius: 14px;
  padding: 1rem;
}
.count {
  background: #eef3f7;
  padding: 0.25rem 0.5rem;
  border-radius: 12px;
  font-size: 0.8rem;
  color: #5a6570;
}
.pulse {
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
.table {
  width: 100%;
  border-collapse: collapse;
}
.table th,
.table td {
  text-align: left;
  padding: 0.6rem 0.4rem;
  border-bottom: 1px solid #eef1f4;
  font-size: 0.9rem;
}
.table th,
.email {
  color: #344054;
  font-weight: 700;
}
.th-with-counter .th-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
}
.table tbody tr:hover {
  background: #f8fafc;
}
.table a {
  color: #2f7dd1;
  text-decoration: none;
}
.table a:hover {
  text-decoration: underline;
}
.error {
  background: #ffe1e1;
  border: 1px solid #ffb7b7;
  color: #7a1111;
  padding: 0.75rem;
  border-radius: 10px;
}
</style>

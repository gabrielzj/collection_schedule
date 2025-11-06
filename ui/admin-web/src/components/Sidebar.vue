<template>
  <aside class="sidebar-container">
    <div class="sidebar-header">
      <h2>Menu</h2>
    </div>

    <nav class="sidebar-links">
      <router-link to="/" class="item" active-class="active">
        <!-- ícone -->
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="18"
          height="18"
          fill="currentColor"
          viewBox="0 0 16 16"
        >
          <path
            d="M12.643 15C13.979 15 15 13.845 15 12.5V5H1v7.5C1 13.845 2.021 15 3.357 15zM5.5 7h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1 0-1M.8 1a.8.8 0 0 0-.8.8V3a.8.8 0 0 0 .8.8h14.4A.8.8 0 0 0 16 3V1.8a.8.8 0 0 0-.8-.8z"
          />
        </svg>
        <span>Chamados</span>
      </router-link>

      <router-link to="/stats" class="item" active-class="active">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="18"
          height="18"
          fill="currentColor"
          viewBox="0 0 16 16"
        >
          <path
            d="M11 2a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v12h.5a.5.5 0 0 1 0 1H.5a.5.5 0 0 1 0-1H1v-3a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3h1V7a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7h1z"
          />
        </svg>
        <span>Estatísticas</span>
      </router-link>

      <router-link to="/users" class="item" active-class="active">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="18"
          height="18"
          fill="currentColor"
          viewBox="0 0 16 16"
        >
          <path
            d="M7 14s-1 0-1-1 1-4 5-4 5 3 5 4-1 1-1 1zm4-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6m-5.784 6A2.24 2.24 0 0 1 5 13c0-1.355.68-2.75 1.936-3.72A6.3 6.3 0 0 0 5 9c-4 0-5 3-5 4s1 1 1 1zM4.5 8a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5"
          />
        </svg>
        <span>Usuários</span>
      </router-link>
    </nav>

    <div class="sidebar-footer">
      <button class="logout-btn" @click="doLogout">
        <!-- ícone sair -->
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="18"
          height="18"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4" />
          <polyline points="16 17 21 12 16 7" />
          <line x1="21" y1="12" x2="9" y2="12" />
        </svg>
        <span>Sair</span>
      </button>
    </div>
  </aside>
</template>

<script setup lang="ts">
import apiClient from '@/services/apiClient';

async function doLogout() {
  await apiClient.logout();
}
</script>

<style scoped>
.sidebar-container {
  width: 200px;
  min-width: 200px;

  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;

  background: #ffffff;
  border: 0 !important;
  box-shadow: none !important;
  outline: none !important;

  z-index: 1000;

  display: flex;
  flex-direction: column;

  border-radius: 0 20px 20px 0;
}

.sidebar-header {
  padding: 1rem 1rem;
  border: 0;
}
.sidebar-header h2 {
  margin: 0;
  font-size: 1rem;
  color: #1d2b39;
  letter-spacing: -0.2px;
}

.sidebar-links {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  padding: 0.5rem;
  flex: 1;
}

.item {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  padding: 0.6rem 0.8rem;
  border-radius: 10px;
  color: #344054;
  text-decoration: none;
  font-weight: 600;
  transition:
    background 0.15s ease,
    color 0.15s ease;
}

.item svg {
  color: #5b6b7c;
}
.item:hover {
  background: #f5f8fa;
  color: #1d2b39;
}

.item.active {
  background: #e9f2fb;
  color: #1b4f8a;
}
.item.active svg {
  color: #2f7dd1;
}

/* Mobile: empilha no topo e sem offset no conteúdo */
@media (max-width: 900px) {
  .sidebar-container {
    position: static;
    width: 100%;
    min-width: 0;
    height: auto;
  }
  .sidebar-links {
    flex-direction: row;
    flex-wrap: wrap;
    gap: 0.25rem;
    padding: 0.5rem;
  }
  .item {
    flex: 1 1 180px;
  }
}

.sidebar-footer {
  padding: 0.75rem 0.75rem 1rem;
}
.logout-btn {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  border: 1px solid #7a1111; /* contorno forte */
  background: #fde9e9; /* vermelho claro no preenchimento */
  color: #7a1111; /* texto em vermelho escuro para contraste */
  padding: 0.6rem 0.8rem;
  border-radius: 10px;
  font-weight: 700;
  cursor: pointer;
}
.logout-btn:hover {
  background: #f7d6d6; /* leve escurecimento no hover, ainda claro */
}
</style>

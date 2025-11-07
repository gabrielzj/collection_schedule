import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from '@/views/Dashboard.vue';
import Login from '@/views/Login.vue';
import CreateUser from '@/views/CreateUser.vue';
import Stats from '@/views/Stats.vue';
import Users from '@/views/Users.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: { public: true },
    },
    {
      path: '/',
      name: 'dashboard',
      component: Dashboard,
    },
    {
      path: '/stats',
      name: 'statistics',
      component: Stats,
    },
    {
      path: '/users',
      name: 'users',
      component: Users,
    },
    {
      path: '/new',
      name: 'create-user',
      component: CreateUser,
      meta: { public: true },
    },
  ],
});

router.beforeEach((to, _from, next) => {
  const isPublic = to.meta && (to.meta as any).public;
  const token = localStorage.getItem('accessToken');
  if (!isPublic && !token) {
    next({ name: 'login', query: { next: to.fullPath } });
    return;
  }
  next();
});

export default router;

import { createRouter, createWebHistory } from "@ionic/vue-router";
import { RouteRecordRaw } from "vue-router";
import TabsPage from "../views/TabsPage.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    redirect: "/login",
  },
  {
    path: "",
    redirect: "/login",
  },
  {
    path: "/login",
    component: () => import("@/views/login-page.vue"),
  },
  {
    path: "/register",
    component: () => import("@/views/register.vue"),
  },
  {
    path: "/home",
    component: TabsPage,
    children: [
      {
        path: "waste-info",
        component: () => import("@/views/Tab1Page.vue"),
      },
      {
        path: "call",
        component: () => import("@/views/Tab2Page.vue"),
      },
      {
        path: "login",
        component: () => import("@/views/login-page.vue"),
      },
      {
        path: "tab4",
        component: () => import("@/views/Tab3Page.vue"),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;

import { createRouter, createWebHistory } from "@ionic/vue-router";
import { RouteRecordRaw } from "vue-router";
import FooterBar from "@/views/FooterBar.vue";
import WasteTypes from "@/views/WasteTypes.vue";
import CreateCall from "@/views/CreateCall.vue";
import loginPage from "@/views/login.vue";
import registerPage from "@/views/Register.vue";
import MyCallsPage from "@/views/MyCallsPage.vue";
import Logout from "@/views/Logout.vue";
import userInfo from "@/views/UserInfo.vue";
import apiClient from "@/services/apiClient";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Root",
    redirect: "/login",
  },
  {
    path: "",
    redirect: "/login",
  },
  {
    path: "/login",
    name: "Login",
    component: loginPage,
  },
  {
    path: "/register",
    name: "Register",
    component: registerPage,
  },
  {
    path: "/home",
    meta: { requiresAuth: true },
    component: FooterBar,
    children: [
      {
        path: "",
        component: MyCallsPage,
      },
      {
        path: "waste-info",
        name: "WasteInfo",
        component: WasteTypes,
      },
      {
        path: "call",
        name: "Call",
        component: CreateCall,
      },
      {
        path: "user",
        name: "user",
        component: userInfo,
      },
      {
        path: "logout",
        name: "Logout",
        component: Logout,
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

router.beforeEach(async (to, _from, next) => {
  const isAuthRoute =
    to.path === "/login" || to.name === "Login" || to.name === "Register";
  const needsAuth = to.matched.some((r) => r.meta?.requiresAuth);

  const logged = await apiClient.hasValidSession();

  if (isAuthRoute && logged) return next("/home");
  if (needsAuth && !logged) return next("/login");
  return next();
});

export default router;

import { createRouter, createWebHistory } from "@ionic/vue-router";
import { RouteRecordRaw } from "vue-router";
import TabsPage from "../views/TabsPage.vue";
import Tab1Page from "@/views/Tab1Page.vue";
import Tab2Page from "@/views/Tab2Page.vue";
import loginPage from "@/views/login.vue";
import registerPage from "@/views/register.vue";
import MyCallsPage from "@/views/MyCallsPage.vue";
import logout from "@/views/logout.vue";

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
    component: TabsPage,
    children: [
      {
        path: "",
        component: MyCallsPage,
      },
      {
        path: "waste-info",
        name: "WasteInfo",
        component: Tab1Page,
      },
      {
        path: "call",
        name: "Call",
        component: Tab2Page,
      },
      {
        path: "logout",
        name: "Logout",
        component: logout,
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;

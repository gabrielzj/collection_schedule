<template>
  <!-- <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Tab 3</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Tab 3</ion-title>
        </ion-toolbar>
      </ion-header>

      <ExploreContainer name="Tab 3 page" />
    </ion-content>
  </ion-page> -->
</template>

<script setup lang="ts">
// import router from "@/router";
import { onMounted } from "vue";
import { onIonViewWillEnter, useIonRouter } from "@ionic/vue";
const ionRouter = useIonRouter();

// import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
// import ExploreContainer from '@/components/ExploreContainer.vue';

function clearAuth() {
  try {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    localStorage.removeItem("user_id");
    sessionStorage.removeItem("access_token");
    sessionStorage.removeItem("refresh_token");
    sessionStorage.removeItem("user_id");
  } catch (e) {
    console.warn("Falha ao limpar credenciais:", e);
  }
}

function goToLogin() {
  ionRouter.navigate("/login", "root");
}

onIonViewWillEnter(() => {
  clearAuth();
  goToLogin();
});

onMounted(() => {
  clearAuth();
  goToLogin();
});
</script>

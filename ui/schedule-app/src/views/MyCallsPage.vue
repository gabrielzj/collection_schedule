<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title color="dark">Bem-vindo, {{ userName }}</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true" class="ion-padding" mode="md">
      <ion-text color="medium">
        <h2>Meus Chamados: {{ calls.length }}</h2>
      </ion-text>
      <CollectionCallList />
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonText,
} from "@ionic/vue";
import CollectionCallList from "@/components/CollectionCallList.vue";
import apiClient from "@/services/apiClient";
import { onBeforeMount, ref } from "vue";

const userName = ref<string>("");
const calls = ref<Array<any>>([]);

// ver de receber o name do backend no login
onBeforeMount(async () => {
  try {
    const data = await apiClient.getUser(localStorage.getItem("user_id"));
    userName.value = data["username"];
  } catch (error: any) {
    console.error("Falha ao buscar usuário");
  }
});
</script>

<style scoped></style>

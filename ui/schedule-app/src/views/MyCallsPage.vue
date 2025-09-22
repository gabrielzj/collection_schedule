<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title color="dark"
          >Bem-vindo, {{ first_name }} {{ last_name }}</ion-title
        >
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true" class="ion-padding" mode="md">
      <ion-text color="medium">
        <h2>Meus Chamados: {{ qtdCalls }}</h2>
      </ion-text>
      <CollectionCallList @qtd-calls="userCalls" />
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

// const userName = ref<string>("");
const first_name = ref<string>("");
const last_name = ref<string>("");
const qtdCalls = ref<number>(0);

function userCalls(qtd: number) {
  qtdCalls.value = qtd;
}

// ver de receber o name do backend no login
onBeforeMount(async () => {
  try {
    const data = await apiClient.getUser(localStorage.getItem("user_id"));
    first_name.value = data["first_name"];
    last_name.value = data["last_name"];
  } catch (error: any) {
    console.error("Falha ao buscar usuário");
  }
});
</script>

<style scoped></style>

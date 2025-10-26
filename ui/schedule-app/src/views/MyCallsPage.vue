<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title color="dark" v-if="first_name || last_name"
          >Bem-vindo, {{ first_name }} {{ last_name }}</ion-title
        >
        <ion-title v-else>Bem-vindo, Usuário</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true" class="ion-padding" mode="md">
      <ion-refresher slot="fixed" @ionRefresh="handleRefresh($event)">
        <ion-refresher-content></ion-refresher-content>
      </ion-refresher>
      <ion-text color="medium">
        <h2>Meus Chamados: {{ qtdCalls }}</h2>
      </ion-text>
      <CollectionCallList
        ref="listRef"
        @updateCalls="updateCalls"
        @qtdCalls="userCalls"
      />
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
  IonRefresherContent,
  IonRefresher,
  RefresherCustomEvent,
} from "@ionic/vue";
import CollectionCallList from "@/components/CollectionCallList.vue";
import apiClient from "@/services/apiClient";
import { onBeforeMount, ref } from "vue";

const listRef = ref<InstanceType<typeof CollectionCallList> | null>(null);

const handleRefresh = async (event: RefresherCustomEvent) => {
  try {
    await listRef.value?.refresh();
    await fetchUserData();
  } catch (error: any) {
    console.error("Falha ao buscar usuário");
  } finally {
    event.target.complete();
  }
};

const first_name = ref<string>("");
const last_name = ref<string>("");
const qtdCalls = ref<number>(0);

function userCalls(qtd: number) {
  console.log("User calls qtd:", qtd);
  qtdCalls.value = qtd;
}

function updateCalls(qtd: number) {
  console.log("Update calls qtd:", qtd);
  qtdCalls.value = qtd;
}

async function fetchUserData() {
  try {
    const data = await apiClient.getUser(localStorage.getItem("user_id"));
    first_name.value = data["first_name"];
    last_name.value = data["last_name"];
  } catch (error: any) {
    console.error("Falha ao buscar usuário");
  }
}
// ver de receber o name do backend no login
onBeforeMount(() => {
  fetchUserData();
});
</script>

<style scoped></style>

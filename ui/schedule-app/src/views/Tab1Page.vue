<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Tipos de resíduos</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Teste</ion-title>
        </ion-toolbar>
      </ion-header>

      <div class="waste-info-container">
        <WasteInfoCard
          v-for="(item, index) in wasteInfo"
          :key="index"
          @click="openModal(item.type)"
          :image="item.image"
          :title="item.title"
          :description="item.description"
        />
      </div>
      <WasteInfoModal
        v-for="(modal, index) in wasteModal"
        :key="index"
        :is-open="isModalOpen[modal.type]"
        @dismiss="closeModal(modal.type)"
        :title="modal.title"
      />
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { ref } from "vue";

import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
} from "@ionic/vue";
import WasteInfoCard from "@/components/WasteInfoCard.vue";
import WasteInfoModal from "@/components/WasteInfoModal.vue";

type WasteType = "paper" | "metal" | "plastic";

interface WasteInfo {
  type: WasteType;
  image: string;
  title: string;
  description: string;
}

interface WasteModal {
  type: WasteType;
  title: string;
}

const wasteInfo: WasteInfo[] = [
  {
    type: "paper",
    image: "/src/assets/paper-waste.jpg",
    title: "Papéis",
    description:
      "Descarte papéis de forma correta e contribua para a preservação ambiental. Saiba como separar, armazenar e encaminhar o papel para reciclagem",
  },
  {
    type: "metal",
    image: "/src/assets/metal-waste.jpg",
    title: "Metais",
    description:
      "Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae",
  },
  {
    type: "plastic",
    image: "/src/assets/plastic-waste.jpg",
    title: "Plásticos",
    description:
      "Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae",
  },
];

const wasteModal: WasteModal[] = [
  {
    type: "paper",
    title: "Papéis",
  },
  {
    type: "metal",
    title: "Metais",
  },
  {
    type: "plastic",
    title: "Plásticos",
  },
];

const isModalOpen = ref({
  paper: false,
  metal: false,
  plastic: false,
});

const openModal = (type: WasteType) => {
  isModalOpen.value[type] = true;
};

const closeModal = (type: WasteType) => {
  isModalOpen.value[type] = false;
};
</script>

<style scoped>
.waste-info-container {
  padding: 16px;
  justify-content: center;
  align-items: center;
  display: flex;
  flex-direction: column;
  width: 100%;
}
</style>

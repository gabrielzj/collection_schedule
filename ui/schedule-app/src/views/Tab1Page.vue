<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Informações de descarte</ion-title>
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
        v-for="(modal, index) in wasteModals"
        :key="index"
        :is-open="isModalOpen[modal.type]"
        @dismiss="closeModal(modal.type)"
        :title="modal.title"
        :description="modal.description"
      />
    </ion-content>
  </ion-page>
</template>

<script setup>
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

const wasteInfo = [
  {
    type: "paper",
    image: "/src/assets/paper-waste.jpg",
    title: "Papéis",
    description:
      "Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae",
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

const wasteModals = [
  {
    type: "paper",
    title: "Papéis",
    description:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vel nisi nec justo.",
  },
  {
    type: "metal",
    title: "Metais",
    description:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vel nisi nec justo.",
  },
  {
    type: "plastic",
    title: "Plásticos",
    description:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vel nisi nec justo.",
  },
];

const isModalOpen = ref({
  paper: false,
  metal: false,
  plastic: false,
});

const openModal = (type) => {
  isModalOpen.value[type] = true;
};

const closeModal = (type) => {
  isModalOpen.value[type] = false;
};
</script>

<style scoped>
.waste-info-container {
  padding: 50px;
  justify-content: center;
  align-items: center;
  display: flex;
  flex-direction: column;
  width: 100%;
}
</style>

<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-back-button default-href="/home"></ion-back-button>
        </ion-buttons>
        <ion-title>Tipos de resíduos</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true" mode="md">
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
        :id="modal.id"
      />
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { ref } from "vue";
// const reloadContent = ref(0);

// onIonViewWillEnter(() => {
//   reloadContent.value++;
// });

//TODO: adicionar novos tipos de resíduos, perigosos, talvez borracha

import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonButtons,
  IonBackButton,
} from "@ionic/vue";
import WasteInfoCard from "@/components/WasteInfoCard.vue";
import WasteInfoModal from "@/components/WasteInfoModal.vue";
import eWaste from "@/assets/e-waste.jpg";
import glassWaste from "@/assets/glass-waste.jpg";
import metalWaste from "@/assets/metal-waste.jpg";
import organicWaste from "@/assets/organic-waste.jpg";
import otherWaste from "@/assets/other-waste.jpg";
import paperWaste from "@/assets/paper-waste.jpg";
import recyclableWaste from "@/assets/recyclable-waste.jpg";
import plasticWaste from "@/assets/plastic-waste.jpg";
import residualWaste from "@/assets/residual-waste.jpg";
import specialWaste from "@/assets/special-waste.jpg";

type WasteType =
  | "paper"
  | "metal"
  | "plastic"
  | "electronic"
  | "organic"
  | "glass"
  | "residual_waste"
  | "special"
  | "other";

interface WasteInfo {
  type: WasteType;
  image: string;
  title: string;
  description: string;
}

interface WasteModal {
  type: WasteType;
  title: string;
  id: number;
}

// alterar import das imagens para evitar problemas no build
const wasteInfo: WasteInfo[] = [
  {
    type: "paper",
    image: paperWaste,
    title: "Papel",
    description:
      "Descarte papéis de forma correta e contribua para a preservação ambiental. Saiba como separar, armazenar e encaminhar o papel para reciclagem",
  },
  {
    type: "metal",
    image: metalWaste,
    title: "Metal",
    description:
      "Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae",
  },
  {
    type: "plastic",
    image: plasticWaste,
    title: "Plástico",
    description:
      "Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae",
  },
  {
    type: "electronic",
    image: eWaste,
    title: "Eletrônico",
    description:
      "Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae",
  },
  {
    type: "organic",
    image: organicWaste,
    title: "Orgânico",
    description:
      "Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae",
  },
  {
    type: "glass",
    image: glassWaste,
    title: "Vidro",
    description:
      "Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae",
  },
  {
    type: "residual_waste",
    image: residualWaste,
    title: "Rejeitos",
    description:
      "Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae",
  },
  {
    type: "other",
    image: otherWaste,
    title: "Outros",
    description:
      "Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae",
  },
  {
    type: "special",
    image: specialWaste,
    title: "Especial",
    description:
      "Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae",
  },
];

const wasteModal: WasteModal[] = [
  {
    type: "paper",
    title: "Papel",
    id: 1,
  },
  {
    type: "metal",
    title: "Metal",
    id: 2,
  },
  {
    type: "plastic",
    title: "Plástico",
    id: 3,
  },
  {
    type: "electronic",
    title: "Eletrônico",
    id: 4,
  },
  {
    type: "organic",
    title: "Orgânico",
    id: 5,
  },
  {
    type: "glass",
    title: "Vidro",
    id: 6,
  },
  {
    type: "residual_waste",
    title: "Rejeitos",
    id: 7,
  },
  {
    type: "other",
    title: "Outros",
    id: 8,
  },
  {
    type: "special",
    title: "Especiais",
    id: 9,
  },
];

const isModalOpen = ref({
  paper: false,
  metal: false,
  plastic: false,
  electronic: false,
  organic: false,
  glass: false,
  residual_waste: false,
  other: false,
  special: false,
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
  display: grid;
  padding: 16px;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  max-width: 640px;
  margin: 0 auto;
  justify-content: center;
  justify-self: center;
  gap: 15px;
  align-items: center;
}

@media (max-width: 700px) {
  .waste-info-container {
    grid-template-columns: 300px;
    justify-content: center;
  }
}

@media (min-width: 700px) {
  .waste-info-container {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>

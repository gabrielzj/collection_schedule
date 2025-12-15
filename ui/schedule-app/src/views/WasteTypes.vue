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
      "Recicle papéis e ajude a reduzir o desperdício. Separe, dobre e encaminhe corretamente!",
  },
  {
    type: "metal",
    image: metalWaste,
    title: "Metal",
    description:
      "Dê nova vida às latas e sucatas! Reciclar metal economiza energia e preserva recursos.",
  },
  {
    type: "plastic",
    image: plasticWaste,
    title: "Plástico",
    description:
      "Transforme o plástico em algo útil. Limpe, separe e encaminhe para reciclagem.",
  },
  {
    type: "electronic",
    image: eWaste,
    title: "Eletrônico",
    description:
      "Descubra como descartar eletrônicos com segurança e evitar danos ao meio ambiente.",
  },
  {
    type: "organic",
    image: organicWaste,
    title: "Orgânico",
    description:
      "Restos de comida e folhas viram adubo! Separe corretamente e contribua com a compostagem.",
  },
  {
    type: "glass",
    image: glassWaste,
    title: "Vidro",
    description:
      "Vidros podem ser reciclados infinitas vezes. Lave bem e evite misturar com outros resíduos.",
  },
  {
    type: "residual_waste",
    image: residualWaste,
    title: "Rejeitos",
    description:
      "São resíduos sem reaproveitamento. Reduza ao máximo e descarte de forma responsável.",
  },
  {
    type: "other",
    image: otherWaste,
    title: "Outros",
    description:
      "Resíduos que não se encaixam nas outras categorias. Informe-se sobre o destino correto.",
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
  // {
  //   type: "special",
  //   title: "Especiais",
  //   id: 9,
  // },
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

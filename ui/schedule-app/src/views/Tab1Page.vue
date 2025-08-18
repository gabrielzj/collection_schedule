<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Tipos de resíduos</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true" :key="reloadContent">
      <ion-header collapse="condense"> </ion-header>

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
import { onIonViewWillEnter } from "@ionic/vue";
const reloadContent = ref(0);

onIonViewWillEnter(() => {
  reloadContent.value++;
});


//TODO: adicionar novos tipos de resíduos, perigosos, talvez borracha

//TODO: ver o pq de ao ser redirecionado para a tela, alguns estilos quebram.

import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
} from "@ionic/vue";
import WasteInfoCard from "@/components/WasteInfoCard.vue";
import WasteInfoModal from "@/components/WasteInfoModal.vue";

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

const wasteInfo: WasteInfo[] = [
  {
    type: "paper",
    image: "/src/assets/paper-waste.jpg",
    title: "Papel",
    description:
      "Descarte papéis de forma correta e contribua para a preservação ambiental. Saiba como separar, armazenar e encaminhar o papel para reciclagem",
  },
  {
    type: "metal",
    image: "/src/assets/metal-waste.jpg",
    title: "Metal",
    description:
      "Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae",
  },
  {
    type: "plastic",
    image: "/src/assets/plastic-waste.jpg",
    title: "Plástico",
    description:
      "Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae",
  },
  {
    type: "electronic",
    image: "/src/assets/e-waste.jpg",
    title: "Eletrônico",
    description:
      "Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae",
  },
  {
    type: "organic",
    image: "/src/assets/organic-waste.jpg",
    title: "Orgânico",
    description:
      "Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae",
  },
  {
    type: "glass",
    image: "/src/assets/glass-waste.jpg",
    title: "Vidro",
    description:
      "Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae",
  },
  {
    type: "residual_waste",
    image: "/src/assets/residual-waste.jpg",
    title: "Rejeitos",
    description:
      "Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae",
  },
  {
    type: "other",
    image: "/src/assets/other-waste.jpg",
    title: "Outros",
    description:
      "Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae",
  },
  {
    type: "special",
    image: "/src/assets/special-waste.jpg",
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

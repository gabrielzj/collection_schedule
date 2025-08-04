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
          @click="openModalPaper"
          image="/src/assets/paper-waste.jpg"
          title="Papéis"
          description="Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus  dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae"
        />
        <WasteInfoCard
          @click="openModalMetal"
          image="/src/assets/metal-waste.jpg"
          title="Metais"
          description="Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus  dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae"
        />
        <WasteInfoCard
          @click="openModalPlastic"
          image="/src/assets/plastic-waste.jpg"
          title="Plásticos"
          description="Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus  dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae"
        />
      </div>
      <WasteInfoModal
        :is-open="isModalOpenPaper"
        @dismiss="closeModal"
        title="Papéis"
        description="Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus  dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae"
      />
      <WasteInfoModal
        :is-open="isModalOpenMetal"
        @dismiss="closeModal"
        title="Metais"
        description="Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus  dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae"
      />
      <WasteInfoModal
        :is-open="isModalOpenPlastic"
        @dismiss="closeModal"
        title="Plásticos"
        description="Lorem ipsum dolor sit amet. At beatae porro et amet velit est delectus  dolorum sit amet nostrum. Est corporis repellendus ab iste dolorem est magnam quae"
      />
      <!-- <ExploreContainer name="Tab 1 page" /> -->
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
// import ExploreContainer from "@/components/ExploreContainer.vue";
import WasteInfoCard from "@/components/WasteInfoCard.vue";
import WasteInfoModal from "@/components/WasteInfoModal.vue";

const isModalOpenPaper = ref(false);
const isModalOpenMetal = ref(false);
const isModalOpenPlastic = ref(false);

const openModalPaper = () => {
  isModalOpenPaper.value = true;
};

const openModalMetal = () => {
  isModalOpenMetal.value = true;
};

const openModalPlastic = () => {
  isModalOpenPlastic.value = true;
};

const closeModal = () => {
  isModalOpenPaper.value = false;
  isModalOpenMetal.value = false;
  isModalOpenPlastic.value = false;
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

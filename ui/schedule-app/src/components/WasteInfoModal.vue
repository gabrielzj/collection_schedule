<template>
  <ion-modal :is-open="isOpen" @didDismiss="closeModal">
    <ion-header>
      <ion-toolbar>
        <ion-title>{{ title }}</ion-title>
        <ion-buttons slot="end">
          <ion-button @click="closeModal">
            <ion-icon :icon="closeOutline"></ion-icon>
          </ion-button>
        </ion-buttons>
      </ion-toolbar>
    </ion-header>

    <ion-content class="ion-padding">
      <h4>Manuseio</h4>
      <p>{{ description }}</p>
      <ion-button @click="closeModal" class="close-button" expand="block">
        Fechar
      </ion-button>
    </ion-content>
  </ion-modal>
</template>

<script setup>
import {
  IonModal,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonButton,
  IonButtons,
  IonIcon,
} from "@ionic/vue";
import { closeOutline } from "ionicons/icons";

defineProps({
  isOpen: {
    type: Boolean,
    required: false,
  },
  title: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    required: true,
  },
});

const emit = defineEmits(["dismiss"]);

const closeModal = () => {
  emit("dismiss");
};
</script>

<style scoped>
.close-button {
  font-family: Inter, sans-serif;
}

p {
  color: #5a5a5a;
}
</style>

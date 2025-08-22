<template>
  <ion-card>
    <img :alt="title" :src="image" />
    <ion-card-header>
      <ion-card-title>{{ title }}</ion-card-title>
      <!-- <ion-card-subtitle>Card Subtitle</ion-card-subtitle> -->
    </ion-card-header>

    <ion-card-content>
      {{ description }}
    </ion-card-content>
  </ion-card>
</template>

<script setup>
import {
  IonCard,
  IonCardContent,
  IonCardHeader,
  // IonCardSubtitle,
  IonCardTitle,
  IonPage,
} from "@ionic/vue";

defineProps({
  image: {
    type: String,
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
</script>

<style scoped>
ion-card {
  border-radius: 20px;
  cursor: pointer;
  transition: transform 0.2s ease-in-out;
  max-width: 300px;
}

img {
  width: 100%;
  max-width: 100%;
  max-height: 150px;
  object-fit: cover;
  border-radius: 20px 20px 0 0;
}

ion-card-content {
  text-align: justify;
  text-justify: inter-word;
  hyphens: auto;
}
</style>

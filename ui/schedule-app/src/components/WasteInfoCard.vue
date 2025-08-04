<template>
  <ion-card>
    <img alt="Recicláveis" :src="image" />
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
} from "@ionic/vue";

defineProps({
  image: {
    type: String,
    required: true,
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
}

ion-card:hover {
  transform: translateY(-2px);
}

img {
  width: 100%;
  max-width: fit-content;
  max-height: 150px;
  object-fit: cover;
  border-radius: 20px 20px 0 0;
}

@media (min-width: 500px) {
  /* img {
    max-width: fit-content;
  } */

  ion-card {
    max-width: 400px;
  }

  ion-card-title {
    font-size: 1.5rem;
  }

  ion-card-content {
    font-size: 1rem;
  }
}

ion-card-content {
  text-align: justify;
  text-justify: inter-word;
}
</style>

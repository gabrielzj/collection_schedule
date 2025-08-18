<template>
  <ion-page>
    <ion-content>
      <ion-tabs>
        <ion-router-outlet></ion-router-outlet>
        <ion-tab-bar slot="bottom">
          <ion-tab-button tab="tab1" href="/home/tab1">
            <ion-icon aria-hidden="true" :icon="trashBin" />
            <ion-label>Resíduos</ion-label>
          </ion-tab-button>

          <ion-tab-button tab="tab2" href="/home/tab2">
            <ion-icon aria-hidden="true" :icon="ellipse" />
            <ion-label>Tab 2</ion-label>
          </ion-tab-button>

          <ion-tab-button tab="tab3" href="/home/tab3">
            <ion-icon aria-hidden="true" :icon="square" />
            <ion-label>Tab 3</ion-label>
          </ion-tab-button>
          <ion-tab-button tab="tab4" href="/home/tab4">
            <ion-icon aria-hidden="true" :icon="atCircle" />
            <ion-label>Tab 4</ion-label>
          </ion-tab-button>
        </ion-tab-bar>
      </ion-tabs>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import {
  IonTabBar,
  IonTabButton,
  IonTabs,
  IonLabel,
  IonIcon,
  IonPage,
  IonRouterOutlet,
  IonContent,
} from "@ionic/vue";
import { atCircle, ellipse, square, trashBin } from "ionicons/icons";
</script>

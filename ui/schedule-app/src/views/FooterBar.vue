<template>
  <ion-page>
    <ion-tabs>
      <ion-router-outlet></ion-router-outlet>
      <ion-tab-bar slot="bottom">
        <ion-tab-button tab="waste-info" href="/home/waste-info">
          <ion-icon aria-hidden="true" :icon="trashBin" />
          <ion-label>Resíduos</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="call" href="/home/call">
          <ion-icon aria-hidden="true" :icon="archive" />
          <ion-label>Coleta</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="tab3" href="/home/user">
          <ion-icon aria-hidden="true" :icon="personCircle" />
          <ion-label>Usuário</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="tab4" href="/home/logout">
          <ion-icon aria-hidden="true" :icon="logOut" />
          <ion-label>Sair</ion-label>
        </ion-tab-button>
      </ion-tab-bar>
    </ion-tabs>
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
} from "@ionic/vue";
import { trashBin, logOut, archive, personCircle } from "ionicons/icons";
</script>

<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Criar um chamado</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true" mode="md">
      <ion-item class="title" lines="none" color="secondary">
        <ion-icon :icon="helpOutline"></ion-icon>
        <h5>Como funciona</h5>
      </ion-item>
      <ion-label class="intro-text"
        >Preencha os campos abaixo para criar um <b>chamado de coleta</b>.
        Informe o tipo de resíduo, descrição, quantidade e urgência.</ion-label
      >
      <ion-item-divider></ion-item-divider>
      <ion-list :inset="true">
        <ion-item lines="none">
          <ion-select
            aria-label="waste-type"
            interface="alert"
            label="Tipo de Resíduo"
            label-placement="floating"
            fill="solid"
          >
            <ion-select-option value="plastic">Plástico</ion-select-option>
            <ion-select-option value="paper">Papel</ion-select-option>
            <ion-select-option value="metal">Metal</ion-select-option>
            <ion-select-option value="glass">Vidro</ion-select-option>
            <ion-select-option value="organic">Orgânico</ion-select-option>
            <ion-select-option value="electronic">Eletrônico</ion-select-option>
            <ion-select-option value="other">Outro</ion-select-option>
          </ion-select>
        </ion-item>
        <br />
        <ion-item lines="none">
          <ion-input
            :clear-input="true"
            label="Endereço para coleta"
            label-placement="floating"
            placeholder="Informe o endereço completo"
            helper-text="Rua, número, bairro, cidade e CEP"
            fill="solid"
          ></ion-input>
        </ion-item>
        <br />
        <ion-item lines="none">
          <ion-textarea
            :clear-input="true"
            label="Descrição"
            label-placement="floating"
            placeholder="Detalhe o resíduo a ser coletado"
            helper-text="Informe detalhes dos resíduos para facilitar a coleta"
            :auto-grow="true"
            :rows="5"
            :counter="true"
            :maxlength="100"
            fill="solid"
          ></ion-textarea>
        </ion-item>
        <br />
        <ion-item lines="none">
          <ion-input
            :clear-input="true"
            label="Quantidade a ser coletada"
            label-placement="floating"
            placeholder="Quantidade aproximada"
            helper-text="Informe uma estimativa em kg"
            fill="solid"
          ></ion-input>
        </ion-item>
        <br />
        <ion-item lines="none">
          <ion-select
            aria-label="waste-urgency"
            :clear-input="true"
            label="Urgência"
            label-placement="floating"
            fill="solid"
            interface="alert"
          >
            <ion-select-option value="low">Baixa</ion-select-option>
            <ion-select-option value="medium">Média</ion-select-option>
            <ion-select-option value="high">Alta</ion-select-option>
          </ion-select>
        </ion-item>
        <ion-item-divider></ion-item-divider>
        <ion-item lines="none">
          <ion-label>Escolha a data e horário da coleta</ion-label>
        </ion-item>
        <ion-item>
          <ion-datetime-button datetime="datetime">
          >
          </ion-datetime-button>
          <ion-modal :keep-contents-mounted="true" >
            <ion-datetime id="datetime" presentation="date-time" :format-options="formatOptions"></ion-datetime>
          </ion-modal>
        </ion-item>
      </ion-list>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonInput,
  IonTextarea,
  IonIcon,
  IonDatetimeButton,
  IonDatetime,
  IonModal,
  IonItemDivider,
} from "@ionic/vue";
import { helpOutline } from "ionicons/icons";

const formatOptions = {
  date: {
    weekday: 'short',
    month: 'short',
    day: '2-digit',
  },
  time: {
    hour: '2-digit',
    minute: '2-digit',
    hour12: false,
  },
}
</script>

<style scoped>

ion-list {
  width: auto;
}

.title {
  font-size: 18px;
  margin: 20px 0 0 20px;
}

.intro-text {
  display: block;
  padding: 12px 50px;
  text-align: justify;
  hyphens: auto;
  margin-top: 20px;
  color: var(--color-light-gray);
}

ion-modal {
  --border-radius: 15px;
}

ion-label {
  color: var(--color-light-gray);
}
</style>

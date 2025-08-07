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
      <div
        class="main-paper-container"
        :class="{ 'is-hidden': props.title !== 'Papéis' }"
      >
        <div class="container">
          <ion-icon :icon="helpOutline"></ion-icon>
          <h5>O que pode ser reciclado?</h5>
        </div>
        <p>
          Papéis são materiais <b>recicláveis</b>, ou seja, podem ser
          transformados em novos produtos. É importante realizar a
          <b>coleta seletiva</b> dos papéis limpos e secos, evitando misturá-los
          com outros resíduos.
        </p>
        <p>
          Papéis sujos com outros resíduos, engordurados, papel higiênico,
          papéis plastificados não serão reciclados, portanto, devem ser
          descartados no lixo comum.
        </p>

        <div class="container">
          <ion-icon :icon="trashBinOutline"></ion-icon>
          <h5>Como descartar?</h5>
        </div>
        <p>
          Antes de descartar, remova grampos, fitas adesivas, plásticos,
          materiais metálicos ou qualquer outro resíduo presente. Desmonte
          caixas e amasse os papéis volumosos para ajudar a otimizar o espaço
          dos caminhões de coleta. Separe um local adequado e seco e mantenha os
          resíduos descartados separados dos demais.
        </p>

        <div class="container">
          <ion-icon :icon="leafOutline"></ion-icon>
          <h5>Reutilização</h5>
        </div>
        <p>
          Antes de descartar, avalie se o papel pode ser <b>reutilizados.</b>
          Folhas usadas apenas de um lado ainda servem para anotações ou
          rascunhos. Caixas de papelão, como de calçados e outros produtos,
          podem ser reutilizadas para armazenamento ou organização de objetos.
        </p>

        <div class="container">
          <ion-icon :icon="locationOutline"></ion-icon>
          <h5>Destinação Correta</h5>
        </div>
        <p>
          Papéis recicláveis devem ser colocados na lixeira correta da coleta
          seletiva, representada pela cor <b>azul</b>. Caso não exista uma
          lixeira perto de sua residência, disponha o material a ser descartado
          nos pontos de coleta de sua rua.
        </p>
        <!-- <div class="container-button">
          <ion-button @click="closeModal" class="close-button" expand="full">
            Fechar
          </ion-button>
        </div> -->
      </div>

      <div
        class="main-container-metal"
        :class="{ 'is-hidden': props.title !== 'Metais' }"
      >
        <div class="container">
          <ion-icon :icon="trashBinOutline"></ion-icon>
          <h5>Como descartar?</h5>
        </div>
        <p>
          Antes de descartar latas de alimentos, bebidas, aerossóis ou
          conservas, garanta que estejam completamente vazias para evitar
          vazamentos e mau cheiro.
        </p>

        <div class="container">
          <ion-icon :icon="buildOutline"></ion-icon>
          <h5>Preparação básica</h5>
        </div>
        <p>
          Enxágue latas de bebidas e de alimentos com água limpas para remover
          restos de produtos. Isso evita a proliferação de insetos e melhora a
          qualidade do material reciclado.
        </p>
        <p>
          Remova rótulos plásticos, etiquetas e separe tampas. O plástico e
          papel podem ser encaminhados para reciclagem separadamente. Latas de
          alumínio podem ser facilmente amassadas para reduzir o volume do lixo
          descartado.
        </p>

        <div class="container">
          <ion-icon :icon="alertCircleOutline"></ion-icon>
          <h5>Cuidados Especiais</h5>
        </div>
        <p>
          Sprays, aerossóis, latas de tinta ou solventes podem conter resíduos
          tóxicos. Mesmo tendo consciência de que estão vazios, mantenha esse
          tipo de resíduos fora do alcance de crianças e animais. Nunca amasse
          ou perfure latas de aerossóis, pois isso pode causar liberação de
          gases ou até explosões.
        </p>
        <p>
          Maneje com cuidado, parafusos, pregos, agulhas ou outros objetos
          metálicos pontiagudos. Deve-se ter cautela extra caso os mesmo estejam
          enferrujados ou danificados.
        </p>
      </div>
    </ion-content>
  </ion-modal>
</template>

<script setup lang="ts">
// TODO: Mudar o texto de acordo com o card

// TODO: talvez mudar o layout para tipo grid quando for resolução tablet
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
import { helpOutline } from "ionicons/icons";
import { trashBinOutline } from "ionicons/icons";
import { leafOutline } from "ionicons/icons";
import { locationOutline } from "ionicons/icons";
import { alertCircleOutline } from "ionicons/icons";
import { buildOutline } from "ionicons/icons";

const props = defineProps({
  isOpen: {
    type: Boolean,
    required: false,
  },
  title: {
    type: String,
    required: true,
  },
});

console.log(props.title);

const emit = defineEmits(["dismiss"]);

const closeModal = () => {
  emit("dismiss");
};
</script>

<style scoped>
.close-button {
  font-family: "Inter", sans-serif;
}

p {
  color: #5a5a5a;
  font-size: 1rem;
}

.container-button {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.container {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.container ion-icon {
  font-size: 2rem;
  margin-top: 0.3rem;
}

.is-hidden {
  display: none;
}
</style>

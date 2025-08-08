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
      <div :class="{ 'is-hidden': props.id !== 1 }">
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
          guardanapos não serão reciclados, portanto, devem ser descartados no
          lixo comum.
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
          <ion-icon :icon="trashBinOutline"></ion-icon>
          <h5>Descarte</h5>
        </div>
        <p>
          Antes de descartar, remova grampos, fitas adesivas, plásticos,
          materiais metálicos ou qualquer outro resíduo presente. Desmonte
          caixas e amasse os papéis volumosos para ajudar a otimizar o espaço
          dos caminhões de coleta. Separe um local adequado e seco e mantenha os
          resíduos descartados separados dos demais. Remova restos de comida e
          limpe antes do descarte.
        </p>

        <div class="container">
          <ion-icon :icon="locationOutline"></ion-icon>
          <h5>Destinação</h5>
        </div>
        <p>
          Papéis devem ser colocados na lixeira correta da coleta seletiva,
          representada pela cor <b>azul</b>. Caso não exista uma lixeira perto
          de sua residência, disponha o material a ser descartado nos pontos de
          coleta do seu bairro.
        </p>
        <!-- <div class="container-button">
          <ion-button @click="closeModal" class="close-button" expand="full">
            Fechar
          </ion-button>
        </div> -->
      </div>

      <div :class="{ 'is-hidden': props.id !== 2 }">
        <div class="container">
          <ion-icon :icon="helpOutline"></ion-icon>
          <h5>O que pode ser reciclado?</h5>
        </div>
        <p>
          Existem muitos resíduos metálicos recicláveis, os principáis são
          <b>alumínio, ferro, aço e cobre</b>. Objetos como latas, embalagens,
          arames, fios de cobre, panelas sem cabo, entrem muitos outros são
          exemplos que podem ser encaminhados para coleta seletiva.
        </p>
        <div class="container">
          <ion-icon :icon="buildOutline"></ion-icon>
          <h5>Preparação</h5>
        </div>
        <p>
          Enxágue latas de bebidas e de alimentos com água limpas para remover
          restos de produtos. Isso evita a proliferação de bixos e permite que o
          resíduo seja considerado reciclável. Após feita limpeza mantenha os
          resíduos em locais secos, para evitar corrosão.
        </p>
        <p>
          Remova rótulos plásticos, etiquetas e separe tampas. O plástico e
          papel podem ser encaminhados para reciclagem separadamente. Latas de
          alumínio podem ser facilmente amassadas para reduzir o volume do lixo
          descartado.
        </p>

        <div class="container">
          <ion-icon :icon="alertCircleOutline"></ion-icon>
          <h5>Cuidados especiais</h5>
        </div>
        <p>
          Sprays, aerossóis, latas de tinta ou solventes podem conter
          <b>resíduos tóxicos</b>. Mesmo tendo consciência de que estão vazios,
          mantenha esses tipos de resíduos fora do alcance de crianças e
          animais. Nunca amasse ou perfure latas de aerossóis, pois isso pode
          causar liberação de gases ou até explosões.
        </p>
        <p>
          Maneje com cuidado, parafusos, pregos, agulhas, lâminas ou outros
          objetos metálicos perfurantes. Deve-se ter cautela extra caso os mesmo
          estejam enferrujados ou danificados, sendo recomendado o uso de
          <b>EPIs</b> como luvas e botas.
        </p>

        <div class="container">
          <ion-icon :icon="trashBinOutline"></ion-icon>
          <h5>Descarte</h5>
        </div>
        <p>
          Antes de descartar latas de alimentos, bebidas, aerossóis ou
          conservas, garanta que estejam <b>completamente vazias</b> para evitar
          vazamentos e mau cheiro. Procure envolver objetos cortantes e
          pontiagudos em mais de um saco ou sacola, garantindo maior segurança
          para catadores. Evite descartar resíduos metálicos com outros tipos de
          resíduos, portanto, disponha-os na lixeira correta representada pela
          cor <b>amarela</b>.
        </p>

        <div class="container">
          <ion-icon :icon="locationOutline"></ion-icon>
          <h5>Destinação</h5>
        </div>
        <p>
          Metais devem ser colocados na lixeira correta da coleta seletiva,
          representada pela cor <b>amarela</b>. Caso não encontre uma lixeira
          perto de sua residência, disponha o material a ser descartado nos
          pontos de coleta da sua rua.
        </p>
      </div>

      <div :class="{ 'is-hidden': props.id !== 3 }">
        <div class="container">
          <ion-icon :icon="buildOutline"></ion-icon>
          <h5>Preparação</h5>
        </div>
        <p>
          Plásticos são materiais recicláveis identificados pelos símbolos
          numerados (1 a 7) geralmente encontrados no fundo das embalagens. PET,
          PEAD, PVC e PP são os mais comuns e recicláveis.
        </p>
        <p>
          Lave embalagens plásticas com água para remover restos de alimentos,
          gordura ou produtos. Não é necessário usar detergente - apenas água é
          suficiente.
        </p>
        <p>
          Retire rótulos de papel, etiquetas adesivas e tampas de outros
          materiais quando possível. Tampas que não forem plásticas devem ser
          separadas.
        </p>

        <div class="container">
          <ion-icon :icon="colorWandOutline"></ion-icon>
          <h5>Sustentabilidade</h5>
        </div>
        <p></p>
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
import { colorWandOutline } from "ionicons/icons";

const props = defineProps({
  isOpen: {
    type: Boolean,
    required: true,
  },
  title: {
    type: String,
    required: true,
  },
  id: {
    type: Number,
    required: true,
  },
});

const emit = defineEmits(["dismiss"]);

const closeModal = () => {
  emit("dismiss");
};
</script>

<style scoped>
/* .close-button {
  font-family: "Inter", sans-serif;
} */

p {
  color: #5a5a5a;
  font-size: 1rem;
  text-align: justify;
}

/* .container-button {
  display: flex;
  justify-content: center;
  margin-top: 20px;
} */

.container {
  display: flex;
  align-items: center;
  gap: 1rem;
  /* color: #2d6b2b; */
}

.container ion-icon {
  font-size: 2rem;
  margin-top: 0.3rem;
  /* color: #42993f; */
}

.is-hidden {
  display: none;
}
</style>

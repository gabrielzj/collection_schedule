<template>
  <ion-modal :is-open="isOpen" @didDismiss="closeModal">
    <ion-page>
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
        <template v-if="isOpen">
          <!-- PAPEL -->
          <div v-if="props.id === 1">
            <div class="container">
              <ion-icon :icon="helpOutline"></ion-icon>
              <h5>Sobre</h5>
            </div>
            <p>
              Papéis são materiais <b>recicláveis</b>, ou seja, podem ser
              transformados em novos produtos. É importante realizar a
              <b>coleta seletiva</b> dos papéis limpos e secos, evitando
              misturá-los com outros resíduos.
            </p>
            <p>
              Papéis sujos com outros resíduos, engordurados, papel higiênico,
              guardanapos não serão reciclados, portanto, devem ser descartados
              no lixo comum.
            </p>

            <div class="container">
              <ion-icon :icon="leafOutline"></ion-icon>
              <h5>Reutilização</h5>
            </div>
            <p>
              Antes de descartar, avalie se o papel pode ser
              <b>reutilizados.</b>
              Folhas usadas apenas de um lado ainda servem para anotações ou
              rascunhos. Caixas de papelão, como de calçados e outros produtos,
              podem ser reutilizadas para armazenamento ou organização de
              objetos.
            </p>

            <div class="container">
              <ion-icon :icon="trashBinOutline"></ion-icon>
              <h5>Descarte</h5>
            </div>
            <p>
              Antes de descartar, remova grampos, fitas adesivas, plásticos,
              materiais metálicos ou qualquer outro resíduo presente. Desmonte
              caixas e amasse os papéis volumosos para ajudar a otimizar o
              espaço dos caminhões de coleta. Separe um local adequado e seco e
              mantenha os resíduos descartados separados dos demais. Remova
              restos de comida e limpe antes do descarte.
            </p>

            <div class="container">
              <ion-icon :icon="locationOutline"></ion-icon>
              <h5>Destino</h5>
            </div>
            <ul>
              <li>
                Lixeiras da coleta seletiva, representadas pela cor <b>azul</b>.
              </li>
              <li>
                Locais de coleta do bairro/rua, ou PEVs (Pontos de entrega
                voluntária).
              </li>
            </ul>
          </div>

          <!-- METAL -->
          <div v-else-if="props.id === 2">
            <div class="container">
              <ion-icon :icon="helpOutline"></ion-icon>
              <h5>Sobre</h5>
            </div>
            <p>
              Existem muitos resíduos metálicos recicláveis, os principais são
              <b>alumínio, ferro, aço e cobre</b>. Objetos como latas,
              embalagens, arames, fios de cobre, panelas sem cabo, entrem muitos
              outros são exemplos que podem ser encaminhados para coleta
              seletiva.
            </p>
            <div class="container">
              <ion-icon :icon="buildOutline"></ion-icon>
              <h5>Preparação</h5>
            </div>
            <p>
              Enxágue latas de bebidas e de alimentos com água limpas para
              remover restos de produtos. Isso evita a proliferação de bichos e
              permite que o resíduo seja considerado reciclável. Após feita
              limpeza mantenha os resíduos em locais secos, para evitar
              corrosão.
            </p>
            <p>
              Remova rótulos plásticos, etiquetas e separe tampas. O plástico e
              papel podem ser encaminhados para reciclagem separadamente. Latas
              de alumínio podem ser facilmente amassadas para reduzir o volume
              do lixo descartado.
            </p>

            <div class="container">
              <ion-icon :icon="alertCircleOutline"></ion-icon>
              <h5>Cuidados</h5>
            </div>
            <p>
              Sprays, aerossóis, latas de tinta ou solventes podem conter
              <b>resíduos tóxicos</b>. Mesmo tendo consciência de que estão
              vazios, mantenha esses tipos de resíduos fora do alcance de
              crianças e animais. Nunca amasse ou perfure latas de aerossóis,
              pois isso pode causar liberação de gases ou até explosões.
            </p>
            <p>
              Maneje com cuidado, parafusos, pregos, agulhas, lâminas ou outros
              objetos metálicos perfurantes. Deve-se ter cautela extra caso os
              mesmo estejam enferrujados ou danificados, sendo recomendado o uso
              de
              <b>EPIs</b> como luvas e botas.
            </p>

            <div class="container">
              <ion-icon :icon="trashBinOutline"></ion-icon>
              <h5>Descarte</h5>
            </div>
            <p>
              Antes de descartar latas de alimentos, bebidas, aerossóis ou
              conservas, garanta que estejam <b>completamente vazias</b> para
              evitar vazamentos e mau cheiro. Procure envolver objetos cortantes
              e pontiagudos em mais de um saco ou sacola, garantindo maior
              segurança para catadores. Evite descartar resíduos metálicos com
              outros tipos de resíduos.
            </p>

            <div class="container">
              <ion-icon :icon="locationOutline"></ion-icon>
              <h5>Destino</h5>
            </div>
            <p>
              Metais devem ser colocados na lixeira correta da coleta seletiva,
              representada pela cor <b>amarela</b>. Caso não encontre uma
              lixeira perto de sua residência, disponha o material a ser
              descartado nos pontos de coleta da sua rua ou
              <b>Pontos de entrega voluntária (PEVs)</b>.
            </p>
          </div>

          <!-- PLÁSTICO -->
          <div v-else-if="props.id === 3">
            <div class="container">
              <ion-icon :icon="helpOutline"></ion-icon>
              <h5>Sobre</h5>
            </div>
            <p>
              Plásticos são materiais recicláveis identificados pelos símbolos
              numerados (1 a 7) geralmente encontrados no fundo das embalagens.
              PET, PEAD, PVC e PP são os mais comuns.
            </p>

            <div class="container">
              <ion-icon :icon="buildOutline"></ion-icon>
              <h5>Preparação</h5>
            </div>
            <p>
              Lave embalagens plásticas com água para remover restos de
              alimentos, gordura ou produtos.
            </p>
            <p>
              Retire rótulos de papel, etiquetas adesivas e tampas de outros
              materiais quando possível. Tampas que não forem plásticas devem
              ser separadas.
            </p>

            <div class="container">
              <ion-icon :icon="earthOutline"></ion-icon>
              <h5>Sustentabilidade</h5>
            </div>
            <p>
              A reciclagem de plásticos reduz a quantidade de resíduos enviados
              para aterros e ajuda a economizar recursos naturais, como petróleo
              e energia, utilizados na produção de novos plásticos. O
              reaproveitamento desses materiais também diminui a poluição de
              rios e oceanos, prevenindo impactos na fauna e flora.
            </p>
            <p>
              Sempre que possível, prefira produtos feitos com
              <b>plástico reciclado</b> ou <b>embalagens retornáveis</b>,
              contribuindo para um ciclo de consumo mais sustentável.
            </p>
            <ul>
              <li>Substitua sacolas plásticas por reutilizáveis.</li>
              <li>Use embalagens retornáveis ou biodegradáveis.</li>
              <li>Reutilize potes e garrafas sempre que possível.</li>
              <li>
                Sempre que possível opte por produtos com selos ambientais.
              </li>
            </ul>

            <div class="container">
              <ion-icon :icon="alertCircleOutline"></ion-icon>
              <h5>Cuidados</h5>
            </div>
            <ul>
              <li>Não exponha os resíduos ao fogo ou calor extremo.</li>
              <li>
                Evite reutilização excessiva, garrafas por exemplo, podem
                acumular bactérias.
              </li>
              <li>Junte várias sacolas em uma só antes de descartar</li>
            </ul>

            <div class="container">
              <ion-icon :icon="locationOutline"></ion-icon>
              <h5>Destino</h5>
            </div>
            <ul>
              <li>
                Lixeiras da coleta seletiva, representadas pela cor
                <b>vermelha</b>.
              </li>
              <li>
                Locais de coleta do bairro/rua, ou
                <b>PEVs (Pontos de entrega voluntária).</b>
              </li>
            </ul>
          </div>

          <!-- ELETRÔNICOS -->
          <div v-else-if="props.id === 4">
            <div class="container">
              <ion-icon :icon="buildOutline"></ion-icon>
              <h5>Preparação</h5>
            </div>
            <p>
              Os dispositivos eletrônicos apresentam um processo diferente de
              descarte e reaproveitamento, portanto é importante considerar
              <b>mantê-los.</b>
              aqueles que ainda estejam em funcionamento. Se possível, considere
              doar o equipamento ao descartá-lo.
            </p>
            <p>
              É importante verificar quaisquer informações pessoais ainda
              presentes em computadores e celulares por exemplo. Antes do
              descarte, anote marcas, modelos e números de série.
            </p>
            <p>
              Com informações em mãos, verifique com fabricante a respeito de
              possíveis <b>garantias</b> ainda vigentes do produto.
            </p>

            <div class="container">
              <ion-icon :icon="cubeOutline"></ion-icon>
              <h5>Programas de Logística Reversa</h5>
            </div>
            <p>
              Processo que envolvem coleta, transporte, tratamento, Destino dos
              equipamento eletrônicos prevista na Lei 12.305/2010. que obriga
              fabricantes, importadores, distribuidores e comerciantes a
              estruturar e implementar sistemas para a devolução e destinação
              adequada de produtos e embalagens após o uso pelo consumidor.
              Exemplos são:
            </p>

            <ul>
              <!-- <li>
                <b>Reciclanip:</b> logística reversa de pneus, parceria com
                Bridgestone, Pirelli entre outras empresas.
              </li> -->
              <li>
                <b>Samsung Re+:</b> logística reversa de produtos da Samsung.
              </li>
              <li>
                <b>Vivo Recicle:</b> logística reversa de produtos da Vivo
              </li>
              <li>
                <b>Green Eletron:</b> entidade de logística reversa sem fins
                lucrativos presentes em diversas cidades
              </li>
            </ul>

            <div class="container">
              <ion-icon :icon="alertCircleOutline"></ion-icon>
              <h5>Cuidados</h5>
            </div>
            <p>
              Separe equipamentos com <b>vazamentos de baterias</b>,
              <b>odores químicos</b>, <b>partes trincados</b>,
              <b>superaquecimento.</b>
            </p>
            <p>
              Procure separar cabos, pilhas, baterias, adaptadores, entre outros
              acessórios, facilitando o processo de descarte.
            </p>

            <div class="container">
              <ion-icon :icon="locationOutline"></ion-icon>
              <h5>Destino</h5>
            </div>
            <p>
              Os resíduos podem ser descartados em pontos de coleta de aparelhos
              eletrônicos disponibilizados por grandes lojas do varejo e centros
              comerciais. Também procure por pontos de coleta especializada
              municipais
            </p>
          </div>

          <!-- ORGÂNICOS -->
          <div v-else-if="props.id === 5">
            <div class="container">
              <ion-icon :icon="helpOutline"></ion-icon>
              <h5>Sobre</h5>
            </div>
            <p>
              Resíduos orgânicos são restos de alimentos e materiais de origem
              biológica que se decompõem naturalmente. A separação correta reduz
              odores, evita atração de pragas e permite a compostagem, gerando
              adubo para o solo.
            </p>

            <div class="container">
              <ion-icon :icon="buildOutline"></ion-icon>
              <h5>Preparação</h5>
            </div>
            <ul>
              <li>
                Prefira lixeiras com tampa e, se possível, use sacos
                biodegradáveis.
              </li>
              <li>
                Mantenha em local ventilado e esvazie com frequência
                (diariamente ou conforme a coleta).
              </li>
              <li>
                Evite líquidos em excesso: escorra caldos e sucos para reduzir
                <b>chorume</b>.
              </li>
              <li>
                Remova embalagens, elásticos, plásticos e metais antes de
                descartar.
              </li>
              <li>
                Feche bem o saco/recipiente para evitar vazamentos e atração de
                insetos.
              </li>
              <li>
                Envolva os resíduos em saco adicional se necessário, evitando
                vazamento.
              </li>
            </ul>

            <div class="container">
              <ion-icon :icon="alertCircleOutline"></ion-icon>
              <h5>Cuidados</h5>
            </div>
            <ul>
              <li>
                Manusei com cuidado grandes quantidades de resíduos, pois podem
                conter moscas, vermes e outras pragas.
              </li>
              <li>
                Fezes de animais carnívoros, carvão/cinzas tratadas, devem ser
                dispostos de forma separada.
              </li>
            </ul>

            <div class="container">
              <ion-icon :icon="locationOutline"></ion-icon>
              <h5>Destino</h5>
            </div>
            <ul>
              <li><b>Compostagem doméstica</b> para gerar adubo.</li>
              <li>
                Lixeiras da coleta seletiva, representadas pela cor
                <b>marrom</b>.
              </li>
              <li>
                <b>Pátios de compostagem/Pontos de entrega voluntária (PEVs)</b>
                ou ecopontos que recebam resíduos orgânicos.
              </li>
            </ul>
            <div class="container">
              <ion-icon :icon="bulbOutline"></ion-icon>
              <h5>Dicas</h5>
            </div>
            <ul>
              <li>
                Higienize a lixeira com água e sabão e desinfete periodicamente.
              </li>
              <li>
                Evite superlotar o saco: pesos altos causam rasgos e vazamentos.
              </li>
            </ul>
          </div>

          <!-- VIDRO -->
          <div v-else-if="props.id === 6">
            <div class="container">
              <ion-icon :icon="helpOutline"></ion-icon>
              <h5>Sobre</h5>
            </div>
            <p>
              Vidro é material inorgânico, sustentável e 100% reciclável sem
              perda significativa de qualidade. A reciclagem reduz extração de
              matéria-prima e consumo de energia. Vidros limpos e separados têm
              maior chance de serem reaproveitados pela cadeia de reciclagem.
            </p>

            <div class="container">
              <ion-icon :icon="buildOutline"></ion-icon>
              <h5>Preparação</h5>
            </div>
            <ul>
              <li>
                Mantenha garrafas, potes, refratários, pratos entre outos
                objetos a serem descartados separados de outros tipos de
                resíduos
              </li>
              <li>
                Separe vidros quebrados em embalagem protegida (papelão ou
                jornal), e armazene em caixas rígidas ou envolva em mais de um
                saco de lixo. Se possível identifique naa caixa ou saco a
                presença de vidro quebrado.
              </li>
              <li>
                Enxágue garrafas e frascos para remover resíduos orgânicos.
              </li>
              <li>
                Remova tampas e rolhas quando possível — metais e plásticos vão
                para outras correntes.
              </li>
            </ul>

            <div class="container">
              <ion-icon :icon="alertCircleOutline"></ion-icon>
              <h5>Cuidados</h5>
            </div>
            <ul>
              <li>
                Lâmpadas (fluorescentes, LED com componentes), espelhos,
                cerâmica, porcelana e vidro temperado exigem destinação
                específica.
              </li>
              <li>
                Vidros com contaminação perigosa (resíduos químicos, solventes,
                tintas) devem ser levados a PEV/centro de descarte.
              </li>
              <li>
                Objectos de cristal (alto teor de chumbo) — verificar locais
                especializados.
              </li>
              <li>
                Atente-se para vidros especiais, pois nem todos são recicláveis
                como o vidro comum. Vidros
                <b>temperados, laminados, blindados e espelhados</b>
                devem permanecer separados do vidro comum e é recomendado
                contatar empresas especializadas para que possam fazer o
                descarte e manuseio do vidro de forma segura.
              </li>
            </ul>

            <div class="container">
              <ion-icon :icon="locationOutline"></ion-icon>
              <h5>Destino</h5>
            </div>
            <ul>
              <li>
                Lixeiras da coleta seletiva, identificadas pela cor
                <b>verde</b>.
              </li>
              <li>
                Ecopontos e Pontos de Entrega Voluntária (PEV) para grandes
                volumes ou itens especiais.
              </li>
              <li>
                Lojas e programas de logística reversa que aceitam embalagens
                retornáveis.
              </li>
            </ul>
          </div>

          <!-- REJEITOS -->
          <div v-else-if="props.id === 7">
            <div class="container">
              <ion-icon :icon="helpOutline"></ion-icon>
              <h5>Sobre</h5>
            </div>
            <p>
              De acordo com a Política Nacional de Resíduos Sólidos (PNRS),
              rejeitos são aqueles que, após esgotadas as possibilidades de
              reutilização, reciclagem ou compostagem, não possuem viabilidade
              para aproveitamento. Geralmente são encaminhados para aterros
              sanitários, onde recebem tratamento adequado para minimizar
              impactos ambientais.
            </p>

            <p>São exemplos de rejeitos:</p>
            <ul>
              <li>Fraldas descartáveis;</li>
              <li>Absorventes;</li>
              <li>Cotonetes;</li>
              <li>Bitucas de cigarro;</li>
              <li>Isopor sujo com alimentos;</li>
              <li>Poeira, cabelos e sujeiras em geral;</li>
              <li>Detritos de construção e demolição.</li>
            </ul>

            <div class="container">
              <ion-icon :icon="buildOutline"></ion-icon>
              <h5>Preparação</h5>
            </div>
            <p>
              No descarte, utilize sacos de lixo, preferencialmente, de cor
              diferenciada e, caso necessário, envolva em mais de um saco. Evite
              misturar sacos de rejeitos com outros tipos de resíduos. Manusear
              com luvas para evitar contaminação. Evite misturar com outros
              tipos de resíduos.
            </p>
            <div class="container">
              <ion-icon :icon="locationOutline"></ion-icon>
              <h5>Destino</h5>
            </div>
            <p>
              Grande parte dos rejeitos são destinados à
              <b>aterros sanitários</b>. Outros tipos de rejeitos podem ser
              incinerados, servindo como combustível para geração de energia.
            </p>
            <p>
              Verifique os pontos de coleta de sua rua/bairro ou procure
              <b>por pontos de entrega voluntária (PEVS)</b>. Confira se seu
              município possui programas especiais de recolhimento desse tipo de
              resíduos.
            </p>
          </div>

          <!-- OUTROS -->
          <div v-else-if="props.id === 8">
            <div class="container">
              <ion-icon :icon="helpOutline"></ion-icon>
              <h5>Sobre</h5>
            </div>
            <p>
              São resíduos que requerem descarte diferenciado dos demais.
              Exemplos:
            </p>
            <ul>
              <li>Resíduos perigosos, como mercúrio;</li>
              <li>Embalagens de agrotõxicos e venenos;</li>
              <li>Alguns resíduos eletrônicos, como lâmpadas fluorescentes;</li>
              <li>Resíduos de construção civil;</li>
              <li>Óleo de cozinha;</li>
              <li>Medicamentos vencidos;</li>
              <li>Móveis.</li>
            </ul>
            <div class="container">
              <ion-icon :icon="buildOutline"></ion-icon>
              <h5>Preparação</h5>
            </div>
            <ul>
              <li>Separe e embale os resíduos especiais dos demais;</li>
              <li>
                Use luvas e outros equipamentos de EPIs para manusear químicos e
                outros itens potencialmente danosos;
              </li>
            </ul>
            <div class="container">
              <ion-icon :icon="locationOutline"></ion-icon>
              <h5>Destino</h5>
            </div>
            <p>
              Procure por pontos de coleta especiais em mercados e farmácias.
              Busque por iniciativas como:
            </p>
            <ul>
              <li>
                <a
                  href="https://reciclus.org.br/onde-descartar/?utm_source=google&utm_medium=cpc&utm_campaign=campanha-reciclus-2025&utm_content=746303008043&utm_term=reciclagem%20lampadas&gad_source=1&gad_campaignid=22442806277&gclid=Cj0KCQjw-4XFBhCBARIsAAdNOks-aNRqTWpjjA0CxYDgLS28RI1dW2_eD5dQTcJr-OpWsVyIGZ8kSeQaAhmdEALw_wcB"
                  ><b>Reciclus:</b>
                </a>
                que atua na logistica reversa de lâmpadas fluorescentes.
              </li>
              <li>
                <a href="https://cidadelimpa.tvtem.com/"
                  ><b>Cidade Limpa:</b></a
                >
                iniciativa da TV TEM, afiliada da rede Globo, que promove
                multirões de limpeza por diversas cidades do Brasil.
              </li>
            </ul>
            <p>
              Para mais informações sobre pontos de coleta ou descarte, entre em
              contato com a Secretária do Meio Ambiente ou com a Vigilância
              Sanitária de sua cidade.
            </p>
          </div>
        </template>
      </ion-content>
    </ion-page>
  </ion-modal>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";

import {
  IonModal,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonButton,
  IonButtons,
  IonIcon,
  IonPage,
} from "@ionic/vue";
import {
  closeOutline,
  helpOutline,
  trashBinOutline,
  leafOutline,
  locationOutline,
  alertCircleOutline,
  buildOutline,
  earthOutline,
  bulbOutline,
  cubeOutline,
} from "ionicons/icons";

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
p {
  color: var(--color-light-gray);
  font-size: 1rem;
  text-align: justify;
  hyphens: auto;
}

ul {
  color: var(--color-light-gray);
  font-size: 1rem;
  padding-left: 15px;
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

a {
  text-decoration: none;
  color: inherit;
}
</style>

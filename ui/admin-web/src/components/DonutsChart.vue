<template>
  <div class="chart-card">
    <h3 v-if="title">{{ title }}</h3>
    <apexchart type="pie" width="350" :options="pieOptions" :series="pieSeries" />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';

const props = defineProps<{
  urgencies: string[];
  title?: string;
}>();

// recebe um array de strings e retorna um array de objetos com contagens por valor
// Exemplo de retorno: [ { label: 'high', count: 10 }, { label: 'medium', count: 5 } ]
function countOccurrences(values: string[]) {
  // cria um novo mapa para armazenar as contagens
  const counts = new Map<string, number>();

  if (!Array.isArray(values)) {
    return [];
  }

  for (const raw of values) {
    let v = '';
    if (raw !== null && raw !== undefined) {
      v = String(raw).trim();
    }
    if (!v) {
      continue;
    }
    const prev = counts.get(v);
    if (typeof prev === 'number') {
      counts.set(v, prev + 1);
    } else {
      counts.set(v, 1);
    }
  }
  // converte o mapa em um array de objetos
  const result: Array<{ label: string; count: number }> = [];
  const entries = Array.from(counts.entries());

  for (let i = 0; i < entries.length; i++) {
    const entry = entries[i];
    if (!entry) {
      continue;
    }
    const [label, count] = entry;
    result.push({ label, count });
  }
  return result;
}

const inputUrgencies = computed(() => {
  if (Array.isArray(props.urgencies)) {
    return props.urgencies;
  } else {
    return [] as string[];
  }
});

const urgencyEntries = computed(() => countOccurrences(inputUrgencies.value));

const URGENCY_PT: Record<string, string> = {
  low: 'Baixa',
  medium: 'Moderada',
  high: 'Alta',
};

function toPortuguese(raw: string): string {
  let key: string = '';

  if (typeof raw === 'string') {
    key = raw.trim().toLowerCase();
  }

  const mapped = URGENCY_PT[key];

  if (mapped) {
    return mapped;
  } else {
    if (raw && raw.length > 0) {
      return raw;
    } else {
      return '';
    }
  }
}

// Agregar contagens por rótulo traduzido
const urgencyEntriesPt = computed(() => {
  const agg = new Map<string, number>();
  const entries = urgencyEntries.value;
  for (let i = 0; i < entries.length; i++) {
    const entry = entries[i];
    if (!entry) {
      continue;
    }
    const labelPt = toPortuguese(entry.label);
    const prev = agg.get(labelPt);
    if (typeof prev === 'number') {
      agg.set(labelPt, prev + entry.count);
    } else {
      agg.set(labelPt, entry.count);
    }
  }
  const result: Array<{ label: string; count: number }> = [];
  const iterator = agg.entries();
  const pairs = Array.from(iterator);
  for (let i = 0; i < pairs.length; i++) {
    const pair = pairs[i];
    if (!pair) {
      continue;
    }
    const [label, count] = pair;
    result.push({ label, count });
  }
  return result;
});

const ORDER_PT = ['Baixa', 'Moderada', 'Alta'] as const;

const entriesPtSorted = computed(() => {
  const getOrder = (label: string) => {
    const i = ORDER_PT.indexOf(label as any);
    return i === -1 ? 99 : i;
  };
  return urgencyEntriesPt.value.slice().sort((a, b) => getOrder(a.label) - getOrder(b.label));
});

const pieLabels = computed(() => entriesPtSorted.value.map((e) => e.label));
const pieSeries = computed(() => entriesPtSorted.value.map((e) => e.count));

// mapa fixo de cor por rótulo traduzido
const COLORS_BY_LABEL_PT: Record<string, string> = {
  Baixa: 'rgb(45, 213, 91)',
  Moderada: 'rgb(255, 196, 9)',
  Alta: 'rgb(197, 0, 15)',
};

// gera as cores na mesma ordem dos labels atuais
const pieColors = computed(() => pieLabels.value.map((l) => COLORS_BY_LABEL_PT[l] ?? '#2F7DD1'));

const pieOptions = computed(
  () =>
    ({
      chart: { id: 'calls-by-urgency' },
      labels: pieLabels.value,
      legend: { position: 'top' },
      colors: pieColors.value,
    }) as any,
);
</script>

<style scoped>
.chart-card {
  background: #fff;
  border: 1px solid #e4e8ee;
  border-radius: 14px;
  padding: 1rem;
}
.chart-card h3 {
  margin: 0 0 0.75rem 0;
  font-size: 1rem;
  color: #1d2b39;
}
</style>

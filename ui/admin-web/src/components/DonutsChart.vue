<template>
  <div class="chart-card">
    <h3 v-if="title">{{ title }}</h3>
    <apexchart type="pie" height="400" :options="pieOptions" :series="pieSeries" />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';

const props = defineProps<{
  urgencies: string[];
  title?: string;
}>();

// countOccurrences: conta quantas vezes cada rótulo aparece no array de entrada
function countOccurrences(values: string[]) {
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
  const result: Array<{ label: string; count: number }> = [];
  const entries = Array.from(counts.entries());
  for (let i = 0; i < entries.length; i++) {
    const [label, count] = entries[i];
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

function toPortugueseUrgency(raw: string) {
  let key = '';
  if (typeof raw === 'string') {
    key = raw.trim().toLowerCase();
  }
  const mapped = URGENCY_PT[key];
  if (mapped) {
    return mapped;
  } else {
    if (raw && raw.length > 0) {
      const first = raw.charAt(0).toUpperCase();
      const rest = raw.slice(1);
      return first + rest;
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
    const labelPt = toPortugueseUrgency(entry.label);
    const prev = agg.get(labelPt);
    if (typeof prev === 'number') {
      agg.set(labelPt, prev + entry.count);
    } else {
      agg.set(labelPt, entry.count);
    }
  }
  const result: Array<{ label: string; count: number }> = [];
  const pairs = Array.from(agg.entries());
  for (let i = 0; i < pairs.length; i++) {
    const [label, count] = pairs[i];
    result.push({ label, count });
  }
  return result;
});
const pieLabels = computed(() => urgencyEntriesPt.value.map((e) => e.label));
const pieSeries = computed(() => urgencyEntriesPt.value.map((e) => e.count));

const pieOptions = computed(
  () =>
    ({
      chart: { id: 'calls-by-urgency' },
      labels: pieLabels.value,
      legend: { position: 'top' },
      colors: ['rgb(45, 213, 91)', 'rgb(255, 196, 9)', 'rgb(197, 0, 15)', '#2F7DD1', '#15AABF'],
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

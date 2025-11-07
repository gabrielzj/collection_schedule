<template>
  <div class="chart-card">
    <h3 v-if="title">{{ title }}</h3>
    <apexchart type="bar" height="400" :options="barOptions" :series="barSeries" />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';

const props = defineProps<{
  types: string[];
  title?: string;
}>();

// countOccurrences: conta quantas vezes cada rótulo aparece no array de entrada
// Ex.: ["papel", "metal", "metal"] => [ { label: "papel", count: 1 }, { label: "metal", count: 2 } ]
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

const inputTypes = computed(() => {
  if (Array.isArray(props.types)) {
    return props.types;
  } else {
    return [] as string[];
  }
});

const typeCounts = computed(() => countOccurrences(inputTypes.value));

const TYPE_PT: Record<string, string> = {
  paper: 'Papel',
  plastic: 'Plástico',
  glass: 'Vidro',
  metal: 'Metal',
  organic: 'Orgânico',
  electronics: 'Eletrônicos',
  'e-waste': 'Eletrônicos',
  electronic: 'Eletrônicos',
  other: 'Outros',
};

function toPortugueseType(raw: string) {
  let key = '';
  if (typeof raw === 'string') {
    key = raw.trim().toLowerCase();
  }
  const mapped = TYPE_PT[key];
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

const typeCountsPt = computed(() => {
  const agg = new Map<string, number>();
  const entries = typeCounts.value;
  for (let i = 0; i < entries.length; i++) {
    const entry = entries[i];
    const labelPt = toPortugueseType(entry.label);
    const prev = agg.get(labelPt);
    if (typeof prev === 'number') {
      agg.set(labelPt, prev + entry.count);
    } else {
      agg.set(labelPt, entry.count);
    }
  }
  const result: Array<{ label: string; count: number }> = [];
  const aggEntries = Array.from(agg.entries());
  for (let i = 0; i < aggEntries.length; i++) {
    const [label, count] = aggEntries[i];
    result.push({ label, count });
  }
  return result;
});
const barCategories = computed(() => typeCountsPt.value.map((e) => e.label));
const seriesData = computed(() => typeCountsPt.value.map((e) => e.count));
const maxCount = computed(() => {
  if (seriesData.value.length > 0) {
    return Math.max(...seriesData.value);
  } else {
    return 0;
  }
});
const tickAmount = computed(() => Math.max(1, maxCount.value));
const barSeries = computed(() => [
  {
    name: 'Chamados',
    data: seriesData.value,
  },
]);

const barOptions = computed(
  () =>
    ({
      chart: { id: 'calls-by-type', toolbar: { show: false } },
      xaxis: {
        categories: barCategories.value,
        min: 0,
        max: tickAmount.value,
        tickAmount: tickAmount.value,
        decimalsInFloat: 0,
        labels: {
          formatter: (val: number) => Math.round(val).toString(),
        },
      },
      dataLabels: {
        enabled: false,
      },
      plotOptions: {
        bar: {
          borderRadius: 6,
          horizontal: true,
          barHeight: '70%',
        },
      },
      tooltip: {
        y: {
          formatter: (val: number) => Math.round(val).toString(),
        },
      },
      colors: ['#2f7dd1'],
      grid: { strokeDashArray: 4 },
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

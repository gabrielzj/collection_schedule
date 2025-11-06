<template>
  <div class="chart-card">
    <h3>{{ title || 'Total de Resíduos' }}</h3>
    <apexchart type="radialBar" :options="options" :series="series" height="280" />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';

const props = defineProps<{
  total: number;
  target?: number;
  title?: string;
}>();

const percent = computed(() => {
  if (typeof props.target === 'number' && props.target > 0) {
    const raw = (props.total / props.target) * 100;
    if (raw < 0) {
      return 0;
    } else if (raw > 100) {
      return 100;
    } else {
      return Math.round(raw);
    }
  } else {
    return 100;
  }
});

const series = computed(() => {
  const arr: number[] = [];
  arr.push(percent.value);
  return arr;
});

const options = computed(() => {
  let totalValue = 0;
  if (Number.isFinite(props.total)) {
    totalValue = Math.trunc(props.total);
  }
  const goal =
    typeof props.target === 'number' && props.target > 0 ? Math.trunc(props.target) : undefined;
  const goalText = goal ? ` / ${goal.toLocaleString('pt-BR')} kg` : '';

  return {
    chart: { sparkline: { enabled: true } },
    colors: ['#2F7DD1'],
    stroke: { lineCap: 'round' },
    plotOptions: {
      radialBar: {
        hollow: { size: '62%' },
        track: { background: '#eef3f7' },
        dataLabels: {
          name: { show: true, offsetY: 12, color: '#5a6570', fontSize: '12px' },
          value: {
            show: true,
            fontSize: '22px',
            color: '#1d2b39',
            formatter: (val: any) => `${Math.round(Number(val) || 0)}%`,
          },
          total: {
            show: true,
            label: 'Total',
            formatter: () => `${totalValue.toLocaleString('pt-BR')} kg${goalText}`,
          },
        },
      },
    },
    labels: ['Progresso'],
  };
});
</script>

<style scoped>
.chart-card {
  background: #fff;
  border: 1px solid #e4e8ee;
  border-radius: 14px;
  padding: 1rem;
}
.chart-card h3 {
  margin: 0 0 0.5rem 0;
  font-size: 1rem;
  color: #1d2b39;
}
</style>

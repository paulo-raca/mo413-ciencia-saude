<script setup>
import { onMounted, ref } from 'vue'
import Highcharts from 'highcharts'
import 'highcharts/highcharts-more'

const chart = ref(null)

// Fonte: project3-final/data/processed/multiseed_20260531_202951/stability.json

// Acurácia — 5 valores reais por seed
const accValues = [0.7162, 0.7568, 0.7432, 0.8514, 0.8514]
const accBox = boxFromValues(accValues)

// F1 por classe — stability.json só guarda mean/std agregados (per-seed
// não foram persistidos). Valores abaixo medidos por pixel a partir do
// gráfico original (PDF página 16); batem com agg (mean ± σ):
//   Tumor Primário: 0.40 ± 0.22 · Metástase: 0.87 ± 0.04 · Nevo: 0.57 ± 0.12
const f1Values = {
  'Tumor Primário': [0.000, 0.370, 0.414, 0.589, 0.620],
  Metástase: [0.821, 0.844, 0.844, 0.921, 0.923],
  'Nevo Benigno': [0.400, 0.448, 0.667, 0.667, 0.667],
}

function clamp(x, lo = 0, hi = 1) {
  return Math.max(lo, Math.min(hi, x))
}

// boxplot quartis a partir dos 5 valores: [min, Q1, mediana, Q3, max]
function boxFromValues(values) {
  const s = [...values].sort((a, b) => a - b)
  return [s[0], s[1], s[2], s[3], s[4]]
}

// PRNG determinístico só para jitter horizontal (não afeta valores)
function mulberry32(seed) {
  return function () {
    seed = (seed + 0x6d2b79f5) | 0
    let t = seed
    t = Math.imul(t ^ (t >>> 15), t | 1)
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61)
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
}
const rng = mulberry32(42)

function jitter(x, amount = 0.29) {
  return x + (rng() - 0.5) * amount
}

const categories = ['Acurácia', ...Object.keys(f1Values)]

onMounted(() => {
  // Boxes derivados dos 5 valores: min, p25, p50, p75, max
  const f1Boxes = Object.values(f1Values).map((values, i) => {
    const box = boxFromValues(values)
    return { x: i + 1, low: box[0], q1: box[1], median: box[2], q3: box[3], high: box[4] }
  })

  // Pontos jitterados (caixa e bolinhas sempre coerentes)
  const accDots = accValues.map((v) => [jitter(0), v])
  const f1Dots = []
  Object.values(f1Values).forEach((values, i) => {
    values.forEach((v) => f1Dots.push([jitter(i + 1), v]))
  })

  Highcharts.chart(chart.value, {
    credits: { enabled: false },
    chart: {
      backgroundColor: 'transparent',
      style: { fontFamily: 'inherit' },
      type: 'boxplot',
      height: 360,
    },
    title: { text: 'Desempenho do GATv2 sobre 5 seeds' },
    subtitle: {
      text: 'Valores reais por seed (F1 medido por pixel do gráfico original) · box = p0 · p25 · p50 · p75 · p100',
    },
    xAxis: { categories },
    yAxis: {
      title: { text: null },
      min: 0,
      max: 1,
      tickInterval: 0.1,
      labels: { formatter() { return (this.value * 100).toFixed(0) + ' %' } },
    },
    plotOptions: {
      series: { grouping: false },
      boxplot: { whiskerLength: '60%', pointWidth: 60 },
      scatter: { marker: { radius: 5, lineWidth: 0, fillColor: '#ff6b35' } },
    },
    legend: {
      enabled: true,
      align: 'right',
      verticalAlign: 'top',
      layout: 'vertical',
      floating: true,
      x: -10,
      y: 30,
      itemStyle: { fontWeight: 'normal' },
    },
    series: [
      {
        name: 'Acurácia',
        type: 'boxplot',
        data: [accBox],
        color: '#3367d6',
        fillColor: '#e6f0ff',
        medianColor: '#1a3a7a',
      },
      {
        name: 'F1 por classe',
        type: 'boxplot',
        data: f1Boxes,
        color: '#137333',
        fillColor: '#e6f4ea',
        medianColor: '#0d4d22',
      },
      {
        name: 'Seeds',
        type: 'scatter',
        data: [...accDots, ...f1Dots],
        tooltip: { pointFormat: 'seed: {point.y:.3f}' },
      },
    ],
  })
})
</script>

<template>
  <div ref="chart" class="w-full"></div>
</template>

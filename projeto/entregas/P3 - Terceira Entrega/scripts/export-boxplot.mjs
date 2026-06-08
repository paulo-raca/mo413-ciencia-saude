// Renderiza ResultsCharts.vue em Playwright e salva SVG ou PNG do gráfico.
// Uso: node scripts/export-boxplot.mjs [out.svg|out.png]

import { chromium } from 'playwright-chromium'
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs'
import { dirname, resolve, extname } from 'node:path'
import { fileURLToPath } from 'node:url'

const __dirname = dirname(fileURLToPath(import.meta.url))
const projectDir = resolve(__dirname, '..')
const outPath = resolve(projectDir, process.argv[2] ?? 'assets/boxplot.svg')
const format = extname(outPath).toLowerCase().replace('.', '')
if (format !== 'svg' && format !== 'png') {
  throw new Error(`extensão não suportada: ${format} (use .svg ou .png)`)
}
const highchartsJs = readFileSync(resolve(projectDir, 'node_modules/highcharts/highcharts.js'), 'utf8')
const highchartsMoreJs = readFileSync(resolve(projectDir, 'node_modules/highcharts/highcharts-more.js'), 'utf8')
const exportingJs = readFileSync(resolve(projectDir, 'node_modules/highcharts/modules/exporting.js'), 'utf8')

// Mesmos valores do componente ResultsCharts.vue
const accValues = [0.7162, 0.7568, 0.7432, 0.8514, 0.8514]
const f1Values = {
  'Tumor Primário': [0.0, 0.37, 0.414, 0.589, 0.62],
  Metástase: [0.821, 0.844, 0.844, 0.921, 0.923],
  'Nevo Benigno': [0.4, 0.448, 0.667, 0.667, 0.667],
}

const html = `<!doctype html>
<html><head><meta charset="utf-8" /></head><body>
<div id="chart" style="width:1200px;height:600px;"></div>
<script>
function boxFromValues(values) {
  const s = [...values].sort((a, b) => a - b)
  return [s[0], s[1], s[2], s[3], s[4]]
}
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
function jitter(x, amount = 0.29) { return x + (rng() - 0.5) * amount }

const accValues = ${JSON.stringify(accValues)}
const f1Values = ${JSON.stringify(f1Values)}
const accBox = boxFromValues(accValues)
const f1Boxes = Object.values(f1Values).map((values, i) => {
  const box = boxFromValues(values)
  return { x: i + 1, low: box[0], q1: box[1], median: box[2], q3: box[3], high: box[4] }
})
const accDots = accValues.map((v) => [jitter(0), v])
const f1Dots = []
Object.values(f1Values).forEach((values, i) => {
  values.forEach((v) => f1Dots.push([jitter(i + 1), v]))
})
const categories = ['Acurácia', ...Object.keys(f1Values)]

window.__render = function () {
window.__chart = Highcharts.chart('chart', {
  credits: { enabled: false },
  chart: { backgroundColor: '#ffffff', style: { fontFamily: 'inherit' }, type: 'boxplot', height: 600, width: 1200 },
  title: { text: 'Desempenho do GATv2 sobre 5 seeds' },
  subtitle: { text: 'Valores reais por seed (F1 medido por pixel do gráfico original) · box = p0 · p25 · p50 · p75 · p100' },
  xAxis: { categories },
  yAxis: {
    title: { text: null }, min: 0, max: 1, tickInterval: 0.1,
    labels: { formatter() { return (this.value * 100).toFixed(0) + ' %' } },
  },
  plotOptions: {
    series: { grouping: false, animation: false },
    boxplot: { whiskerLength: '60%', pointWidth: 60 },
    scatter: { marker: { radius: 5, lineWidth: 0, fillColor: '#ff6b35' } },
  },
  legend: { enabled: true, align: 'right', verticalAlign: 'top', layout: 'vertical', floating: true, x: -10, y: 30, itemStyle: { fontWeight: 'normal' } },
  series: [
    { name: 'Acurácia', type: 'boxplot', data: [accBox], color: '#3367d6', fillColor: '#e6f0ff', medianColor: '#1a3a7a' },
    { name: 'F1 por classe', type: 'boxplot', data: f1Boxes, color: '#137333', fillColor: '#e6f4ea', medianColor: '#0d4d22' },
    { name: 'Seeds', type: 'scatter', data: [...accDots, ...f1Dots], tooltip: { pointFormat: 'seed: {point.y:.3f}' } },
  ],
})
window.__svg = window.__chart.getSVG()
}
</script></body></html>`

const browser = await chromium.launch()
const page = await browser.newPage({ viewport: { width: 1200, height: 600 }, deviceScaleFactor: 2 })
await page.goto('about:blank')
await page.setContent(html, { waitUntil: 'load' })
await page.addScriptTag({ content: highchartsJs })
await page.addScriptTag({ content: highchartsMoreJs })
await page.addScriptTag({ content: exportingJs })
await page.evaluate(() => window.__render())
await page.waitForFunction(() => typeof window.__svg === 'string' && window.__svg.length > 0)

mkdirSync(dirname(outPath), { recursive: true })
if (format === 'svg') {
  const svg = await page.evaluate(() => window.__svg)
  writeFileSync(outPath, svg, 'utf8')
  console.log(`escrito: ${outPath} (${svg.length} bytes, svg)`)
} else {
  const png = await page.locator('#chart').screenshot({ type: 'png', omitBackground: false })
  writeFileSync(outPath, png)
  console.log(`escrito: ${outPath} (${png.length} bytes, png @2x)`)
}
await browser.close()

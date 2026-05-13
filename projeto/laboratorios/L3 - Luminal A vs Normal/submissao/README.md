# Laboratório 3 — Analisando a Expressão de Luminal A vs Normal

Submissão do **subgrupo B** da equipe **ALFAK**.

Enunciado: [`../README.md`](../README.md).

Sessão Cytoscape com todas as subredes deste documento: [`breast-cancer-luminal-a-matrix-all-genes.cys`](breast-cancer-luminal-a-matrix-all-genes.cys).

## Subgrupo

- Alan Freitas Ribeiro — 193400
- Paulo Costa - 063607
- Naruan Ferraz - 323009

---

## Análise 1 — Cluster do hub de maior logFC entre genes superexpressos

### Subredes criadas

Uma sub-rede criada a partir da filtragem pela **maior componente conexa** do grafo principal, restringindo a:

- logFC > 1 (superexpressos)
- p-value ≤ 0,01
- adj. p-value ≤ 0,01

Sobre essa sub-rede aplicamos novamente o filtro de **maior componente conexa** e em seguida a **clusterização Leiden — Modularity**, observando todos os clusters formados. Por fim, mantivemos visível apenas **o cluster que continha o nó com maior valor de logFC**.

Para destacar conexões entre nós muito expressos, calculamos por aresta `max_logfc = max(logFC_a, logFC_b)` e coloriremos as arestas onde `max_logfc > 5`.

### Parâmetros de filtragem

- `Community Leiden - Modularity is between 6 and 6`
- `Node: LogFC is between 1 and 8,7`
- `Node: p-value is between 0 and 0,01`
- `Node: adj p-value is between 0 and 0,01`

### Estilos adotados

- Node — **Fill Color** — `LogFC` — Continuous
- Edge — **Transparency** — `Combined Score` — Continuous
- Edge — **Stroke Color** — `max_logfc` — Continuous (5,00 – 8,7) — *Default: green* (fora do range)

### Recortes do grafo

![Visão geral dos clusters Leiden sobre os genes superexpressos](analise-1-clusters.png)

![Cluster que contém o nó de maior logFC](analise-1-cluster-foco.png)

### Observações

No grafo acima conseguimos isolar a **sub-rede clusterizada (cluster 6)** que contém o nó com maior valor de logFC, e identificar com facilidade os nós que se relacionam com os de maior expressabilidade (maior logFC) dentro desse cluster.

---

## Análise 2 — Hubs entre genes super e subexpressos

### Subredes criadas

Sub-rede obtida filtrando-se pela **maior componente conexa** do grafo principal, restringindo a:

- |logFC| ≥ 2 (super **ou** subexpressos)
- p-value < 0,05

Sobre o resultado aplicamos novamente o filtro de **maior componente conexa** e adotamos os estilos visuais abaixo, com o objetivo de identificar genes de maior **influência** (centralidade de autovetor[^EIGEN]) dentro dessa sub-rede de genes deferencialmente expressos.

### Parâmetros de filtragem

- `Node: LogFC is not between -2 and 2`
- `Node: p-value is between 0 and 0,05`

### Estilos adotados

- Node — **Fill Color** — `LogFC` — Continuous
- Node — **Size** — `Eigenvector` — Continuous (10 → 30)
- Node — **Label Font Size** — `Eigenvector` — Continuous (5 → 12)
- Edge — **Transparency** — `Combined Score` — Continuous

### Recortes do grafo

![Sub-rede de DE genes (|logFC| ≥ 2) — tamanho ∝ eigenvector](analise-2-superexpressos.png)

![Zoom nos hubs com maior centralidade de autovetor](analise-2-zoom-hubs.png)

### Observações

Esta rede permite a fácil visualização de genes com **alta influência (eigenvector)** na sub-rede dos genes mais super e subexpressos. No grafo, identificamos **pontos de atenção**: um **trio de hubs** na segunda imagem e o gene **C074** na primeira imagem.

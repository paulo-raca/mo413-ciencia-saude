# Workspace — arquivos de trabalho da análise

Materiais intermediários da análise do projeto semestral (câncer de pele) — dados processados, sessões Cytoscape, workflow Orange e screenshots que o grupo usou durante a construção das redes.

Os *dumps brutos* do GEO (`*.soft.gz`) **não** ficam aqui; são baixáveis pelo accession e vão para [`../data/geo/`](../data/) (cache local, gitignored).

---

## Inventário

### Sessões e workflows

| Arquivo | O que é |
| --- | --- |
| [`skin_cancer.ows`](skin_cancer.ows) | Workflow Orange com 3 ramos paralelos, todos lendo `GSE7553_family.soft.gz` local e filtrando por `sample_substring`: (1) Pele normal vs. metastático, (2) Pele normal vs. in situ, (3) Pele normal vs. primário — o 3º ramo está com **título herdado** dizendo "in situ (1)" mas o substring configurado é `'Normal Skin, Primary'`. Cada ramo: `GEO SOFT Extractor (arquivo local, não baixa do GEO) → Unique → Differential Expression (×2, com/sem filtro p ≤ 0.001) → Merge → junta com Open Targets oncogenes → Save Data`. |
| [`GSE45216_cytoscape.cys`](GSE45216_cytoscape.cys) | Sessão Cytoscape já montada para GSE45216 (carcinoma espinocelular). |

### Tabelas de expressão diferencial (saída intermediária Orange/GEO)

| Arquivo | Dataset | Conteúdo |
| --- | --- | --- |
| [`GSE7553_GEO.csv`](GSE7553_GEO.csv) | GSE7553 | ID da sonda, `Gene.symbol`, `Gene.title`, `log2(fold change)`, `-LOG10(p-value)`. Separador `;`. |
| [`GSE45216_geo.tsv`](GSE45216_geo.tsv) | GSE45216 | Mesmas colunas, separador `\t`. |

### Redes PPI exportadas do STRING

| Arquivo | Dataset |
| --- | --- |
| [`GSE7553_string.tsv`](GSE7553_string.tsv) | GSE7553 — arestas PPI com pontuação de cada canal de evidência (neighborhood, fusion, phylogenetic, homology, coexpression, experimental, database, textmining) + `combined_score`. |
| [`GSE45216_string.tsv`](GSE45216_string.tsv) | GSE45216 — mesmo formato. |

### Listas de nós geradas pelo workflow Orange (`nodes/`)

Saída do `Save Data` do `skin_cancer.ows` — tabelas prontas para importar como *node table* no Cytoscape, já com *Entrez ID*, *Gene Symbol*, *LogFC*, *p-value* e `globalScore` (pontuação Open Targets).

- [`nodes/Melanoma_in-situ.csv`](nodes/Melanoma_in-situ.csv)
- [`nodes/Metastatic_melanoma.csv`](nodes/Metastatic_melanoma.csv)

(Arquivos `.csv.metadata` são sidecar do Orange.)

### Anotação externa

| Arquivo | Fonte |
| --- | --- |
| [`OT-EFO_0000756-associated-targets-4_20_2026-v26_03.tsv`](OT-EFO_0000756-associated-targets-4_20_2026-v26_03.tsv) | Open Targets — alvos associados a **melanoma** (`EFO_0000756`), export de 20/abr/2026, plataforma v26.03. Entra como `globalScore` nos *nodes*. |

### Screenshots de configuração

| Arquivo | Contexto |
| --- | --- |
| [`GSE7553.png`](GSE7553.png) | Rede PPI GSE7553 renderizada. |
| [`GSE7553 string config.png`](GSE7553%20string%20config.png) | Configuração usada no STRING ao exportar. |

---

## Próximo passo — reimplementar em Python

Objetivo: reescrever o pipeline do `skin_cancer.ows` como notebook Marimo (`analise.py`) usando `geoparse` + `pandas`, de forma que a geração de `nodes/*.csv` seja reprodutível a partir de `../data/geo/*.soft.gz`.

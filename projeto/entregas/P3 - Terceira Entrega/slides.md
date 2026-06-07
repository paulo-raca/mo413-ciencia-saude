# Câncer de Pele e seus Tipos: uma Análise do Perfil de Expressão Gênica em Redes

MO413A - Ciência e Visualização de Dados em Saúde

Alan Freitas Ribeiro (193400)
Augusto José Peterlevitz (209783)
Felipe Kennedy Carvalho Torquato (174157)
Luis Henrique Angélico (248891)
Naruan Francisco Ferraz e Ferraz (323009)
Paulo Costa (063607)

*(Instituto de Computação | Instituto de Biologia | UNICAMP)*

---

# Resumo

Este projeto visa comparar redes de interação gênica derivadas de amostras de **câncer de pele melanoma, não-melanoma e tecido saudável**. Serão analisadas as diferenças na topologia da rede, nos genes centrais e nos módulos biológicos, com objetivo de observar padrões específicos da doença e mecanismos compartilhados, fornecendo informações sobre a biologia tumoral e potenciais biomarcadores.

---

# Fundamentação Teórica

*Felipe* — slide em branco.

---

# Tipos de Câncer de Pele

Imagem comparando epiderme normal (squamous cells, basal cells, melanocytes) com Basal cell carcinoma, Squamous cell carcinoma e Melanoma.

**Classificação**
- Local
- Tipo celular de origem

**Tipos**
- Carcinoma Basocelular
- Carcinoma Espinocelular
- Melanoma

---

# Epidemiologia — Câncer de Pele no Mundo

Imagem do Global Cancer Observatory (Cancer Tomorrow / IARC):

- **2022:** 1,57 milhão de novos casos
- **2045:** 2,96 milhões (estimativa)

Melanoma de pele + Não-melanoma, ambos os sexos, idade 0–85+, mundo.

Fonte: gco.iarc.who.int (Globocan 2022, versão 1.1 — 08.02.2024).

---

# Perguntas a serem respondidas

1. Como as redes gênicas diferem entre câncer de pele melanoma, não-melanoma e tecido saudável?
2. Existem genes "exclusivos" em cada tipo de câncer? Quais são?
3. Existem vias moleculares compartilhadas entre melanoma e não-melanoma?
4. Quais interações são adquiridas ou perdidas em cada tipo de câncer?
5. Podemos identificar módulos (clusters) específicos para cada tipo de câncer?

---

# 3. Metodologia

1. Obtenção de datasets por meio do Gene Expression Omnibus (GEO)
   - Saudável
   - Melanoma
   - Não-melanoma
2. Obtenção de expressão diferencial:
   - Saudável vs Melanoma
   - Saudável vs Não-melanoma
   - Melanoma vs Não-melanoma
3. Consulta do database STRING
   - Interações entre proteínas
   - Scores de confiança

---

# 3. Metodologia (continuação)

4. Análise no Cytoscape
   - Eigenvector centrality (CytoNCA)
   - Degree e clustering coefficient (NetworkAnalyzer)
   - Clusterização (clusterMaker2/MCODE)
5. Comparação entre redes
   - Identificação de genes ganhos/perdidos (saudável vs não saudável)
   - Identificação de genes centrais e arestas exclusivas
   - Métricas (degree, betweenness centrality e closeness centrality)
   - Identificação de semelhanças entre melanoma e saudável

---

# Base de dados: Gene Expression Omnibus (GEO)

| Base de dados | Dataset | Grupos |
| --- | --- | --- |
| Gene Expression Omnibus (GEO) | GSE7553 | Carcinoma baso celular, Melanoma in situ (estágio 0), Melanoma primário, Melanoma metastático, Carcinoma espinocelular, **Pele Normal (controle)** |
| Gene Expression Omnibus (GEO) | GSE45216 | Carcinoma espinocelular, Queratose actínica |
| Open Targets Platform | Melanoma | — |
| Open Targets Platform | Carcinoma | — |
| The Cancer Genome Atlas Program (TCGA) | TCGA-SKCM | |

---

# Análises adicionais — Deep Learning

- Graph Attention Networks — GAT (Baseline)
  - Dataset: TCGA-SKCM (Xena Browser)
  - Modelo: GATv2Conv
  - Distribuição de classes:
    - 472 pacientes
    - 103 Primários, 368 Metástase, 1 normal
  - Filtramos os 500 Top K genes pela variância
  - Usamos um limiar de confiança do STRING (interações) de 50%
  - Treinamos por 5000 épocas

---

# Fundamentação Teórica: Graph Neural Network

*Augusto*

**Neural Network**

$$H^{(l+1)} = \sigma(H^{(l)} W^{(l)})$$

**Graph Neural Network**

$$H^{(l+1)} = \sigma\!\left(\tilde{D}^{-\tfrac{1}{2}} \tilde{A} \tilde{D}^{-\tfrac{1}{2}} H^{(l)} W^{(l)}\right)$$

- $H^{(l)}$: embeddings da camada $l$
- $W^{(l)}$: pesos a serem aprendidos no treinamento
- $\tilde{A}$: matriz adjacente
- $\tilde{D}$: matriz diagonal (normalização de dados)
- $\sigma$: função de ativação

---

# Fundamentação Teórica: GAT

*Augusto*

**1. Score de importância por meio de mecanismo de atenção $a$**

$$e_{ij} = a(W h_i, W h_j)$$

**2. Normalização com Softmax**

$$\alpha_{ij} = \text{Softmax}_j(e_{ij}) = \frac{\exp(\text{LeakyReLU}(e_{ij}))}{\sum_{k \in \mathcal{N}_i} \exp(\text{LeakyReLU}(e_{ik}))}$$

**3. Weighted Aggregation**

$$h_i^{(l+1)} = \sigma\!\left(\sum_{j \in \mathcal{N}_i} \alpha_{ij} W h_j^{(l)}\right)$$

Diagrama: Velickovi, P. *et al* (2018).

---

# Base de dados: Transformações e tratamentos

*Luis*

Diagrama de pipeline com 18 etapas, do download bruto até o `.pt` consumido pelo GAT:

1. **TOIL TPM** — baixa a matriz `log2(TPM+0.001)` recomputada da UCSC Xena para todas as amostras TCGA + GTEx + TARGET.
2. **Phenotype** — baixa o arquivo de rótulos da Xena com tipo de tecido, *sample type* e coorte de cada amostra.
3. **GSE112509** — baixa as contagens DESeq2 normalizadas do GEO para o estudo de nevos benignos vs melanomas.
4. **GENCODE probemap** — baixa a tabela de equivalência Ensembl ID ↔ símbolo HGNC ↔ tipo de gene (versão v23).
5. **STRING API** — endpoint REST do STRING v12 que devolve interações físicas com *combined score*.
6. **Filtra TCGA-SKCM** — seleciona apenas amostras do coorte SKCM com *sample type* "Primary Tumor" (Class 0) ou "Metastatic" (Class 1).
7. **Ensembl → HGNC** — substitui IDs Ensembl pelos símbolos HGNC do probemap, descartando linhas sem mapeamento.
8. **Seleciona nevos** — filtra o GSE112509 para reter apenas as 23 amostras de nevo (Class 2), descartando os melanomas do GEO.
9. **log2(counts+1)** — aplica `log2(x+1)` às contagens DESeq2 do GSE para casar a *escala* do TOIL.
10. **Concatena coortes** — junta as matrizes TCGA-SKCM e GSE112509 por gene em comum, formando a matriz combinada (~492 amostras).
11. **Protein-coding** — mantém apenas genes anotados como *protein-coding* no GENCODE, descartando pseudogenes/lncRNAs.
12. **Split 70/15/15** — divisão estratificada por classe com `SEED=42`, persistida em `splits.npz`.
13. **Top-variable genes** — calcula a variância **somente nas amostras de treino do TCGA** e seleciona `NUM_NODES = 1000` mais variáveis.
14. **STRING REST** — consulta o STRING para os 1000 símbolos com `required_score ≥ 200`, recuperando todas as arestas físicas entre eles.
15. **edge_index único** — converte a lista de arestas em um `edge_index` PyG **compartilhado** por todas as amostras (a topologia não muda).
16. **Per-sample x,y** — para cada amostra constrói `x ∈ ℝ^{1000×1}` (vetor de expressão) e `y ∈ {0,1,2}` (rótulo de classe).
17. **Data objects** — empacota cada `(x, edge_index, y)` em um `torch_geometric.data.Data`.
18. **Saída** — serializa a lista de 492 grafos em `skcm_nevi_1000_200.pt` junto a `splits.npz` para uso reprodutível em treino/validação/teste.

---

# Treino GAT

*Luis*

**Arquitetura (`GATv2Classifier`)**

| Parâmetro | Valor |
| --- | --- |
| Camadas GATv2 | 3 |
| `hidden_channels` | 128 |
| Cabeças por camada | 4, 4, 1 |
| `dropout` | 0.4 |
| Normalização | `LayerNorm` após cada camada |
| Pooling | `global_mean_pool` |
| Cabeça de classificação | `Linear(128 → 3)` |
| Atributo de nó (`in_channels`) | 1 (expressão log) |

**Hiperparâmetros de treino (`src/train.py`)**

| Parâmetro | Valor |
| --- | --- |
| Otimizador | `Adam` |
| `learning_rate` | 1e-3 |
| `weight_decay` | 5e-4 |
| Scheduler | `ReduceLROnPlateau` (factor 0.5, patience 10, min_lr 1e-6) |
| Loss | `CrossEntropyLoss` |
| Balanceamento | `WeightedRandomSampler` por *batch* (train only) |
| `batch_size` | 32 |
| `num_epochs` (máx) | 500 |
| `EARLY_STOP_PATIENCE` | 50 (sobre val loss) |
| `SEED` (single-run) | 42 |
| Split | 70/15/15 estratificado, salvo em `splits.npz` |
| Seleção de modelo | menor val loss observada |
| Device | auto: CUDA → MPS → CPU (env `GAT_DEVICE`) |

---

# Análises adicionais GAT

*Luis*

- Embeddings
- Pseudotempo
- Biomarcadores

---

# Embeddings — t-SNE e vizinhos próximos

*Luis*

O modelo processa o grafo PPI de cada amostra com um vetor de 64 números que mistura [a expressão] de seus vizinhos PPI (e dos vizinhos deles); [aplica] média desses 1000 vetores em um único [vetor de] embedding.

Projeção t-SNE colorida por classe verdadeira (Tumor Primário, Metástase, Nevo Benigno).

Painel lateral — exemplo de amostra **TCGA-EB-A5VU-01**:
- Classe verdadeira: Tumor Primário
- Predita: Tumor Primário
- Confiança: 54,8% — correta
- 10 vizinhos mais próximos por cosseno (TCGA-EB-A57M-01, TCGA-D3-A1Q6-06, TCGA-BF-A1PX-01, TCGA-XV-A9W2-01, TCGA-BF-A3DJ-01, TCGA-EB-A3XC-01, TCGA-GN-A4U9-06, TCGA-D3-A1Q5-06, TCGA-WE-A8ZM-06, TCGA-EE-A20H-06)

---

# Embeddings — heatmap de atenção entre classes

*Luis*

Cada coluna é uma aresta PPI que o modelo trata com atenção diferente entre as três classes. Cor = atenção média sobre 5 seeds. As arestas são ordenadas por **amplitude entre classes / variabilidade entre seeds** — valores altos indicam que o modelo trata a aresta como informativa de forma consistente e diferencia entre tipos de amostra.

Heatmap:
- Linhas: Primary Tumor, Metastasis, Benign Nevus
- Colunas: pares de gene (PI3 — KRT1, NDUROG2 — POU5F3, KRT3 — KRT27, KRT14 — KRT12, CTSC — SLPI, PIP — ARG5, DSG1 — TGM3, SCGB1D2 — SCGB1D2, CARD17 — CARD18, DEFB1 — DEFR4A, DEFB1 — DEFB108A, LOR — LCE3A, ICE1L, CARD12B — C1orf38, MAGEA9 — MAGEC1, PI3 — LCE3A, KRT11 — KRT8R, KRT11 — KRT8R, LOR — SPRR2G, LOR — SPRR8D, LOR — SPRR8D, FGF22 — PI4, PIP — JOSTNC1, LCEC — CRCT1, LOR — LCE6A, BPXI — DMP, KRT12 — KRT27, KRT11 — KRT75, KRTFN — LCE6A, KRT16 — KRT6B, LOR — LCE6A, RPA — CCL11, LGR — LCEJC, IRK22-5 — TBP2G, FGF10 — PLAT3, PI3 — LOR, OAT — NPFX2)

---

# Pseudotempo

Ordenamos toda amostra ao longo de um eixo de "grau de tumor" e observamos como [a atenção] cresce conforme as amostras ficam mais parecidas com tumor — esses são candidatos a biomarcadores.

Calculamos duas âncoras no espaço de embeddings: o embedding médio das amostras de pele normal (a "âncora de normal") e o embedding médio das amostras de Metástase (a "âncora de metástase"). Em seguida, desenhamos uma reta entre as duas. Cada amostra recebe um número entre 0 e 1:

- **0** = embedding na âncora de pele normal
- **1** = embedding na âncora de metástase
- valores intermediários = "em algum ponto do caminho"

Dividimos esse eixo 0→1 em **10 bins de largura igual** (decis) e, para cada bin, [agregamos as] amostras que caíram nele. O resultado é um retrato de *quais genes o modelo foca* ao longo da trajetória.

Como ler a figura: uma linha clara à esquerda e escura à direita significa "o modelo prestava atenção [quando a amostra era normal] e deixou de se importar quando elas ficaram mais parecidas com tumor". O padrão inverso significa o oposto.

Heatmap "Per-decile mean attention (row-normalized) — Each row peaks once; rows ordered by when their attention peaks". Eixo Y: genes (SBK1, CAL, SOSTDC1, DEFB4B, KRT12, KRT3, LCE2D, MAGEC1, LCE4A, ITLN2, POUS5F, KRT17, SPRR2D, CUL92, TRIM71, LCE3D, ICE1L, IGLV10-54, SPRR2F, SCGB1D2, AQP1, GH7, LCALS7, MAGEB6, MRP, ENTRO1A, CDH1, SPRR2A, NPTX2, DSG1, KRT1, KRT16, OMP, LOR, LCE3A, KRT13, SLPI, LCE2C, PI4, ICGN3-15). Eixo X: pseudotime decile (Normal-like → Metastasis-like) com (n=9, n=9, n=32, n=101, n=86, n=32, n=47, n=15, n=1).

---

# Análises adicionais — Deep Learning (Resultados e Próximos passos)

- **Resultados**
  - Validamos o funcionamento do treinamento
  - Validamos o funcionamento da ferramenta de [visualização]
- **Próximos passos**
  - Integrar outros datasets
  - Melhorar a ferramenta de visualização de dados
    - Adicionar opções para comparar pacientes
    - Adicionar opções para comparações gerais
    - Melhorar exploração e filtragem de dados

Screenshot da ferramenta interativa de exploração — amostra `TCGA-ER-A24-01A`, Tumor Primário, Confiança absoluta 50,79%, distribuição das probabilidades e mapa de cores de atenção (gene em destaque: **CALML5**, expressão 0.30).

---

# Ferramentas

- Gene Expression Omnibus (GEO)
- Excel
- STRING
- Cytoscape
  - CytoNCA
  - NetworkAnalyzer
  - MCODE
  - clusterMaker2
- Python
  - PyTorch
  - Pandas
  - Scikit-learn

---

# Modelo lógico da base de grafos que será construída

```
Gene  ──[Expressão diferencial]──►  Comparação  ──[Resulta em]──►  Tecido
```

**Gene** — atributos: `Símbolo: string`, `Nome: string`.

**Comparação** — atributos: `Nome: string`, `dataset_id: string`.

**Tecido** — atributos: `Nome: string`, `dataset_id: string`.

**Aresta "Expressão diferencial"** — atributos: `log2fc: float`, `p_value: float`.

---

# Workflow GSE7553 — Carcinoma vs Normal skin

Diagrama do workflow Orange:

- **Metastatic Melanoma from GEO Soft Extractor** → Unique → ramos paralelos:
  - *Differential Expression* com `logFC ≤ −2,3 ou logFC ≥ 2,3`
  - *Differential Expression* com `p-value ≤ 0,001`
  - Volcano Plot (inspeção)
- Os dois ramos vão para **Combine LogFC with p-value**.
- Em paralelo: **Melanoma Oncogenes from Open Gene Targets** → Unique (2).
- Os dois fluxos se juntam em **Append Oncogene Score** → *Only ID, Symbol, LogFC, p-value, and Oncogenes* → *Padronize Names* → **Save Nodes to Cytoscape** (saída: `Nodes`).
- Em paralelo: **Select only Entrez ID** → `Nodes String` (entrada do STRING).
- **STRING processed** → *String network* → *Select Physical* → *Select Only origin, destination and combined score* → **Cytoscape Edges** (saída: `Edges`).

---

# Também em Python!

Decidimos replicar a análise feita em Orange em um notebook Python. Acreditamos que em Python será mais fácil generalizar as próximas análises.

Screenshots do notebook:

- Aba "datasets_summary" com GSE4570, GSE2503, GSE53462, GSE8401, **GSE7553**, GSE45216.
- GSE7553 — *Gene Expression Patterns Involved in the Malignant Transformation and Progression of Metastatic Melanoma*. Plataforma GPL570, 87 amostras, submetido em 19/abr/2007.
- Amostras por categoria: Metastatic Melanoma 40, Basal Cell Carcinoma 15, Primary Melanoma 14, Squamous Cell Carcinoma 11.
- Tabela final `Nodes_cytoscape.csv` (360 linhas × 5 colunas): Entrez ID, Gene Symbol, LogFC, p-value, oncogeneScore — ex.: IRF6 −3,957…, BNC1 −3,990…, ATP6V1C2 −2,760…, SERPINA2 −4,506…, BTBD16 −2,606…, GRHL1 −1,544…, RAET1E −1,579…, PROM2 −4,405…, SERPINB12 −2,533…

**Comparação com baseline do Orange**

| Métrica | Valor |
| --- | --- |
| Genes no notebook | 360 |
| Genes esperados (Orange) | 359 |
| Em comum | 358 |
| Só no notebook | 1 |
| Só no Orange | 0 |
| Similaridade de Jaccard | **99,72%** |

**Status:** pipeline bate ≈99,7% com o baseline Orange. Os genes só no nosso output (tipicamente 1) correspondem a um **bug conhecido do `orange3-biosci.geo_soft_extractor`** — descarta Entrez IDs com 4 ou 5 dígitos (filtro `len(candidate) > 2` nas linhas 637 e 655), marcando como "?" e perdendo-os no Unique. Afeta ~139 probes de genes "antigos" (Entrez baixo): A2M (2), ACACB (32), ACADL (35), ACAT1 (38), ACP1 (52), etc.

Não replicamos o bug — nosso output inclui esses genes legitimamente.

---

# Resultados — GSE7553

Duas redes lado a lado:

**Melanoma vs Pele Normal** (esquerda) — rede mais densa, com vários clusters incluindo nós como ALOX12, COL12A1, LAMC2, CTNNBP1, ITGB6, mais um cluster central com KRT (KRT1, KRT5, KRT14, KRT15, KRT19, KRT33A, KRT35, KRT68, KRT77, KRT78, KRT2), GSTA, TGM1, LCE1B, SPRR2A, IVL, LOR, PPL, EVPL, DSC3, DSG3, PKP3, PKP2, JUP, DSG1, FLG.

**Carcinoma vs Pele Normal** (direita) — rede esparsa, com clusters menores e dispersos: FOS/CREB5/BACH1/BACH2 (com CREB5 destacado em azul); NRXN3/CRBN/RAMP1/CALCB; SOX13/LEF1; PTCH1/PTCH2; PCNT/PCDH16/PCDH18; PRKN/FAM20C/DMD/TNNI2; KIF12/KIF20A; GPHA2/TSHR; GLI1/GLI2; GFRA3/NRTN; VGAN.

---

# Resultados GSE7553 — close-up do cluster de queratinas

Recorte do cluster KRT — nós principais: DSP (centro), KRT19, KRT15, KRT34/KRT3/KRT14, KRT35/KRT33A, KRT68, KRT80/KRT5, KRT77/KRT78/KRT78, KRT2, GSTA, TGM1, LCE1B, SPRR2A, IVL, LOR, PPL, EVPL, SPRR2A/CDSN, LCE2B, DSC3/DSG3/DSC1, PKP3, PKP2/JUP/DSC2, CTNNBP1/PKP4/DSG1, SDC1/LAMA2/LOX12/KLK5, COL17A1/SPINK5, FLG.

---

# Workflow GSE45216 (Carcinoma vs Queratose actínica)

Diagrama do workflow Orange:

- **GSE45216 — AK vs SCC** → Unique (2) → ramos:
  - *Differential Expression* com `logFC ≤ −0,15 ou logFC ≥ 0,15`
  - *Differential Expression* com `p-value ≤ 0,001`
- **Merge Data** combina os dois ramos.
- Em paralelo: **Melanome — Oncogenes** → Unique (3) → Merge Data (1) → Select Columns (1) → Edit Domain → `Nodes Cytoscape`.
- Outro ramo: Select Columns → `Nodes String`.
- **STRING Network** → *Select Physical (Experimental and Databases)* → *Extract only origin, destination and combined score* → Save Data.

---

# Resultados GSE45216 (Carcinoma vs Queratose actínica)

Múltiplas pequenas redes resultantes:

Destaque (à esquerda): cluster PLP1 / ITGB5 / FLNB / ITGA5 / CD36 / PPP — todos conectados em pequena sub-rede densa.

Demais clusters menores, alguns com 2–3 nós: vários pares isolados (sem rotulação detalhada), incluindo nodos verdes (CD36, PPP destacados em verde-escuro) e azuis.

---

# Perspectivas Futuras

- A
- B
- C

*(placeholders — a preencher)*

---

# Discussão

- A
- B
- C

*(placeholders — a preencher)*

---

# Conclusão

- A
- B
- C

*(placeholders — a preencher)*

---

# Trabalhos Futuros

- A
- B
- C

*(placeholders — a preencher)*

---

# Referências bibliográficas

- A
- B
- C
- Veličković, P., Cucurull, G., Casanova, A., Romero, A., Lio, P., & Bengio, Y. (2017). *Graph attention networks*. arXiv preprint arXiv:1710.10903.

*(referências A, B, C — placeholders a preencher)*

---

# Obrigado!

Contact us:
Naruan Ferraz, n323009@dac.unicamp.br

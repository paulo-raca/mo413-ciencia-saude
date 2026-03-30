# Resumo: Gene Network Rewiring to Study Melanoma Stage Progression

---

## Metadados

| Campo              | Informação                                                                                                  |
| ------------------ | ----------------------------------------------------------------------------------------------------------- |
| **Título**         | Gene Network Rewiring to Study Melanoma Stage Progression and Elements Essential for Driving Melanoma       |
| **Autores**        | Abhinav Kaushik, Yashuma Bhatia, Shakir Ali, Dinesh Gupta                                                   |
| **Filiação**       | Bioinformatics Laboratory, International Centre for Genetic Engineering and Biotechnology, New Delhi, Índia |
| **Revista**        | _PLoS ONE_                                                                                                  |
| **Ano**            | 2015                                                                                                        |
| **Volume**         | 10(11): e0142443                                                                                            |
| **DOI**            | https://doi.org/10.1371/journal.pone.0142443                                                                |
| **Acesso**         | Acesso aberto (Open Access)                                                                                 |
| **Banco de dados** | http://bioinfo.icgeb.res.in/m3db/                                                                           |

---

## Problema Investigado

### Contexto

Melanoma metastático tem prognóstico ruim, pois é difícil identificar quais genes _causam_ a progressão da doença. Os estudos tradicionais focam em **genes diferencialmente expressos (DE)**[^deg] — ou seja, genes que ficam mais ou menos ativos no tumor. Porém, nem todo gene importante muda de nível de atividade.

### O Insight Central do Artigo

> **A maioria dos genes que mudam suas conexões de rede durante a progressão do melanoma NÃO são diferencialmente expressos.**

Em outras palavras: um gene pode permanecer igualmente "ativo" no tecido saudável e no tumor, mas mudar _com quem ele interage_ — passando a co-expressar com genes cancerígenos. Esse fenômeno é chamado de **rewiring**[^rewiring] (re-fiação da rede).

Isso é análogo a uma pessoa que não muda seu comportamento, mas muda completamente seu grupo de amigos — e seus novos amigos são todos criminosos. A pessoa em si não mudou, mas suas conexões mudaram tudo.

### A Pergunta de Pesquisa

> **"É possível identificar genes-chave para a progressão do melanoma estudando a mudança nas conexões da rede gênica ao longo dos estágios da doença, em vez de apenas olhar para mudanças no nível de expressão?"**

---

## Dados Utilizados

| Estágio                       | Amostras | Séries | Plataformas   |
| ----------------------------- | -------- | ------ | ------------- |
| Normal (N)                    | 97       | 13     | 7 plataformas |
| Cutâneo não-metastático (CnM) | 183      | 9      | 5 plataformas |
| Cutâneo metastático (CM)      | 246      | 10     | 5 plataformas |
| Linfonodo metastático (LN)    | 116      | 7      | 5 plataformas |
| **Total**                     | **642**  | **39** | múltiplas     |

- **Tipo de dado:** Microarray[^microarray] de expressão gênica (mRNA)
- **Origem:** Repositórios públicos (GEO, ArrayExpress)
- **Pré-processamento:** Correção de efeito de lote com ComBat[^combat]; normalização

---

## Pipeline / Metodologia

```
╔══════════════════════════════════════════════════════════════════════════╗
║         PIPELINE DO ARTIGO (Kaushik et al., PLoS ONE 2015)               ║
╚══════════════════════════════════════════════════════════════════════════╝

  ┌──────────────────────────────────────────────────────────────────────┐
  │  PASSO 1: COLETA E INTEGRAÇÃO DE DADOS                               │
  │                                                                      │
  │  642 microarrays públicos → 4 grupos (N, CnM, CM, LN)               │
  │  ComBat: remove variações técnicas entre plataformas                │
  └───────────────────────────────┬──────────────────────────────────────┘
                                  │
                                  ▼
  ┌──────────────────────────────────────────────────────────────────────┐
  │  PASSO 2: CONSTRUÇÃO DAS REDES DE CO-EXPRESSÃO                       │
  │                                                                      │
  │  Para cada estágio (N, CnM, CM, LN):                                │
  │    • Calcular correlação de Pearson entre todos os pares de genes   │
  │    • Aplicar limiar de correlação → criar arestas                   │
  │    • Resultado: 4 redes gênicas (uma por estágio)                   │
  └───────────────────────────────┬──────────────────────────────────────┘
                                  │
                                  ▼
  ┌──────────────────────────────────────────────────────────────────────┐
  │  PASSO 3: ANÁLISE DE EXPRESSÃO DIFERENCIAL (DE)                      │
  │                                                                      │
  │  Comparações: N vs CnM, N vs CM, N vs LN                           │
  │  Critério: |logFC| > 1, adj. p < 0.05                               │
  │  Identificados: 324 (CnM), 622 (CM), 1398 (LN) genes DE            │
  └───────────────────────────────┬──────────────────────────────────────┘
                                  │
                                  ▼
  ┌──────────────────────────────────────────────────────────────────────┐
  │  PASSO 4: ANÁLISE DE REWIRING (CONECTIVIDADE DIFERENCIAL)            │
  │                                                                      │
  │  Para cada gene: comparar conexões em N vs cada estágio tumoral     │
  │  Score de rewiring = conexões ganhas + conexões perdidas            │
  │  Identificar genes com alto rewiring mas BAIXA expressão diferencial│
  │                                                                      │
  │  DESCOBERTA CHAVE: maioria dos genes re-fiados NÃO são DE           │
  └───────────────────────────────┬──────────────────────────────────────┘
                                  │
                                  ▼
  ┌──────────────────────────────────────────────────────────────────────┐
  │  PASSO 5: ANÁLISE DE HUBS POR ESTÁGIO                                │
  │                                                                      │
  │  Identificar hubs (genes altamente conectados) em cada estágio      │
  │  Comparar quais hubs mudam entre estágios                           │
  │  Resultado: hubs distintos para cada fase de progressão             │
  └───────────────────────────────┬──────────────────────────────────────┘
                                  │
                                  ▼
  ┌──────────────────────────────────────────────────────────────────────┐
  │  PASSO 6: ENRIQUECIMENTO DE VIAS (PATHWAY ANALYSIS)                  │
  │                                                                      │
  │  Genes com alto rewiring → enriquecimento em vias KEGG/GO           │
  │  Classificação de vias por estágio de melanoma                      │
  │  Quantificação da complexidade das vias com a progressão            │
  └───────────────────────────────┬──────────────────────────────────────┘
                                  │
                                  ▼
  ┌──────────────────────────────────────────────────────────────────────┐
  │  PASSO 7: BANCO DE DADOS PÚBLICO (M3DB)                              │
  │                                                                      │
  │  Resultados disponibilizados em banco SQL com interface Cytoscape   │
  │  URL: http://bioinfo.icgeb.res.in/m3db/                             │
  └──────────────────────────────────────────────────────────────────────┘
```

---

## Estratégia de Grafo Utilizada

### Tipo de rede

**Grafos**[^grafo] **de co-expressão gênica não-direcionados**, construídos separadamente para cada estágio do melanoma:

- **Nós:** genes
- **Arestas:** correlação de Pearson[^pearson] acima de um limiar entre dois genes (co-expressão)
- **Peso das arestas:** valor de correlação (0 a 1)
- **Quatro redes paralelas:** N, CnM, CM, LN

### Estratégia central: Análise de Rewiring (Conectividade Diferencial)

A estratégia inovadora do artigo é **comparar as topologias das 4 redes** em vez de apenas comparar os níveis de expressão dos genes:

1. **Construir** a rede para o estado Normal (N).
2. **Construir** as redes para cada estágio tumoral (CnM, CM, LN).
3. **Para cada gene**, calcular quantas conexões ele ganhou e quantas perdeu entre N e o estágio tumoral.
4. **Ranquear** os genes pelo score de rewiring[^scorerewiring].
5. **Cruzar** a lista de genes altamente re-fiados com a lista de genes DE: os genes que têm alto rewiring mas baixa expressão diferencial são os novos candidatos identificados pelo método.

### Análise de hubs

Além do rewiring, os autores identificaram **hubs**[^hub] **específicos de cada estágio** — os genes com maior grau em cada rede. Como hubs diferentes emergem em diferentes estágios da doença, eles representam os "motores" moleculares de cada fase da progressão.

---

## Resultados Principais

| Comparação    | Genes DE identificados |
| ------------- | ---------------------- |
| Normal vs CnM | 324                    |
| Normal vs CM  | 622                    |
| Normal vs LN  | 1398                   |

**Genes conservados em todos os estágios (essenciais para o melanoma):**

- 55 genes expressos diferencialmente em todos os estágios
- Inclui: _MAGEA1, MAGEA12, IL8, FOXD1, IL1B, POSTN, PRAME, MMP9, SERPINE, CTGF_
- _PRAME_ é consistentemente o gene mais upregulado em todos os estágios

**Descoberta sobre rewiring:**

- A maioria dos genes que mudam suas conexões de rede **não** são diferencialmente expressos
- Os genes associados à doença no banco de dados têm conectividade forte e anormal
- A conectividade aumenta com a progressão da doença (redes ficam mais densas e complexas)

**Hubs distintos por estágio:**

- Hubs diferentes emergem em CnM, CM e LN para as mesmas vias biológicas[^vias] conservadas
- Indica que os mesmos processos são "executados" por diferentes genes centrais em cada estágio

**Enriquecimento de vias:**

- Complexidade das vias aumenta abruptamente após o início da metástase
- Vias enriquecidas em LN: resposta imune, sinalização de quimiocinas, metabolismo

---

## Por que é Relevante para o Projeto sobre Câncer de Pele

Este artigo é diretamente relevante ao projeto da equipe ALFAK pelos seguintes motivos:

### 1. Metodologia de comparação entre redes

O projeto compara redes de melanoma, não-melanoma e tecido saudável. Este artigo mostra como construir e comparar redes de co-expressão entre diferentes condições, usando exatamente a abordagem de correlação de Pearson + análise de hubs.

### 2. Insight sobre rewiring vs. expressão diferencial

A descoberta de que genes importantes podem ter suas _conexões_ alteradas sem mudar seu _nível de expressão_ é crucial: o projeto deve considerar tanto genes DE quanto genes com alta conectividade diferencial[^condif].

### 3. Progressão de estágios

O pipeline N → CnM → CM → LN é análogo à comparação do projeto: saudável → não-melanoma → melanoma. A estratégia de construir uma rede por grupo e compará-las é diretamente aplicável.

### 4. Análise de hubs como biomarcadores

A identificação de hubs específicos de cada estágio fornece um método para descobrir genes candidatos a biomarcadores[^biomarcador] — objetivo central do projeto.

### 5. Vias moleculares compartilhadas

A análise revela vias compartilhadas entre estágios (ex: sinalização imune), análoga à pergunta do projeto sobre vias compartilhadas entre melanoma e não-melanoma.

---

## Referência Completa

**ABNT:**
KAUSHIK, Abhinav; BHATIA, Yashuma; ALI, Shakir; GUPTA, Dinesh. Gene Network Rewiring to Study Melanoma Stage Progression and Elements Essential for Driving Melanoma. **PLoS ONE**, v. 10, n. 11, p. e0142443, 11 nov. 2015. DOI: https://doi.org/10.1371/journal.pone.0142443.

**Vancouver:**
Kaushik A, Bhatia Y, Ali S, Gupta D. Gene Network Rewiring to Study Melanoma Stage Progression and Elements Essential for Driving Melanoma. PLoS ONE. 2015 Nov 11;10(11):e0142443. doi: 10.1371/journal.pone.0142443.

**APA:**
Kaushik, A., Bhatia, Y., Ali, S., & Gupta, D. (2015). Gene Network Rewiring to Study Melanoma Stage Progression and Elements Essential for Driving Melanoma. _PLoS ONE_, _10_(11), e0142443. https://doi.org/10.1371/journal.pone.0142443

---

_Resumo elaborado em: 2026-03-29_
_PDF disponível em: artigos/A/bhatt2015-melanoma-network-rewiring.pdf_

---

## Notas

[^deg]: _Gene Diferencialmente Expresso (DEG)_ — gene que apresenta nível de atividade significativamente diferente entre duas condições (ex: tecido saudável vs. tumor).

[^rewiring]: _Rewiring de rede (Network Rewiring)_ — mudança nas conexões de uma rede gênica entre dois estados, onde um gene passa a co-expressar com parceiros moleculares diferentes mesmo sem alterar seu nível de expressão.

[^microarray]: _Microarray_ — tecnologia laboratorial que mede simultaneamente o nível de expressão de milhares de genes em uma amostra de tecido, como uma "fotografia" da atividade gênica.

[^combat]: _ComBat (batch correction)_ — método estatístico para remover o "efeito de lote", ou seja, variações técnicas introduzidas quando dados são produzidos em laboratórios ou plataformas diferentes.

[^pearson]: _Correlação de Pearson_ — medida estatística (de −1 a +1) que quantifica o quanto dois genes variam juntos em suas expressões; usada para definir arestas em redes de co-expressão.

[^grafo]: _Grafo / Rede_ — estrutura matemática com nós (genes) conectados por arestas (relações de co-expressão); a representação formal de uma rede gênica.

[^hub]: _Hub (gene hub)_ — nó de altíssimo grau na rede gênica, ou seja, um gene conectado a muitos outros, biologicamente importante por sua capacidade de desestabilizar toda a rede se perturbado.

[^scorerewiring]: _Score de rewiring_ — valor numérico que quantifica o quanto um gene alterou suas conexões entre dois estados, calculado como a soma de conexões ganhas e perdidas.

[^condif]: _Conectividade diferencial (Differential Connectivity)_ — diferença no número ou padrão de conexões de um gene entre dois estados biológicos distintos, capturando mudanças de rede além das mudanças de expressão.

[^biomarcador]: _Biomarcador_ — molécula (gene, proteína, etc.) cuja presença ou nível mensurável indica a existência ou o estágio de uma doença.

[^vias]: _Vias moleculares (pathways)_ — sequências de reações bioquímicas dentro da célula que executam funções específicas, frequentemente alteradas em cânceres.

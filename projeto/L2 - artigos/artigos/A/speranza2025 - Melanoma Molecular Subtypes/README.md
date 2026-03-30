# Resumo: Genetic Insight into Expression-Defined Melanoma Subtypes and Network Mechanisms

---

## Metadados

| Campo         | Informação                                                                                                                                                                                                                                          |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**    | Genetic Insight into Expression-Defined Melanoma Subtypes and Network Mechanisms: An in Silico Study                                                                                                                                                |
| **Autores**   | Desirèe Speranza, Mariapia Marafioti, Martina Musarra, Vincenzo Cianci, Cristina Mondello, Maria Francesca Astorino, Mariacarmela Santarpia, Natasha Irrera, Mario Vaccaro, Nicola Silvestris, Concetta Crisafulli, Marco Calabrò, Silvana Briuglia |
| **Filiação**  | Itália (múltiplas instituições)                                                                                                                                                                                                                     |
| **Revista**   | _Genes_ (Basel, MDPI)                                                                                                                                                                                                                               |
| **Ano**       | 2025                                                                                                                                                                                                                                                |
| **Volume**    | 16(12):1428                                                                                                                                                                                                                                         |
| **DOI**       | https://doi.org/10.3390/genes16121428                                                                                                                                                                                                               |
| **PMID**      | 41465101                                                                                                                                                                                                                                            |
| **Publicado** | 30 de novembro de 2025                                                                                                                                                                                                                              |
| **Acesso**    | Acesso aberto (Open Access)                                                                                                                                                                                                                         |

---

## Problema Investigado

### Contexto

O melanoma[^melanoma] é uma doença heterogênea[^heterogeneidade]: embora todos os tumores recebam o mesmo diagnóstico, seus perfis moleculares são muito diferentes. Essa heterogeneidade é um dos principais motivos pelos quais os tratamentos atuais funcionam bem para alguns pacientes e falham em outros.

### A Pergunta de Pesquisa

> **"É possível identificar subtipos moleculares distintos de melanoma baseados em padrões de expressão gênica, e quais mecanismos de rede diferem entre esses subtipos?"**

O objetivo é criar uma classificação por subtipo molecular[^subtipo] refinada do melanoma que possa guiar tratamentos personalizados (medicina de precisão).

---

## Dados Utilizados

| Dataset                 | Fonte              | Conteúdo                                                    |
| ----------------------- | ------------------ | ----------------------------------------------------------- |
| **E-MTAB-6697**[^emtab] | ArrayExpress (EBI) | 194 amostras de tumor de melanoma (microarray[^microarray]) |

- **Critério de seleção:** Dataset público com amostras tumorais de melanoma suficientes para análise de agrupamento.
- **Tipo de análise:** Exclusivamente computacional (_in silico_[^insilico]).

---

## Pipeline / Metodologia

```
╔══════════════════════════════════════════════════════════════════════════╗
║            PIPELINE DO ARTIGO (Speranza et al., Genes 2025)              ║
╚══════════════════════════════════════════════════════════════════════════╝

  ┌──────────────────────────────────────────────────────────────────────┐
  │  PASSO 1: DADOS DE ENTRADA                                           │
  │                                                                      │
  │  E-MTAB-6697: 194 amostras de tumor de melanoma (microarray)        │
  │  Pré-processamento: normalização, controle de qualidade             │
  └───────────────────────────────┬──────────────────────────────────────┘
                                  │
                                  ▼
  ┌──────────────────────────────────────────────────────────────────────┐
  │  PASSO 2: ESTRATIFICAÇÃO — K-MEANS CLUSTERING [^kmeans]              │
  │                                                                      │
  │  K = 3 clusters definidos a partir do perfil de expressão gênica    │
  │  194 amostras divididas em:                                         │
  │    • Cluster A: 51 amostras                                          │
  │    • Cluster B: 52 amostras                                          │
  │    • Cluster C: 59 amostras (+ 32 não classificados)                │
  └───────────────────────────────┬──────────────────────────────────────┘
                                  │
                                  ▼
  ┌──────────────────────────────────────────────────────────────────────┐
  │  PASSO 3: ANÁLISE DE EXPRESSÃO DIFERENCIAL [^deg]                    │
  │                                                                      │
  │  Comparações entre os 3 clusters                                     │
  │  Identificação de genes que definem cada subgrupo                   │
  └───────────────────────────────┬──────────────────────────────────────┘
                                  │
                                  ▼
  ┌──────────────────────────────────────────────────────────────────────┐
  │  PASSO 4: WGCNA [^wgcna] — ANÁLISE DE CO-EXPRESSÃO                  │
  │                                                                      │
  │  Construção de rede de co-expressão gênica pesada                   │
  │  Identificação de módulos (comunidades) de genes co-expressos       │
  │  Correlação dos módulos com características de cada cluster         │
  └───────────────────────────────┬──────────────────────────────────────┘
                                  │
                                  ▼
  ┌──────────────────────────────────────────────────────────────────────┐
  │  PASSO 5: ENRIQUECIMENTO FUNCIONAL [^enrichment]                     │
  │                                                                      │
  │  GO e KEGG para cada cluster                                         │
  │  Identificação de vias compartilhadas e específicas de cada subtipo │
  │  Vias compartilhadas: diferenciação epidérmica, resposta imune,     │
  │                        metabolismo lipídico                          │
  │  Vias divergentes: proliferação, metabolismo, plasticidade          │
  └───────────────────────────────┬──────────────────────────────────────┘
                                  │
                                  ▼
  ┌──────────────────────────────────────────────────────────────────────┐
  │  PASSO 6: AVALIAÇÃO DO IMUNOFENÓTIPO (IPS [^ips])                    │
  │                                                                      │
  │  Todos os clusters: IPS 7–8 (imunologicamente quentes)              │
  │  Implicação: todos podem ser responsivos à imunoterapia             │
  └──────────────────────────────────────────────────────────────────────┘
```

---

## Estratégia de Grafo Utilizada

### Modelo de grafo

**Rede de co-expressão gênica pesada (WGCNA)**:

- **Nós:** genes
- **Arestas:** correlação de Pearson entre pares de genes (pesada — a intensidade da correlação é preservada)
- **Não-direcionada**

### Estratégia central: Identificação de módulos (comunidades)

O WGCNA identifica **módulos de genes** na rede de co-expressão — subgrafos densos onde todos os genes variam juntos. Cada módulo representa um programa biológico coordenado:

1. **Construção da rede:** correlações de Pearson entre todos os pares de genes nas 194 amostras.
2. **Transformação:** correlações são elevadas a uma potência (soft threshold) para criar pesos e aproximar uma rede livre de escala.
3. **Identificação de módulos:** algoritmo de clusterização hierárquica sobre a matriz de sobreposição topológica (TOM) forma os módulos.
4. **Correlação com subtipos:** cada módulo é correlacionado com os 3 clusters (A, B, C) para identificar quais módulos são específicos de cada subtipo.

### Integração com K-Means

O diferencial do artigo é a **combinação de duas estratégias**:

- **K-Means**: clusteriza as _amostras_ com base em seus perfis de expressão → define os subtipos.
- **WGCNA**: clusteriza os _genes_ em módulos e correlaciona os módulos com os subtipos → explica os mecanismos moleculares de cada subtipo.

---

## Resultados Principais

### Três subtipos moleculares de melanoma

| Cluster | Amostras | Perfil Biológico                                                                                                                                             |
| ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **A**   | 51       | Enriquecido em replicação/reparo de DNA e metabolismo mitocondrial → estado _proliferativo genomicamente estável_                                            |
| **B**   | 52       | Ênfase em sinalização imune e citocinas, com menor proliferação → _fenótipo transitório_                                                                     |
| **C**   | 59       | Enriquecimento em ciclo celular, manutenção de DNA e reprogramação neuroectodérmica[^neuroect] → subtipo _altamente plástico[^plasticidade] e proliferativo_ |

### Vias compartilhadas entre todos os clusters

- Diferenciação epidérmica (desregulada)
- Resposta imune
- Metabolismo lipídico

### Imunofenótipo

- Todos os 3 subtipos têm IPS 7–8 → todos "imunologicamente quentes"
- Implicação: todos podem ser candidatos à imunoterapia, mas com diferentes mecanismos

### Limitação principal

Os autores reconhecem que os resultados precisam de **validação em coortes clínicas independentes** com dados de sobrevivência e resposta ao tratamento.

---

## Por que é Relevante para o Projeto sobre Câncer de Pele

### 1. Estratificação molecular como objetivo análogo

O projeto da equipe ALFAK também busca comparar perfis moleculares entre grupos (melanoma, não-melanoma, saudável). A estratégia de K-Means + WGCNA deste artigo é diretamente aplicável para identificar subtipos dentro de cada grupo.

### 2. WGCNA como ferramenta de análise de comunidades

O WGCNA é um método de identificação de **comunidades/módulos** em redes de co-expressão — exatamente o tipo de análise que o projeto planeja realizar com MCODE e clusterMaker2 no Cytoscape.

### 3. Heterogeneidade do melanoma

Este artigo demonstra que "melanoma" não é uma única doença molecular — há ao menos 3 subtipos distintos. Isso tem implicações diretas para o projeto: as redes gênicas de melanoma podem precisar ser analisadas considerando essa heterogeneidade.

### 4. Imunoterapia e dados de expressão

A associação entre subtipos moleculares e responsividade à imunoterapia (IPS) é relevante para o projeto, que inclui análise com dados de TCGA[^tcga]-SKCM (melanoma cutâneo) — coorte que inclui dados de tratamento.

### 5. Validação da abordagem computacional (in silico)

O artigo mostra que análises computacionais com dados públicos podem gerar hipóteses biologicamente plausíveis — validando a metodologia geral do projeto da equipe.

---

## Referência Completa

**ABNT:**
SPERANZA, Desirèe et al. Genetic Insight into Expression-Defined Melanoma Subtypes and Network Mechanisms: An in Silico Study. **Genes**, v. 16, n. 12, p. 1428, 30 nov. 2025. DOI: https://doi.org/10.3390/genes16121428. PMID: 41465101.

**Vancouver:**
Speranza D, Marafioti M, Musarra M, Cianci V, Mondello C, Astorino MF, Santarpia MC, Irrera N, Vaccaro M, Silvestris N, Crisafulli C, Calabrò M, Briuglia S. Genetic Insight into Expression-Defined Melanoma Subtypes and Network Mechanisms: An in Silico Study. Genes (Basel). 2025 Nov 30;16(12):1428. doi: 10.3390/genes16121428. PMID: 41465101.

**APA:**
Speranza, D., Marafioti, M., Musarra, M., Cianci, V., Mondello, C., Astorino, M. F., Santarpia, M. C., Irrera, N., Vaccaro, M., Silvestris, N., Crisafulli, C., Calabrò, M., & Briuglia, S. (2025). Genetic Insight into Expression-Defined Melanoma Subtypes and Network Mechanisms: An in Silico Study. _Genes_, _16_(12), 1428. https://doi.org/10.3390/genes16121428

---

_Resumo elaborado em: 2026-03-29_
_Fonte: PubMed PMID 41465101, MDPI Genes, ArrayExpress E-MTAB-6697_

---

## Notas

[^melanoma]: _Melanoma_ — tipo mais agressivo de câncer de pele, originado nos melanócitos (células produtoras do pigmento da pele); altamente heterogêneo entre pacientes.

[^heterogeneidade]: _Heterogeneidade tumoral_ — o fato de que tumores do mesmo tipo podem ter perfis moleculares muito diferentes entre pacientes e até dentro do mesmo tumor.

[^subtipo]: _Subtipo molecular_ — subgrupo de uma doença definido por um padrão específico de atividade gênica, permitindo classificar pacientes e personalizar tratamentos.

[^emtab]: _E-MTAB-6697_ — dataset público de expressão gênica de 194 amostras de tumor de melanoma disponível no banco ArrayExpress (EBI), principal conjunto de dados do estudo.

[^microarray]: _Microarray_ — tecnologia para medir simultaneamente o nível de expressão (atividade) de milhares de genes em uma amostra biológica.

[^insilico]: _In silico_ — estudo realizado inteiramente por computação, sem experimentos laboratoriais, usando dados públicos e análises bioinformáticas.

[^kmeans]: _K-Means Clustering_ — algoritmo não supervisionado que divide um conjunto de dados em K grupos (clusters) minimizando a distância interna de cada grupo; aqui usado com K=3 para agrupar as amostras de melanoma por perfil de expressão.

[^deg]: _Análise de expressão diferencial_ — identificação de genes com nível de atividade significativamente diferente entre grupos, revelando o que define molecularmente cada subgrupo.

[^wgcna]: _WGCNA (Weighted Gene Co-expression Network Analysis)_ — método que constrói uma rede de co-expressão gênica pesada e identifica módulos (grupos de genes que variam juntos), cada um representando um programa biológico coordenado.

[^enrichment]: _Enriquecimento de vias (pathway enrichment)_ — análise que verifica se genes de uma lista estão concentrados em vias biológicas específicas (GO, KEGG), transformando listas de genes em interpretação biológica.

[^ips]: _IPS (Immunophenoscore)_ — métrica que quantifica o grau de atividade imunológica de um tumor; valores 7–8 indicam tumores "imunologicamente quentes", com maior potencial de resposta à imunoterapia.

[^neuroect]: _Reprogramação neuroectodérmica_ — processo pelo qual células tumorais adquirem características de células do sistema nervoso (mesma origem embrionária dos melanócitos), associado a maior plasticidade e agressividade tumoral.

[^plasticidade]: _Plasticidade celular_ — capacidade de uma célula de mudar seu fenótipo (comportamento e características) em resposta ao ambiente; tumores com alta plasticidade são mais difíceis de tratar.

[^tcga]: _TCGA (The Cancer Genome Atlas)_ — consórcio americano que gerou dados genômicos abrangentes de dezenas de tipos de câncer; TCGA-SKCM é a coorte específica de melanoma cutâneo.

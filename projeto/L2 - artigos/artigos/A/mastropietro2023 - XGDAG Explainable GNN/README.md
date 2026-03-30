# Resumo: XGDAG — Explainable Gene-Disease Associations via Graph Neural Networks

---

## Metadados

| Campo        | Informação                                                             |
| ------------ | ---------------------------------------------------------------------- |
| **Título**   | XGDAG: explainable gene-disease associations via graph neural networks |
| **Autores**  | Andrea Mastropietro, Gianluca De Carlo, Aris Anagnostopoulos           |
| **Filiação** | Sapienza University of Rome, Itália                                    |
| **Revista**  | _Bioinformatics_ (Oxford Academic)                                     |
| **Ano**      | 2023                                                                   |
| **DOI**      | https://doi.org/10.1093/bioinformatics/btad482                         |
| **PMID**     | 37531293                                                               |
| **Acesso**   | Disponível no Oxford Academic e PubMed                                 |

---

## Glossário de Termos Técnicos

> Esta seção explica todos os termos especializados como se o leitor nunca tivesse estudado biologia ou computação avançada.

### Termos de Biologia e Genética

**Gene**
: Trecho do DNA que contém instruções para produzir uma proteína ou realizar uma função na célula. O genoma humano tem cerca de 20.000–25.000 genes.

**Doença (Disease)**
: Qualquer condição que perturba o funcionamento normal do organismo. Neste artigo, o foco são doenças com base genética — causadas (em parte) por alterações em genes específicos.

**Associação Gene-Doença (Gene-Disease Association — GDA)**
: Ligação documentada entre um gene e uma doença. Por exemplo: o gene BRAF está associado ao melanoma, e mutações nele são encontradas em ~50% dos melanomas. O objetivo do artigo é descobrir _novas_ GDAs não documentadas.

**Proteína**
: Molécula fabricada a partir das instruções de um gene. As proteínas realizam a maioria das funções celulares.

**Rede de interação proteína-proteína (PPI)**
: Grafo onde cada nó é uma proteína e cada aresta representa uma interação física ou funcional entre duas proteínas. É a principal fonte de dados estruturais do artigo.

**BioGRID**
: Banco de dados público (https://thebiogrid.org/) que cataloga interações proteína-proteína e gene-gene documentadas em experimentos. Usado como fonte da rede PPI no artigo.

**Positive-Unlabeled Learning (Aprendizado Positivo-Não Rotulado)**
: Estratégia de aprendizado de máquina usada quando só se conhecem os exemplos positivos (GDAs confirmadas) mas não se sabe com certeza quais pares são negativos (NÃO associados). Em vez de assumir que todos os pares sem evidência são negativos, o modelo trata pares sem evidência como "desconhecidos" — uma abordagem mais realista, pois a ausência de evidência não é evidência de ausência.

**Gene candidato**
: Gene identificado computacionalmente como provável associado a uma doença, mas ainda sem confirmação experimental. É uma hipótese a ser testada no laboratório.

**Biomarcador**
: Molécula mensurável que indica presença ou estado de uma doença. Genes hub com alta associação à doença são candidatos a biomarcadores.

**Priorização de genes (Gene Prioritization)**
: O problema de ranquear genes por probabilidade de estar associado a uma doença de interesse. Dado que há ~20.000 genes e só alguns estão associados a uma doença específica, a priorização reduz o espaço de busca para experimentos.

---

### Termos de Computação e IA

**GNN (Graph Neural Network — Rede Neural em Grafo)**
: Tipo de inteligência artificial projetado para operar sobre dados em forma de grafo. Enquanto redes neurais tradicionais recebem tabelas, GNNs recebem diretamente a estrutura do grafo e aprendem padrões nas conexões entre os nós. Aqui, a GNN aprende quais genes são importantes com base na estrutura da rede PPI.

**GraphSAGE (Graph Sample and Aggregate)**
: Uma arquitetura específica de GNN que aprende representações de nós _amostrando e agregando_ informações dos vizinhos. Em vez de processar todos os vizinhos de uma vez (o que é computacionalmente caro em redes grandes), GraphSAGE amostra um subconjunto de vizinhos em cada camada.

Funcionamento em camadas:

1. Cada nó coleta informações de uma amostra de seus vizinhos diretos.
2. Agrega essas informações (ex: média, concatenação).
3. Combina com sua própria representação para formar um novo embedding.
4. Após várias camadas, o embedding captura o contexto de vizinhanças cada vez mais distantes.

Neste artigo são usadas **7 camadas** de GraphSAGE — o gene aprende de vizinhos até 7 "saltos" de distância na rede PPI.

**Embedding (Representação vetorial)**
: Transformação de um nó (gene) em um vetor de números reais que captura suas características e posição na rede. Genes com papéis similares na rede ficam com embeddings similares (próximos no espaço matemático).

**Link Prediction (Predição de Ligação)**
: Tarefa de prever quais pares de nós deveriam ter uma aresta mas não têm. Aqui, é prever quais pares gene-doença provavelmente são associados.

**Explainable AI / XAI (IA Explicável)**
: Área da IA que desenvolve métodos para entender _por que_ um modelo faz uma previsão específica. GNNs são frequentemente "caixas pretas" — sabemos o resultado mas não o motivo. Técnicas de XAI abrem a caixa preta.

**GNNExplainer**
: Método de explicabilidade para GNNs que identifica quais arestas e features do grafo foram mais importantes para a previsão de um nó específico. É como perguntar: "Quais conexões na rede PPI levaram o modelo a classificar este gene como associado à doença?"

**GraphSVX**
: Método de explicabilidade baseado em valores de Shapley (conceito da teoria dos jogos), adaptado para GNNs. Atribui uma "contribuição" a cada nó vizinho para a previsão final.

**SubgraphX**
: Método de explicabilidade que identifica o subgrafo (subconjunto de nós e arestas) mais relevante para a previsão. Revela o contexto local da rede que justifica a classificação de um gene.

**NIAPU (Non-IsolAted Positive-Unlabeled learning)**
: O nome do framework de aprendizado proposto no artigo. Implementa o aprendizado positivo-não rotulado de forma específica para redes PPI, considerando a estrutura de vizinhança dos genes.

**Camada (Layer)**
: Em redes neurais, cada camada processa os dados e os transforma. Com 7 camadas, o GraphSAGE do artigo agrega informações de vizinhos até 7 passos de distância na rede PPI — capturando contexto biológico mais amplo.

**AUC (Area Under the Curve)**
: Métrica de desempenho de classificadores. AUC = 1,0 é perfeito; AUC = 0,5 é equivalente a chute aleatório. Quanto maior, melhor o modelo distingue casos positivos de negativos.

**Priorização não-black-box**
: Uma característica chave do XGDAG: o modelo não apenas ranqueia os genes, mas também explica quais interações na rede PPI sustentam cada previsão. Isso é essencial para pesquisadores que precisam entender _por que_ um gene é candidato.

---

## Problema Investigado

### Contexto

Descobrir quais genes estão associados a doenças é fundamental para desenvolver tratamentos, mas os experimentos laboratoriais são caros e lentos. Há bilhões de pares gene-doença possíveis — a grande maioria nunca foi testada.

Modelos computacionais de GNN[^gnn] já foram usados para prever GDAs[^gda], mas têm dois problemas:

1. **Aprendizado negativo inadequado**: tratam todos os pares sem evidência como "negativos" (não associados), quando na realidade muitos são simplesmente _desconhecidos_.
2. **Caixa preta**: não explicam quais estruturas da rede motivam a previsão, dificultando a confiança dos pesquisadores nos resultados.

### A Solução Proposta (XGDAG)

> **"Usar GraphSAGE[^graphsage] com aprendizado positivo-não rotulado (NIAPU[^niapu]) para priorizar genes candidatos, combinado com métodos de explicabilidade (GNNExplainer[^gnnexplainer], GraphSVX[^graphsvx], SubgraphX[^subgraphx]) para revelar os subgrafos da rede PPI[^ppi] que justificam cada previsão."**

O nome XGDAG vem de: **X**plainable **G**raph-based **D**isease-**A**ssociated **G**enes.

---

## Dados Utilizados

| Fonte                                         | Conteúdo                                       | Papel no Estudo                                    |
| --------------------------------------------- | ---------------------------------------------- | -------------------------------------------------- |
| **BioGRID**[^biogrid]                         | Rede PPI humana (interações proteína-proteína) | Estrutura do grafo — arestas entre genes           |
| **Associações gene-doença** (diversas fontes) | GDAs confirmadas                               | Exemplos positivos para treinamento                |
| **Pares sem evidência**                       | Pares gene-doença não documentados             | Tratados como "desconhecidos" (não como negativos) |

---

## Pipeline / Metodologia

```
╔══════════════════════════════════════════════════════════════════════════╗
║              PIPELINE DO ARTIGO (Mastropietro et al., 2023)              ║
╚══════════════════════════════════════════════════════════════════════════╝

  ┌──────────────────────────────────────────────────────────────────────┐
  │  PASSO 1: CONSTRUÇÃO DO GRAFO PPI                                    │
  │                                                                      │
  │  BioGRID → rede de interação proteína-proteína (PPI)                │
  │  Nós: proteínas/genes humanos                                        │
  │  Arestas: interações documentadas                                    │
  └───────────────────────────────┬──────────────────────────────────────┘
                                  │
                                  ▼
  ┌──────────────────────────────────────────────────────────────────────┐
  │  PASSO 2: DEFINIÇÃO DAS CLASSES (NIAPU)                              │
  │                                                                      │
  │  Positivos (P): genes confirmados como associados à doença          │
  │  Desconhecidos (U): todos os outros (NÃO tratados como negativos)   │
  │  → Aprendizado Positivo-Não Rotulado                                 │
  └───────────────────────────────┬──────────────────────────────────────┘
                                  │
                                  ▼
  ┌──────────────────────────────────────────────────────────────────────┐
  │  PASSO 3: MODELO GNN — GraphSAGE (7 camadas)                        │
  │                                                                      │
  │  Cada gene recebe embedding inicial                                  │
  │  Camada 1: agrega vizinhos diretos (1 salto)                        │
  │  Camada 2: agrega vizinhos de 2 saltos                              │
  │  ...                                                                 │
  │  Camada 7: agrega contexto de 7 saltos de distância                 │
  │  → Embedding final captura contexto amplo da rede PPI               │
  └───────────────────────────────┬──────────────────────────────────────┘
                                  │
                                  ▼
  ┌──────────────────────────────────────────────────────────────────────┐
  │  PASSO 4: CLASSIFICAÇÃO E RANQUEAMENTO                               │
  │                                                                      │
  │  Para cada gene: score de probabilidade de associação à doença      │
  │  Ranquear todos os genes desconhecidos pelo score                   │
  │  Retornar lista priorizada de candidatos                             │
  └───────────────────────────────┬──────────────────────────────────────┘
                                  │
                                  ▼
  ┌──────────────────────────────────────────────────────────────────────┐
  │  PASSO 5: EXPLICABILIDADE (XAI[^xai])                                │
  │                                                                      │
  │  Para cada gene candidato:                                           │
  │    GNNExplainer → arestas mais importantes para a previsão         │
  │    GraphSVX → contribuição de cada vizinho (Shapley)                │
  │    SubgraphX → subgrafo da PPI que justifica a classificação        │
  │                                                                      │
  │  Resultado: "Por que este gene é candidato?"                         │
  │  → subgrafo explicativo mostrando as interações relevantes          │
  └──────────────────────────────────────────────────────────────────────┘
```

---

## Estratégia de Grafo Utilizada

### Modelo de grafo

**Grafo PPI não-direcionado (proteína-proteína)**:

- **Nós:** genes/proteínas humanos (do BioGRID)
- **Arestas:** interações proteína-proteína conhecidas
- **Não tem pesos** — a presença/ausência da interação é binária

### Estratégia central: GraphSAGE com 7 camadas

A chave técnica do artigo é usar **GraphSAGE** (em vez de GCN simples) porque:

1. **Escalabilidade:** GraphSAGE funciona bem em redes grandes como a PPI humana completa, pois amostra vizinhos em vez de processar todos.
2. **Generalização:** É projetado para generalizar para nós novos (genes não vistos durante o treinamento).
3. **Profundidade:** Com 7 camadas, captura o contexto de vizinhanças extensas — biologicamente relevante, pois genes distantes na rede PPI podem compartilhar funções.

### Estratégia secundária: Explicabilidade com subgrafos

O diferencial principal é que cada previsão vem acompanhada de um **subgrafo explicativo** — um subconjunto da rede PPI que "justifica" a classificação. Isso permite que um pesquisador entenda: "Este gene foi classificado como candidato porque interage com os genes X, Y e Z, que já são conhecidos como envolvidos na doença."

---

## Resultados Principais

- XGDAG **supera métodos existentes** de priorização de genes em benchmarks padrão
- A abordagem NIAPU (positivo-não rotulado) é superior ao uso de negativos aleatórios
- Os **subgrafos explicativos** revelam mecanismos biológicos plausíveis para cada candidato
- O modelo é eficaz mesmo ao recuperar grandes números de genes candidatos — onde métodos tradicionais falham
- Combinar 3 métodos de XAI (GNNExplainer, GraphSVX, SubgraphX) dá maior robustez às explicações

---

## Por que é Relevante para o Projeto sobre Câncer de Pele

### 1. Priorização de genes de melanoma

O framework XGDAG pode ser aplicado especificamente para priorizar genes candidatos em melanoma — inserindo as GDAs conhecidas do melanoma como positivos e usando a rede PPI do STRING/BioGRID.

### 2. Explicabilidade como validação

Em um projeto de análise de redes gênicas, saber _por que_ um gene é um hub[^hub] é tão importante quanto saber _que_ ele é um hub. Os subgrafos explicativos do XGDAG complementam métricas de centralidade como betweenness e eigenvector centrality.

### 3. Aprendizado com dados incompletos

Os dados de câncer de pele são incompletos: muitas associações ainda não foram documentadas. O NIAPU é ideal para esse cenário — evita penalizar o modelo por "não associações" que podem ser simplesmente desconhecidas.

### 4. Integração com redes PPI (STRING)

O projeto usa STRING para construir redes PPI. O XGDAG opera sobre esse mesmo tipo de rede, tornando os dois trabalhos diretamente comparáveis e complementares.

### 5. Deep learning sobre grafos

O projeto planeja usar Graph Attention Networks (GAT). XGDAG usa GraphSAGE — ambas são arquiteturas de GNN. O artigo fornece um modelo de como aplicar GNNs a dados de doenças genéticas, incluindo estratégias de validação e interpretação.

---

## Referência Completa

**ABNT:**
MASTROPIETRO, Andrea; DE CARLO, Gianluca; ANAGNOSTOPOULOS, Aris. XGDAG: explainable gene-disease associations via graph neural networks. **Bioinformatics**, v. 39, n. 8, p. btad482, 2023. DOI: https://doi.org/10.1093/bioinformatics/btad482. PMID: 37531293.

**Vancouver:**
Mastropietro A, De Carlo G, Anagnostopoulos A. XGDAG: explainable gene-disease associations via graph neural networks. Bioinformatics. 2023;39(8):btad482. doi: 10.1093/bioinformatics/btad482. PMID: 37531293.

**APA:**
Mastropietro, A., De Carlo, G., & Anagnostopoulos, A. (2023). XGDAG: explainable gene-disease associations via graph neural networks. _Bioinformatics_, _39_(8), btad482. https://doi.org/10.1093/bioinformatics/btad482

---

## Notas

[^gnn]: _GNN (Graph Neural Network)_ — Tipo de inteligência artificial projetado para operar sobre dados em forma de grafo, aprendendo padrões nas conexões entre nós.

[^gda]: _GDA (Gene-Disease Association)_ — Ligação documentada entre um gene e uma doença; o objetivo do artigo é descobrir novas GDAs não documentadas.

[^graphsage]: _GraphSAGE (Graph Sample and Aggregate)_ — Arquitetura de GNN que aprende representações de nós amostrando e agregando informações dos vizinhos em múltiplas camadas.

[^niapu]: _NIAPU (Non-IsolAted Positive-Unlabeled learning)_ — Framework de aprendizado proposto no artigo que implementa o aprendizado positivo-não rotulado considerando a estrutura de vizinhança dos genes na rede PPI.

[^gnnexplainer]: _GNNExplainer_ — Método de explicabilidade para GNNs que identifica quais arestas e features do grafo foram mais importantes para a previsão de um nó específico.

[^graphsvx]: _GraphSVX_ — Método de explicabilidade baseado em valores de Shapley adaptado para GNNs, atribuindo uma "contribuição" a cada nó vizinho para a previsão final.

[^subgraphx]: _SubgraphX_ — Método de explicabilidade que identifica o subgrafo (subconjunto de nós e arestas) mais relevante para justificar a classificação de um gene.

[^ppi]: _PPI (Protein-Protein Interaction — Rede de interação proteína-proteína)_ — Grafo onde cada nó é uma proteína e cada aresta representa uma interação física ou funcional entre duas proteínas.

[^biogrid]: _BioGRID_ — Banco de dados público que cataloga interações proteína-proteína e gene-gene documentadas em experimentos, usado como fonte da rede PPI no artigo.

[^xai]: _XAI (Explainable AI — IA Explicável)_ — Área da IA que desenvolve métodos para entender por que um modelo faz uma previsão específica, abrindo a "caixa preta" das GNNs.

[^hub]: _Hub_ — Gene ou proteína muito conectado na rede, analogamente a uma estação central de metrô; indica alta relevância funcional na rede PPI.

---

_Resumo elaborado em: 2026-03-29_
_Fonte: PubMed PMID 37531293, Oxford Bioinformatics_

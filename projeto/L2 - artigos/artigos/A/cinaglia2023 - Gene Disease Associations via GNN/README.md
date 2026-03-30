# Resumo: Identifying Candidate Gene–Disease Associations via Graph Neural Networks

---

## Metadados

| Campo        | Informação                                                                                                    |
| ------------ | ------------------------------------------------------------------------------------------------------------- |
| **Título**   | Identifying Candidate Gene–Disease Associations via Graph Neural Networks                                     |
| **Autores**  | Pietro Cinaglia, Mario Cannataro                                                                              |
| **Filiação** | Department of Health Sciences & Data Analytics Research Center, Magna Graecia University of Catanzaro, Itália |
| **Revista**  | _Entropy_ (MDPI)                                                                                              |
| **Ano**      | 2023                                                                                                          |
| **Volume**   | 25, Número 6, Artigo 909                                                                                      |
| **DOI**      | https://doi.org/10.3390/e25060909                                                                             |
| **PMID**     | 37372253                                                                                                      |
| **PMC ID**   | PMC10296901                                                                                                   |
| **Acesso**   | Acesso aberto (Open Access)                                                                                   |
| **GitHub**   | https://github.com/pietrocinaglia/gnn_gda                                                                     |

---

## Glossário de Termos Técnicos

> Esta seção explica todos os termos especializados como se o leitor nunca tivesse estudado biologia ou computação avançada.

### Termos de Biologia e Genética

**Gene**
: Um trecho do DNA que contém as instruções para fabricar uma proteína ou realizar uma função específica no organismo. Pense no gene como uma "receita" dentro do manual de instruções do corpo (o genoma).

**Doença (disease)**
: Qualquer condição que perturba o funcionamento normal do organismo. Neste artigo, o foco é em doenças com base genética — ou seja, causadas (ao menos em parte) por variações em genes.

**Gene–Disease Association (GDA) — Associação Gene–Doença**
: A ligação documentada entre um gene específico e uma doença específica. Por exemplo, o gene BRCA1 está associado ao câncer de mama: mutações nesse gene aumentam o risco da doença. O objetivo do artigo é descobrir _novas_ associações que ainda não foram documentadas.

**Candidato gene-doença (candidate GDA)**
: Uma associação prevista por computador, mas ainda não confirmada experimentalmente. É uma "hipótese" gerada pela IA que pesquisadores podem depois testar no laboratório.

**Proteína**
: Molécula fabricada a partir das instruções de um gene. As proteínas fazem a maior parte do "trabalho" nas células (estrutura, transporte, sinalização, defesa imunológica, etc.).

**Interação gene–gene**
: Quando dois genes influenciam mutuamente sua atividade. Isso cria redes complexas dentro da célula.

**DisGeNET**
: Banco de dados público que reúne associações entre genes e doenças coletadas da literatura científica, de experimentos clínicos e de bancos de dados curados manualmente. É como uma "enciclopédia" das relações gene-doença já conhecidas. URL: https://www.disgenet.org/

**DG-AssocMiner (BioSNAP/Stanford)**
: Outro banco de dados de associações gene-doença, desenvolvido pela Universidade de Stanford, usado neste artigo para validação externa do modelo.

**AUC (Area Under the Curve — Área Sob a Curva)**
: Métrica usada para avaliar modelos de classificação. Vai de 0 a 1 (ou 0% a 100%). Um AUC de 95% significa que em 95% das vezes o modelo consegue distinguir corretamente um par gene-doença verdadeiro de um par falso. É como uma nota escolar: 95% é excelente.

**Top-15**
: As 15 associações gene-doença com maior "pontuação de confiança" previstas pelo modelo para uma determinada doença. O artigo testou se essas previsões tinham base na literatura científica.

---

### Termos de Computação e IA

**Grafo (Graph)**
: Estrutura matemática formada por **nós** (pontos) conectados por **arestas** (linhas). Exemplos do cotidiano: mapa de metrô (estações = nós, trilhos = arestas), rede social (pessoas = nós, amizades = arestas). Em biologia, usa-se grafos para representar redes de interação entre genes, proteínas e doenças.

**Nó (Node / Vertex)**
: Um ponto do grafo que representa uma entidade. Neste artigo, os nós representam **genes** ou **doenças**.

**Aresta (Edge / Link)**
: A linha que conecta dois nós no grafo. Aqui, uma aresta entre um gene e uma doença representa uma associação documentada entre eles. Arestas também conectam genes a genes (interações) e doenças a doenças (comorbidades).

**Rede Heterogênea (Heterogeneous Network)**
: Grafo que contém mais de um tipo de nó e/ou mais de um tipo de aresta. Neste artigo, a rede tem dois tipos de nó (gene e doença) e múltiplos tipos de aresta.

**GNN (Graph Neural Network — Rede Neural em Grafo)**
: Um tipo de inteligência artificial projetado especificamente para processar dados em forma de grafo. Enquanto redes neurais tradicionais recebem uma tabela de números, a GNN recebe diretamente a estrutura do grafo e aprende padrões nas conexões entre os nós.

**Graph Convolutional Network (GCN) — Rede Convolucional em Grafo**
: Um tipo específico de GNN que aplica operações matemáticas chamadas "convoluções" sobre o grafo. Inspirada nas redes neurais convolucionais usadas para reconhecer imagens, a GCN "varre" a vizinhança de cada nó para aprender sua representação.

**Convolução (convolution)**
: Operação matemática que "mescla" a informação de um nó com a informação de seus vizinhos. Em imagens, uma convolução detecta bordas e texturas; em grafos, detecta padrões de conectividade. Neste artigo, múltiplas camadas de convolução são empilhadas para capturar vizinhanças cada vez mais distantes.

**Embedding (Incorporação / Representação Vetorial)**
: A transformação de um nó (por exemplo, um gene) em um vetor de números reais (como `[0.3, -1.2, 0.8, ...]`) que captura suas características e posição na rede. É como dar um "código de identidade numérico" a cada gene ou doença, de forma que genes com funções parecidas tenham vetores parecidos.

**Espaço multidimensional (multidimensional space)**
: Um espaço matemático com muitas "dimensões" (eixos). Cada embedding existe nesse espaço. Nós parecidos ficam "próximos" nesse espaço, e o modelo aprende a medir essa proximidade.

**Link Prediction (Predição de Ligação)**
: Tarefa de prever quais pares de nós _deveriam_ ter uma aresta, mas ainda não a têm no grafo observado. Aqui, é prever quais pares gene-doença _provavelmente_ são associados, mesmo sem evidência experimental ainda.

**Amostragem Negativa (Negative Sampling)**
: Para treinar o modelo, é preciso mostrar exemplos de pares gene-doença que _não_ são associados (exemplos negativos), além dos que são (exemplos positivos). A amostragem negativa é o processo de selecionar aleatoriamente esses "não-pares" para treino.

**Função de Ativação ReLU (Rectified Linear Unit)**
: Função matemática simples aplicada após cada camada da rede neural: se o valor é negativo, vira zero; se positivo, permanece igual. Introduz não-linearidade no modelo, permitindo aprender padrões complexos.

**Matriz de Peso (Weight Matrix)**
: Conjunto de parâmetros que a rede neural aprende durante o treinamento. Representa o "conhecimento" adquirido. Durante o pré-processamento, a topologia do grafo (quem está conectado a quem) é usada para inicializar essas matrizes.

**Treinamento / Validação / Teste (Train / Validation / Test)**
: Divisão padrão dos dados em machine learning:

- _Treinamento_: dados usados para o modelo aprender.
- _Validação_: dados usados para ajustar hiperparâmetros e evitar super-aprendizado (_overfitting_).
- _Teste_: dados guardados para avaliação final imparcial do desempenho.

**Overfitting (Super-ajuste)**
: Quando um modelo aprende tão bem os dados de treinamento que "decora" os exemplos em vez de aprender regras gerais, e passa a falhar em dados novos.

**Bioinformática**
: Área que combina biologia, ciência da computação e estatística para analisar dados biológicos (genomas, proteínas, redes moleculares). Este artigo é um trabalho de bioinformática.

---

## Problema Investigado

### Contexto

Doenças complexas (câncer, diabetes, Alzheimer, etc.) raramente são causadas por um único gene. Em geral, resultam da interação de dezenas ou centenas de genes[^gene] com fatores ambientais. Identificar quais genes contribuem para uma doença específica é fundamental para:

- Desenvolver novos medicamentos direcionados a alvos moleculares específicos.
- Identificar biomarcadores para diagnóstico precoce.
- Compreender os mecanismos moleculares da doença.

### O problema

Os experimentos laboratoriais para identificar novas associações gene-doença são **caros, lentos e trabalhosos**. Existem milhares de genes e milhares de doenças catalogadas, formando um espaço de bilhões de pares possíveis. A maioria nunca foi testada experimentalmente.

A pergunta central do artigo é:

> **"É possível usar uma GNN[^gnn] para prever automaticamente, a partir de uma rede de associações conhecidas, quais outros genes provavelmente estão associados a uma determinada doença?"**

O objetivo não é substituir os experimentos, mas **priorizar** quais pares gene-doença merecem investigação laboratorial, reduzindo enormemente o espaço de busca.

---

## Dados Utilizados

### Fonte principal: DisGeNET[^disgenet]

- **O que é:** Banco de dados público e curado que agrega associações gene-doença de múltiplas fontes (artigos científicos, bases clínicas, OMIM, UniProt, etc.).
- **Conteúdo usado:** Conjunto de GDAs[^gda] bem estabelecidas (alta confiança), incluindo relações gene-gene e doença-doença.
- **Papel no estudo:** Treinamento e teste do modelo GNN.

### Fonte de validação externa: DG-AssocMiner (BioSNAP[^biosnap], Stanford)

- **O que é:** Dataset de associações gene-doença do projeto BioSNAP da Universidade de Stanford.
- **Papel no estudo:** Avaliação de desempenho do modelo em dados completamente independentes, para confirmar que os resultados não são específicos do DisGeNET.

### Estrutura dos dados (grafo construído)

A partir dessas fontes, foi construído um **grafo heterogêneo**[^grafo] com:

| Tipo de nó | O que representa                   |
| ---------- | ---------------------------------- |
| Gene       | Cada gene humano presente nas GDAs |
| Doença     | Cada doença presente nas GDAs      |

| Tipo de aresta | O que representa                                     |
| -------------- | ---------------------------------------------------- |
| Gene–Doença    | Associação documentada entre gene e doença           |
| Gene–Gene      | Interação ou co-expressão entre dois genes           |
| Doença–Doença  | Comorbidade ou similaridade fenotípica entre doenças |

---

## Pipeline / Metodologia

```
╔══════════════════════════════════════════════════════════════════════╗
║              PIPELINE DO ARTIGO (Cinaglia & Cannataro, 2023)         ║
╚══════════════════════════════════════════════════════════════════════╝

  ┌─────────────────────────────────────────────────────────────────┐
  │  PASSO 1: COLETA E PREPARAÇÃO DOS DADOS                         │
  │                                                                  │
  │  DisGeNET ──► GDAs conhecidas (gene↔doença)                    │
  │  BioSNAP  ──► GDAs para validação externa                      │
  │                                                                  │
  │  Arestas positivas: pares gene-doença confirmados               │
  │  Arestas negativas: pares gene-doença aleatórios (não confirm.) │
  └───────────────────────────┬─────────────────────────────────────┘
                              │
                              ▼
  ┌─────────────────────────────────────────────────────────────────┐
  │  PASSO 2: CONSTRUÇÃO DO GRAFO HETEROGÊNEO                       │
  │                                                                  │
  │  Nós: genes + doenças                                           │
  │  Arestas: gene-doença / gene-gene / doença-doença               │
  │                                                                  │
  │  Representação matricial: Matriz de adjacência A                │
  └───────────────────────────┬─────────────────────────────────────┘
                              │
                              ▼
  ┌─────────────────────────────────────────────────────────────────┐
  │  PASSO 3: PRÉ-PROCESSAMENTO                                     │
  │                                                                  │
  │  Aprendizado da matriz de pesos a partir da topologia do grafo  │
  │  Inicialização dos embeddings[^embedding] dos nós                           │
  └───────────────────────────┬─────────────────────────────────────┘
                              │
                              ▼
  ┌─────────────────────────────────────────────────────────────────┐
  │  PASSO 4: MODELO GNN (Graph Convolutional Network)              │
  │                                                                  │
  │  Camada Conv 1: embedding inicial + vizinhos de 1ª ordem       │
  │       ▼  ReLU (ativação não-linear)                             │
  │  Camada Conv 2: agrega vizinhos de 2ª ordem                    │
  │       ▼  ReLU                                                   │
  │  ... (múltiplas camadas convolucionais)                         │
  │       ▼                                                         │
  │  Embedding final: vetor numérico para cada nó                  │
  └───────────────────────────┬─────────────────────────────────────┘
                              │
                              ▼
  ┌─────────────────────────────────────────────────────────────────┐
  │  PASSO 5: PREDIÇÃO DE LIGAÇÕES (Link Prediction[^linkprediction])               │
  │                                                                  │
  │  Para cada par (gene X, doença Y):                              │
  │    Score = f(embedding[X], embedding[Y])                        │
  │    Score alto → provável associação                             │
  │    Score baixo → improvável associação                          │
  └───────────────────────────┬─────────────────────────────────────┘
                              │
                              ▼
  ┌─────────────────────────────────────────────────────────────────┐
  │  PASSO 6: TREINAMENTO / VALIDAÇÃO / TESTE                       │
  │                                                                  │
  │  Divisão dos dados em conjuntos de treino, validação e teste    │
  │  Otimização dos pesos da rede para maximizar AUC                │
  └───────────────────────────┬─────────────────────────────────────┘
                              │
                              ▼
  ┌─────────────────────────────────────────────────────────────────┐
  │  PASSO 7: GERAÇÃO DE CANDIDATOS                                 │
  │                                                                  │
  │  Para uma doença alvo: ranquear todos os genes pelo score       │
  │  Retornar Top-15 genes candidatos como novas GDAs              │
  │  Verificar na literatura se os candidatos têm suporte           │
  └─────────────────────────────────────────────────────────────────┘
```

---

## Estratégia de Grafo Utilizada

### Tipo de rede

**Grafo heterogêneo não-direcionado**, ou seja:

- Contém dois tipos de nós (genes e doenças).
- As arestas não têm direção (a associação gene-doença é simétrica para fins do modelo).
- Múltiplos tipos de aresta (gene-doença, gene-gene, doença-doença).

### Nós

- **Genes humanos**: cada gene presente nas GDAs do DisGeNET é um nó.
- **Doenças**: cada doença catalogada no DisGeNET é um nó.

### Arestas

- **Gene ↔ Doença**: associação direta documentada (aresta principal de interesse).
- **Gene ↔ Gene**: interações moleculares entre genes (co-expressão, regulação, etc.).
- **Doença ↔ Doença**: relacionamento entre doenças (comorbidade, fenótipo semelhante).

### Algoritmo central: Graph Convolutional Network (GCN)[^gcn]

A GCN opera da seguinte forma:

1. **Inicialização**: cada nó recebe um embedding inicial (vetor de características).
2. **Agregação**: em cada camada, o embedding de um nó é atualizado combinando seu próprio embedding com os embeddings de seus vizinhos diretos (multiplicação pela matriz de adjacência normalizada + matriz de pesos).
3. **Ativação**: aplicação da função ReLU para introduzir não-linearidade.
4. **Profundidade**: com múltiplas camadas, o nó captura informações de vizinhos cada vez mais distantes na rede.
5. **Predição**: o score de uma associação gene-doença é calculado a partir do produto interno (ou similaridade de cosseno) entre os embeddings finais do gene e da doença.

### Pré-processamento específico

Um passo de pré-processamento aprende a **matriz de pesos** a partir da topologia do grafo antes do treinamento principal. Isso permite que o modelo incorpore informações estruturais do grafo desde o início.

---

## Resultados Principais

| Métrica               | Resultado |
| --------------------- | --------- |
| AUC (treino)          | 95%       |
| AUC (validação)       | 95%       |
| AUC (teste)           | 95%       |
| Taxa de acerto Top-15 | 93%       |

### Interpretação

- **AUC[^auc] de 95%** em todos os conjuntos (treino, validação e teste) indica que o modelo:
  1. Aprendeu bem os padrões — sem overfitting[^overfitting] (o desempenho se manteve nos dados de teste).
  2. Generaliza para dados não vistos.

- **93% de acerto no Top-15**: Para doenças conhecidas, 93% dos 15 genes mais bem ranqueados pelo modelo têm suporte na literatura científica — ou seja, já foram mencionados como relacionados àquela doença em algum estudo.

- O modelo foi validado tanto no **DisGeNET** (dado de treinamento) quanto no **DG-AssocMiner/BioSNAP** (dado externo independente), confirmando robustez.

---

## Por que é Relevante para um Projeto sobre Redes Gênicas em Câncer de Pele

Este artigo é diretamente relevante para pesquisa em redes gênicas no contexto do câncer de pele (melanoma e carcinomas) pelos seguintes motivos:

### 1. Metodologia transferível diretamente

A abordagem GNN apresentada pode ser **aplicada diretamente** a um grafo de interações gênicas em câncer de pele:

- Substituir ou enriquecer o DisGeNET com dados específicos de câncer de pele (melanoma, carcinoma basocelular, carcinoma espinocelular).
- Usar interações proteína[^proteina]-proteína de bancos como STRING para construir as arestas gene-gene.
- Usar dados de expressão gênica de tumores cutâneos (ex: TCGA-SKCM) como features dos nós.

### 2. Descoberta de novos alvos terapêuticos

Em câncer de pele, muitos genes já são conhecidos (BRAF, NRAS, TP53, CDKN2A, etc.), mas a rede de interações ao redor deles é vasta e pouco explorada. Um modelo GNN pode:

- Identificar genes candidatos ainda não associados ao melanoma que interagem com genes-chave já conhecidos.
- Priorizar alvos para novos inibidores ou para terapia combinada.

### 3. Redes heterogêneas para integração de dados multi-ômicos

O framework heterogêneo (gene + doença + relações múltiplas) é ideal para integrar diferentes camadas de dados biológicos de câncer de pele:

- Dados genômicos (mutações somáticas).
- Dados transcriptômicos (expressão gênica diferencial em tumor vs. pele normal).
- Dados de metilação do DNA.
- Dados clínicos (estadiamento, resposta a imunoterapia).

### 4. Resistência a tratamentos

O câncer de pele com frequência desenvolve resistência ao vemurafenibe (inibidor de BRAF) e a inibidores de checkpoint imunológico. A predição de GDAs pode revelar rotas de sinalização alternativas que o tumor usa para escapar dos tratamentos.

### 5. Reprodutibilidade e open source

O código está disponível no GitHub (https://github.com/pietrocinaglia/gnn_gda), facilitando a adaptação do pipeline para dados específicos de câncer de pele.

### 6. Integração com bancos de dados de câncer

Os bancos utilizados (DisGeNET, BioSNAP) contêm dados específicos de cânceres cutâneos, tornando a replicação do estudo com foco em melanoma direta.

---

## Referência Completa

**ABNT:**
CINAGLIA, Pietro; CANNATARO, Mario. Identifying Candidate Gene–Disease Associations via Graph Neural Networks. **Entropy**, v. 25, n. 6, p. 909, 7 jun. 2023. DOI: https://doi.org/10.3390/e25060909. PMID: 37372253. PMC: PMC10296901.

**Vancouver:**
Cinaglia P, Cannataro M. Identifying Candidate Gene–Disease Associations via Graph Neural Networks. Entropy. 2023 Jun 7;25(6):909. doi: 10.3390/e25060909. PMID: 37372253; PMCID: PMC10296901.

**APA:**
Cinaglia, P., & Cannataro, M. (2023). Identifying Candidate Gene–Disease Associations via Graph Neural Networks. _Entropy_, _25_(6), 909. https://doi.org/10.3390/e25060909

---

## Nota sobre o PDF

O PDF completo do artigo está disponível gratuitamente em:

- **PubMed Central:** https://pmc.ncbi.nlm.nih.gov/articles/PMC10296901/pdf/
- **MDPI (editora):** https://www.mdpi.com/1099-4300/25/6/909/pdf

Para baixar o PDF via terminal:

```bash
wget "https://pmc.ncbi.nlm.nih.gov/articles/PMC10296901/pdf/" \
     -O /home/paulo/Workspace/ciencia_saude/artigos/A/cinaglia2023-gene-disease-gnn.pdf \
     --user-agent="Mozilla/5.0 (X11; Linux x86_64)"
```

---

_Resumo elaborado em: 2026-03-29_
_Fontes: PubMed (PMID 37372253), PMC (PMC10296901), MDPI Entropy, GitHub pietrocinaglia/gnn_gda_

---

## Notas

[^gene]: _Gene_ — trecho do DNA que contém as instruções para fabricar uma proteína ou realizar uma função celular; funciona como uma "receita" no manual de instruções do organismo.

[^gnn]: _GNN (Graph Neural Network)_ — tipo de inteligência artificial projetado para processar dados em forma de grafo, aprendendo padrões nas conexões entre os nós.

[^disgenet]: _DisGeNET_ — banco de dados público que agrega associações gene-doença coletadas da literatura científica, experimentos clínicos e bases curadas; disponível em https://www.disgenet.org/.

[^gda]: _GDA (Gene–Disease Association)_ — ligação documentada entre um gene específico e uma doença específica; o objetivo do artigo é prever novas GDAs ainda não confirmadas experimentalmente.

[^biosnap]: _BioSNAP (DG-AssocMiner / Stanford)_ — dataset de associações gene-doença desenvolvido pela Universidade de Stanford, utilizado como fonte de validação externa e independente do modelo.

[^grafo]: _Grafo heterogêneo_ — estrutura matemática com nós (pontos) conectados por arestas (linhas) que contém mais de um tipo de nó e/ou aresta; aqui, representa genes e doenças com múltiplos tipos de relação entre eles.

[^embedding]: _Embedding (Representação Vetorial)_ — transformação de um nó (ex.: um gene) em um vetor de números reais que captura suas características e posição na rede, permitindo ao modelo medir similaridades.

[^linkprediction]: _Link Prediction (Predição de Ligação)_ — tarefa de prever quais pares de nós deveriam ter uma aresta no grafo mas ainda não a possuem; aqui, identifica pares gene-doença provavelmente associados sem evidência experimental prévia.

[^gcn]: _GCN (Graph Convolutional Network)_ — tipo específico de GNN que aplica convoluções sobre o grafo, "varrendo" a vizinhança de cada nó para aprender sua representação vetorial.

[^auc]: _AUC (Area Under the Curve)_ — métrica de avaliação de modelos de classificação que vai de 0 a 1; um AUC de 95% significa que em 95% das vezes o modelo distingue corretamente um par gene-doença verdadeiro de um falso.

[^overfitting]: _Overfitting (Super-ajuste)_ — quando um modelo "decora" os dados de treinamento em vez de aprender regras gerais, perdendo desempenho em dados novos.

[^proteina]: _Proteína_ — molécula fabricada a partir das instruções de um gene; realiza a maior parte do trabalho nas células (estrutura, transporte, sinalização, defesa imunológica, etc.).

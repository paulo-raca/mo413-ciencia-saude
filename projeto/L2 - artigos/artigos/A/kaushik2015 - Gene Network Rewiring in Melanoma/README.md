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

## Glossário de Termos Técnicos

> Esta seção explica todos os termos especializados como se o leitor nunca tivesse estudado biologia ou computação avançada.

### Termos de Biologia e Genética

**Melanoma**
: Tipo mais agressivo de câncer de pele, originado dos melanócitos (células que produzem o pigmento da pele, a melanina). É altamente invasivo e tende a se espalhar para outros órgãos (metástase).

**Melanócito**
: Célula especializada presente na camada profunda da pele que produz melanina, o pigmento responsável pela cor da pele. Quando esse tipo de célula sofre mutações e começa a crescer de forma descontrolada, origina o melanoma.

**Estágios do melanoma (progressão)**
: O melanoma não surge de uma vez — ele evolui gradualmente por estágios:

- **N (Normal)**: pele saudável com melanócitos normais.
- **CnM (Cutaneous non-Metastatic)**: melanoma na pele ainda sem metástase. É o estágio inicial do tumor.
- **CM (Cutaneous Metastatic)**: o tumor cresceu e já tem células que migraram para outras partes da pele (metástase cutânea).
- **LN (Lymph Node Metastatic)**: as células cancerígenas chegaram aos linfonodos (glândulas do sistema imunológico) e podem atingir outros órgãos.

**Gene**
: Trecho do DNA que carrega instruções para produzir uma proteína ou realizar alguma função celular. O ser humano tem cerca de 20.000–25.000 genes.

**Expressão gênica**
: O "nível de atividade" de um gene — quanto aquele gene está sendo lido e executado pela célula para produzir sua proteína. Um gene pode estar muito ativo (expresso), pouco ativo ou silenciado.

**Gene Diferencialmente Expresso (DE gene / DEG)**
: Um gene que tem nível de atividade significativamente diferente entre duas condições (ex: tecido saudável vs. tumor). É como comparar o volume do rádio em duas situações: genes DE são os que estão muito mais alto ou mais baixo em uma condição.

**Microarray**
: Tecnologia laboratorial que mede simultaneamente o nível de expressão de milhares de genes em uma amostra de tecido. É como tirar uma "fotografia" da atividade de todos os genes de uma vez.

**Proteína**
: Molécula fabricada seguindo as instruções de um gene. Proteínas executam a maioria das funções celulares: estrutura, transporte, defesa, sinalização.

**Gene PRAME**
: Gene altamente expresso em melanomas. O nome vem de "Preferentially Expressed Antigen in Melanoma" (antígeno preferencialmente expresso em melanoma). É um dos mais conhecidos biomarcadores de melanoma.

**Família MAGE (MAGEA1, MAGEA12)**
: Família de genes normalmente silenciados em tecidos adultos normais, mas reativados em células tumorais. São usados como marcadores de tumor.

**IL8 (Interleucina 8)**
: Proteína sinalizadora do sistema imunológico (uma citocina) que promove inflamação e pode ajudar tumores a crescerem e se espalharem.

**VEGFA**
: Gene que codifica o fator de crescimento vascular endotelial A — estimula a formação de novos vasos sanguíneos (angiogênese), processo que tumores usam para se alimentar e crescer.

**Homeostase celular**
: Estado de equilíbrio normal de uma célula, no qual todos os processos funcionam dentro de limites saudáveis.

**Interactoma**
: O conjunto completo de interações moleculares dentro de uma célula — como todas as proteínas e genes se "conversam" entre si.

**Biomarcador**
: Molécula (gene, proteína, etc.) cuja presença ou nível pode indicar a existência ou o estágio de uma doença. É como um "sinal de alerta" mensurável do organismo.

**Vias moleculares (pathways)**
: Sequências de reações bioquímicas dentro da célula que executam funções específicas (ex: dividir a célula, responder a sinais externos, reparar o DNA). O câncer frequentemente altera essas vias.

---

### Termos de Computação e Redes

**Grafo / Rede**
: Estrutura matemática composta por **nós** (pontos) conectados por **arestas** (linhas). Em biologia, usamos grafos para representar redes de genes: cada gene é um nó, e uma aresta entre dois genes significa que eles se co-expressam (têm padrões de atividade correlacionados).

**Rede de co-expressão gênica**
: Grafo onde dois genes são conectados se seus níveis de expressão variam de forma semelhante em diferentes amostras. Se sempre que o gene A está alto, o gene B também está, eles provavelmente fazem parte de um mesmo processo biológico.

**Correlação de Pearson**
: Medida estatística que varia de −1 a +1 e quantifica o quanto dois conjuntos de dados variam juntos. +1 = variam perfeitamente iguais; −1 = variam em sentidos opostos; 0 = sem relação. É usada aqui para medir se dois genes têm expressão correlacionada.

**Grau (Degree)**
: Em uma rede, o grau de um nó é o número de arestas (conexões) que ele possui. Um gene com grau alto está conectado a muitos outros genes — é um hub.

**Hub (gene hub)**
: Nó de altíssimo grau na rede — um gene que interage com muitos outros. Hubs são biologicamente importantes porque interrompê-los pode desestabilizar toda a rede. Em cânceres, hubs frequentemente são genes-chave do tumor.

**Conectividade diferencial (Differential Connectivity)**
: A diferença no número ou no padrão de conexões de um gene entre dois estados (ex: saudável vs. tumoral). Um gene pode ter a mesma expressão nos dois estados, mas ter conexões completamente diferentes — isso é o "rewiring" (re-fiação).

**Rewiring de rede (Network Rewiring)**
: Mudança nas conexões de uma rede gênica de um estado para outro. Pense como uma planta elétrica que é re-fiada: o mesmo fio (gene) pode agora estar ligado a tomadas diferentes (novos parceiros moleculares), mesmo que a quantidade de corrente que passa por ele não tenha mudado.

**Score de rewiring**
: Valor numérico que quantifica o quanto um gene "re-fiou" suas conexões entre dois estados. Calculado como: número de conexões ganhas + número de conexões perdidas entre os dois estados.

**Meta-análise**
: Técnica que combina os resultados de múltiplos estudos independentes para aumentar o tamanho amostral e a confiabilidade das conclusões. Aqui, foram combinados dados de 642 amostras de múltiplos estudos publicados.

**ComBat (batch correction)**
: Método estatístico para remover o "efeito de lote" — variações técnicas que surgem quando dados são produzidos em laboratórios ou plataformas diferentes. Sem essa correção, diferenças técnicas podem mascarar diferenças biológicas reais.

**Rede livre de escala (Scale-free network)**
: Tipo de rede onde poucos nós têm muitas conexões (hubs) e a maioria tem poucas. A distribuição dos graus segue uma lei de potência. Redes biológicas (como redes de proteínas) geralmente são livre de escala — assim como a internet ou redes sociais.

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

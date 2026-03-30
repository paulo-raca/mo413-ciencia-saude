# Resumo: Murgas et al. (2024)

**Título:** Multi-scale geometric network analysis identifies melanoma immunotherapy response gene modules
**Revista:** Scientific Reports, vol. 14, artigo 6082
**DOI:** https://doi.org/10.1038/s41598-024-56459-7
**Autores:** Kevin A. Murgas, Rena Elkin, Nadeem Riaz, Emil Saucan, Joseph O. Deasy, Allen R. Tannenbaum

---

## Glossário de Termos

| Termo                                 | O que significa                                                                                                                                                                                                                                               |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Melanoma**                          | Tipo mais agressivo de câncer de pele, originado nos melanócitos (células que produzem a pigmentação da pele)                                                                                                                                                 |
| **Imunoterapia**                      | Tratamento que não ataca o tumor diretamente, mas "ensina" o sistema imunológico do paciente a reconhecer e combater as células cancerosas                                                                                                                    |
| **Nivolumab**                         | Nome do medicamento de imunoterapia usado no estudo. É um anticorpo que bloqueia uma proteína chamada PD-1, que normalmente "desliga" o sistema imunológico — ao bloqueá-la, o sistema imune volta a atacar o tumor                                           |
| **Gene**                              | Trecho do DNA que carrega a instrução para produzir uma proteína específica                                                                                                                                                                                   |
| **Expressão gênica**                  | Medida de quão "ativo" um gene está — ou seja, o quanto ele está sendo lido e usado para produzir proteínas naquele momento                                                                                                                                   |
| **RNA-seq**                           | Técnica laboratorial para medir a expressão de milhares de genes ao mesmo tempo. Funciona como um "censo" de quais genes estão mais ou menos ativos numa amostra de tecido                                                                                    |
| **Rede de correlação**                | Um grafo (rede) em que cada nó é um gene e cada aresta representa o quanto a expressão de dois genes "anda junto" — se um sobe, o outro também sobe (ou desce)                                                                                                |
| **Curvatura de Ollivier-Ricci (ORC)** | Medida geométrica que avalia o quão "bem conectados" são os vizinhos de dois nós ligados por uma aresta. Valores positivos indicam que os dois nós pertencem ao mesmo grupo (comunidade); valores negativos indicam que fazem a ponte entre grupos diferentes |
| **Módulo gênico**                     | Grupo de genes que têm expressão coordenada — tendem a ser ativados ou silenciados juntos, geralmente porque participam do mesmo processo biológico                                                                                                           |
| **Via NF-κB**                         | Conjunto de proteínas que funcionam como um "interruptor" molecular: quando ativado, comanda processos de inflamação e resposta imunológica. Também está envolvido no crescimento tumoral                                                                     |
| **Clustering de Louvain**             | Algoritmo matemático que agrupa automaticamente os nós de uma rede em comunidades, maximizando conexões dentro de cada grupo e minimizando conexões entre grupos                                                                                              |
| **DEG**                               | _Differentially Expressed Gene_ — gene diferencialmente expresso: um gene que está significativamente mais ativo (ou menos ativo) num grupo comparado ao outro (ex.: antes vs. depois do tratamento)                                                          |
| **GO**                                | _Gene Ontology_ — sistema padronizado de classificação de genes por função biológica, componente celular ou processo em que participam                                                                                                                        |

---

## Problema Investigado

O melanoma é um câncer de pele muito agressivo. Embora imunoterapias como o nivolumab funcionem em alguns pacientes, não sabemos bem por que funcionam em uns e não em outros — e quais genes estão por trás dessa resposta.

---

## O Que Foi Feito

Os autores coletaram amostras de tumor de **43 pacientes com melanoma** antes e depois do tratamento com nivolumab e mediram a expressão de **912 genes** usando RNA-seq.

Com esses dados, construíram uma **rede de correlação**: cada gene é um nó, e dois genes são conectados por uma aresta se suas expressões mudam de forma coordenada em resposta ao tratamento. No total, a rede tinha **50.518 arestas**.

Em vez de usar métodos tradicionais de agrupamento (que exigem definir manualmente um limiar de correlação), os autores aplicaram a **curvatura de Ollivier-Ricci (ORC)** — uma propriedade geométrica da rede que identifica naturalmente quais arestas são "pontes" entre comunidades e quais estão dentro de comunidades.

A rede foi analisada em múltiplas escalas (o parâmetro τ na Figura 1A do artigo) para encontrar o ponto em que as comunidades ficam mais bem definidas (τ_crit = 1,58). Com isso, aplicaram o **algoritmo de Louvain** para dividir a rede em grupos.

---

## Estratégia de Grafo Utilizada

**Detecção de comunidades por curvatura geométrica (ORC + Louvain)**

```
Genes (nós) → Rede de correlação (arestas = correlação de expressão)
                    ↓
         Curvatura de Ollivier-Ricci
         (identifica arestas dentro vs. entre comunidades)
                    ↓
         Clustering de Louvain
                    ↓
         6 módulos (comunidades de genes)
                    ↓
         Análise de enriquecimento de vias biológicas (GO)
                    ↓
         Associação com sobrevida e resposta clínica
```

---

## Resultados

Foram identificados **6 módulos** de genes que respondem juntos à imunoterapia:

| Módulo | Nº de genes | Processo biológico associado                       |
| ------ | ----------- | -------------------------------------------------- |
| 1      | 116         | Endocitose e transporte vesicular                  |
| 2      | 79          | Migração e quimiotaxia de leucócitos               |
| 3      | 204         | Modificação de histonas e remodelação da cromatina |
| 4      | 342         | Adesão celular e proliferação de leucócitos        |
| 5      | 113         | Catabolismo proteossomal e ubiquitinação           |
| **6**  | **58**      | **Via NF-κB, sinalização de citocinas**            |

O **Módulo 6** foi o único associado significativamente à **melhor sobrevida** dos pacientes e à **resposta positiva ao tratamento** (p = 0,029). Dois genes deste módulo tiveram efeitos individuais significativos: **IL18R1** (mais ativo em quem respondeu bem) e **IL1RAP** (menos ativo em quem respondeu bem).

![Figura 1 do artigo — rede de genes dividida em 6 módulos coloridos por curvatura](murgas2024-geometric-network-melanoma.pdf)

---

## Por Que Este Artigo É Relevante para o Nosso Projeto

Nosso projeto compara redes gênicas de melanoma, não-melanoma e tecido saudável usando ferramentas como STRING e Cytoscape. Este artigo demonstra exatamente como a **detecção de comunidades em redes gênicas** pode revelar grupos de genes funcionalmente relevantes em melanoma — a mesma lógica que aplicaremos, mas com outra abordagem técnica (curvatura geométrica vs. MCODE).

---

## Referência

Murgas, K.A., Elkin, R., Riaz, N., Saucan, E., Deasy, J.O. & Tannenbaum, A.R. (2024). Multi-scale geometric network analysis identifies melanoma immunotherapy response gene modules. _Scientific Reports_, 14, 6082. https://doi.org/10.1038/s41598-024-56459-7

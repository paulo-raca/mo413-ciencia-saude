# Resumo: Xuan et al. (2021)

**Título:** Identification of Genes Potentially Associated with Melanoma Tumorigenesis Through Co-Expression Network Analysis
**Revista:** International Journal of General Medicine, vol. 14, pp. 8495–8508
**DOI:** https://doi.org/10.2147/IJGM.S336295
**Autores:** Xiuyun Xuan, Yuqi Wang, Yanhong Sun, Changzheng Huang

---

## Glossário de Termos

| Termo                         | O que significa                                                                                                                                                                                                    |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----- | -------------------------------------------------------------------------- |
| **Melanoma**                  | Tipo mais agressivo de câncer de pele, originado nos melanócitos (células responsáveis pela pigmentação da pele). Representa ~4% dos cânceres de pele mas causa ~75% das mortes por câncer de pele                 |
| **Tumorigenese**              | O processo pelo qual células normais se transformam em células cancerosas. O estudo investiga justamente essa "viagem" da pele normal até o melanoma                                                               |
| **DEG**                       | _Differentially Expressed Gene_ — Gene diferencialmente expresso: um gene que está significativamente mais ativo (superexpresso) ou menos ativo (subexpresso) em tecido canceroso comparado ao tecido normal       |
| **ODEG**                      | _Overlapping DEG_ — Gene diferencialmente expresso que aparece em **vários datasets ao mesmo tempo**, tornando-o mais confiável (menos provável de ser um falso positivo)                                          |
| **GEO**                       | _Gene Expression Omnibus_ — Banco de dados público onde pesquisadores depositam seus dados de expressão gênica para que outros possam reutilizá-los livremente                                                     |
| **Microarray**                | Tecnologia laboratorial que mede a atividade de milhares de genes simultaneamente numa amostra de tecido. Funciona como um "painel de controle" que mostra quais genes estão ligados e quais estão desligados      |
| **logFC**                     | _log Fold Change_ — Medida de quanto a expressão de um gene mudou.                                                                                                                                                 | logFC | > 1 significa que o gene está pelo menos 2× mais (ou menos) ativo no tumor |
| **PPI**                       | _Protein-Protein Interaction_ — Interação proteína-proteína: representa fisicamente quais proteínas se "encostam" e interagem umas com as outras dentro da célula. Cada proteína é produzida por um gene           |
| **STRING**                    | Banco de dados de interações conhecidas entre proteínas. Dado um conjunto de genes/proteínas, o STRING retorna quais pares já foram documentados como interagindo, com um "score de confiança"                     |
| **Cytoscape**                 | Software de visualização e análise de redes biológicas. Permite desenhar e explorar o grafo de interações                                                                                                          |
| **MCODE**                     | Plugin do Cytoscape que detecta automaticamente "regiões densamente conectadas" (módulos/comunidades) dentro de uma rede PPI                                                                                       |
| **CytoHubba**                 | Plugin do Cytoscape que calcula a importância de cada nó na rede usando 12 métricas matemáticas diferentes (grau, centralidade, etc.) para identificar os genes hub                                                |
| **Gene hub**                  | Gene que funciona como um "nó central" na rede — altamente conectado a muitos outros genes. Tende a ser biologicamente mais importante                                                                             |
| **GO**                        | _Gene Ontology_ — Sistema de classificação padronizado que descreve as funções dos genes: processo biológico (o que a célula faz), componente celular (onde está) e função molecular (como age)                    |
| **KEGG**                      | _Kyoto Encyclopedia of Genes and Genomes_ — Banco de dados de vias moleculares (circuitos de reações dentro da célula). Permite saber em qual "rota metabólica" ou "via de sinalização" um gene está envolvido     |
| **DAVID**                     | Ferramenta online de anotação funcional de genes — recebe uma lista de genes e diz quais processos biológicos estão "enriquecidos" nessa lista                                                                     |
| **GEPIA**                     | Plataforma online que usa dados do TCGA e GTEx para analisar expressão gênica em tumores e sua relação com sobrevida dos pacientes                                                                                 |
| **OS**                        | _Overall Survival_ — Sobrevida global: tempo de vida do paciente após o diagnóstico                                                                                                                                |
| **DFS**                       | _Disease-Free Survival_ — Sobrevida livre de doença: tempo sem recorrência do câncer após o tratamento                                                                                                             |
| **TIMER**                     | Banco de dados que avalia a correlação entre expressão gênica e infiltração de células do sistema imunológico no tumor                                                                                             |
| **TCGA**                      | _The Cancer Genome Atlas_ — Projeto que sequenciou o genoma de amostras de 33 tipos de câncer de milhares de pacientes. SKCM = melanoma cutâneo no TCGA                                                            |
| **TRRUST**                    | Banco de dados de redes de regulação por fatores de transcrição — diz quais "interruptores moleculares" controlam quais genes                                                                                      |
| **Fator de transcrição (TF)** | Proteína que funciona como um "interruptor": ao se ligar ao DNA, ativa ou silencia outros genes                                                                                                                    |
| **DGIdb**                     | Banco de dados de interações droga-gene: lista quais medicamentos conhecidos atuam sobre quais genes                                                                                                               |
| **qPCR**                      | _Quantitative Polymerase Chain Reaction_ — Técnica laboratorial que mede com precisão a quantidade de RNA de um gene específico numa amostra. É usada para **validar** os resultados computacionais no tecido real |
| **IHC**                       | _Immunohistochemistry_ — Imunohistoquímica: técnica que usa anticorpos marcados para visualizar ao microscópio onde e quanto uma proteína está presente em cortes de tecido                                        |
| **Quimiocinas**               | Família de pequenas proteínas (~8-14 kDa) que funcionam como "sinais de navegação" para células imunes — recrutam linfócitos e outros leucócitos para o local da inflamação ou tumor                               |
| **NF-κB**                     | Via de sinalização (conjunto de proteínas) que regula inflamação, resposta imune, proliferação celular e apoptose (morte celular programada)                                                                       |

---

## Problema Investigado

Melanoma é responsável por 75% das mortes por câncer de pele, apesar de representar apenas 4% dos casos. A maioria dos estudos foca em melanoma avançado ou metastático. Este trabalho investiga o processo menos estudado de **transição de pele normal para melanoma primário** — ou seja, o que acontece geneticamente no início do desenvolvimento do tumor.

---

## Dados Utilizados

Três datasets de microarray obtidos do banco público **GEO**, todos comparando melanoma primário vs. pele normal saudável:

| Dataset   | Amostras de Melanoma | Amostras Normais | Plataforma               |
| --------- | -------------------- | ---------------- | ------------------------ |
| GSE15605  | 46                   | 16               | Affymetrix U133 PLUS 2.0 |
| GSE46517  | 31                   | 7                | Affymetrix U133A         |
| GSE114445 | 16                   | 6                | Affymetrix U133 PLUS 2.0 |
| **Total** | **93**               | **29**           | —                        |

---

## Pipeline de Análise

```
3 datasets GEO (93 melanomas + 29 normais)
          ↓
  Identificação de DEGs em cada dataset
  (GEO2R / limma: |logFC| > 1, p < 0,05)
          ↓
  Diagrama de Venn → 295 ODEGs comuns
  (157 superexpressos + 138 subexpressos)
          ↓
  Anotação funcional (GO + KEGG via DAVID)
          ↓
  Rede PPI (STRING, confiança ≥ 0,70)
  149 nós, 510 arestas
          ↓
  Visualização no Cytoscape
          ↓
  Detecção de módulos: MCODE
  → Módulo 1 (score=9, 9 nós)
  → Módulo 2 (score=8, 8 nós)
          ↓
  Seleção de hub genes: CytoHubba (12 métodos)
  → 9 genes hub identificados
          ↓
  Validação: expressão (GEPIA), imunidade (TIMER),
  TFs (TRRUST), drogas (DGIdb),
  qPCR e IHC em tecidos humanos
```

---

## Estratégia de Grafo Utilizada

**Rede PPI + detecção de módulos (MCODE) + identificação de hubs (CytoHubba)**

O modelo de grafo é uma **rede de interação proteína-proteína (PPI)**:

- **Nós:** genes/proteínas (149 no total)
- **Arestas:** interações físicas conhecidas entre proteínas (510 no total), com score de confiança ≥ 0,70 no STRING

Sobre essa rede foram aplicadas duas estratégias complementares:

1. **MCODE** — detecta sub-redes densamente conectadas (módulos/comunidades): regiões onde cada nó se conecta a muitos outros nós do mesmo grupo
2. **CytoHubba** — calcula 12 métricas de centralidade para cada nó (grau, betweenness, closeness, etc.) e elege os genes com maior importância estrutural na rede como "hubs"

---

## Resultados

### ODEGs identificados

- **295 genes** em comum entre os 3 datasets
- 157 superexpressos no melanoma (mais ativos que na pele normal)
- 138 subexpressos no melanoma (menos ativos que na pele normal)

### Os 9 Genes Hub

| Gene       | Direção         | O que é                                                                          |
| ---------- | --------------- | -------------------------------------------------------------------------------- |
| **CXCL10** | ↑ superexpresso | Quimiocina que recruta células imunes para o tumor; associada a melhor sobrevida |
| **CXCL9**  | ↑ superexpresso | Quimiocina que inibe o crescimento tumoral por recrutamento linfocítico          |
| **CCL4**   | ↑ superexpresso | Quimiocina que recruta células NK (assassinas naturais) para o tumor             |
| **CXCL2**  | ↑ superexpresso | Quimiocina pró-inflamatória                                                      |
| **CCL5**   | ↑ superexpresso | Quimiocina que recruta linfócitos T e células NK; associada a melhor sobrevida   |
| **NPY1R**  | ↓ subexpresso   | Receptor de neuropeptídeo Y                                                      |
| **PTGER3** | ↓ subexpresso   | Receptor de prostaglandina                                                       |
| **NMU**    | ↓ subexpresso   | Neuromedin U; associada a **pior** sobrevida quando subexpresso                  |
| **CCL27**  | ↓ subexpresso   | Quimiocina da pele                                                               |

### Achados de Sobrevida

- **CCL4, CCL5, CXCL9, CXCL10** (os 4 superexpressos da família das quimiocinas) — associados a **melhor sobrevida** e mais expressos nos estágios iniciais (0 e 1) do melanoma
- **NMU** (subexpresso) — associado a **pior sobrevida**

### Correlação com o Sistema Imunológico (TIMER)

5 genes (CCL5, NPY1R, CXCL10, CXCL9, CCL4) mostraram correlação positiva com a infiltração dos 6 tipos de células imunes:

- Linfócitos B, Linfócitos T CD4⁺, Linfócitos T CD8⁺, Macrófagos, Neutrófilos, Células dendríticas

### Regulação por Fatores de Transcrição

| TF                                           | Genes que regula          |
| -------------------------------------------- | ------------------------- |
| **RELA** e **NFKB1** (componentes do NF-κB)  | CCL4, CCL5, CXCL10, CXCL2 |
| **IRF7, IRF3, IRF1** (fatores de interferon) | CCL5, CXCL10              |

### Interações Droga-Gene

46 pares droga-gene identificados. Destaques:

- **Oxaliplatina** (interagindo com CXCL10) — já usada em outros cânceres, com evidências de potencializar imunoterapia anti-PD-1
- **Beraprost** (interagindo com PTGER3) — análogo de prostaciclina que reduziu metástase pulmonar de melanoma em camundongos

### Validação Experimental

qPCR e IHC em 10 pares de tecido humano (melanoma + pele normal adjacente) confirmaram que **CCL4, CCL5, CXCL9 e CXCL10** estão mais expressos no melanoma tanto no nível de tecido quanto em linhagens celulares.

---

## Por Que Este Artigo É Relevante para o Nosso Projeto

Este artigo é o mais diretamente alinhado com nossa metodologia: usa **STRING + Cytoscape + MCODE** para construir uma rede PPI e encontrar módulos e hubs em melanoma — exatamente o que faremos no projeto. Os datasets GEO usados (GSE15605, GSE46517) são do mesmo tipo que usaremos. Os 9 genes hub identificados — especialmente **CXCL10, CXCL9, CCL4 e CCL5** — são candidatos fortes a aparecerem como nós centrais nas nossas redes. Além disso, a descoberta de que esses genes estão ligados à via NF-κB conecta diretamente com o Módulo 6 identificado por Murgas et al. (2024), sugerindo que essa via é um marcador robusto de melanoma.

---

## Referência

Xuan, X., Wang, Y., Sun, Y. & Huang, C. (2021). Identification of Genes Potentially Associated with Melanoma Tumorigenesis Through Co-Expression Network Analysis. _International Journal of General Medicine_, 14, 8495–8508. https://doi.org/10.2147/IJGM.S336295

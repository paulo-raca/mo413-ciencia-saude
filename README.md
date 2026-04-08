# MO413A — Ciência e Visualização de Dados em Saúde

**UNICAMP, 1º semestre de 2026** | [Página da disciplina](https://datasci4health.github.io/) | [Google Classroom](https://classroom.google.com/c/ODQwMTg4NTgxMDMz)

Disciplina interdisciplinar que integra Ciência de Dados, Biologia de Sistemas e Ciência de Redes aplicadas à saúde. O curso aborda desde fundamentos de biologia celular e genômica até análise de redes complexas, com projetos práticos em datasets reais de doenças como câncer, leucemia e doenças cardiovasculares.

---

## Aulas

### 2026-02-23 — Course Overview

[resumo](aulas/2026-02-23%20-%20Course%20Overview/README.md) | [slides](aulas/2026-02-23%20-%20Course%20Overview/slides.pdf) | [YouTube](https://www.youtube.com/watch?v=Yb-ygbFyeAc)

Apresentação da disciplina: sua natureza interdisciplinar unindo Saúde, Biologia de Sistemas, Ciência de Dados e Ciência de Redes. Discute o papel das redes como modelo central para representar fenômenos biológicos complexos e apresenta os quatro pilares do curso — saúde, biologia de sistemas, ciência de dados e visualização.

### 2026-02-25 — Models and Tables

[resumo](aulas/2026-02-25%20-%20Models%20and%20Tables/README.md) | [slides](aulas/2026-02-25%20-%20Models%20and%20Tables/slides.pdf) | [YouTube](https://www.youtube.com/watch?v=iy6lvExoqLk)

Introdução aos modelos conceituais, lógicos e físicos de dados. Apresenta os principais paradigmas de representação de dados biológicos — tabelas relacionais, grafos e modelos semânticos — e discute como a escolha do modelo impacta a análise, com exemplos em dados genômicos e de expressão gênica.

### 2026-03-02 — Biologia Celular e Molecular

[resumo](aulas/2026-03-02%20-%20Biologia%20celular%20e%20molecular/README.md) | [slides](aulas/2026-03-02%20-%20Biologia%20celular%20e%20molecular/slides.pdf) | [YouTube](https://www.youtube.com/watch?v=V0h4nsmtv2g)

Fundamentos de biologia celular e molecular para cientistas de dados: o dogma central (DNA → RNA → Proteína), estrutura dos genes, transcrição, tradução e regulação gênica. Contextualiza como variações nesse fluxo de informação estão associadas a doenças e são capturadas por tecnologias como microarray e RNA-seq.

### 2026-03-04 — Genomics and Transcriptomics

[resumo](aulas/2026-03-04%20-%20Genomics%20and%20transcriptomics/README.md) | [slides](aulas/2026-03-04%20-%20Genomics%20and%20transcriptomics/slides.pdf) | [YouTube](https://www.youtube.com/watch?v=lI1nm7oQE8E)

Panorama das tecnologias ômicas (genômica, transcriptômica, proteômica, metabolômica) e seus dados. Foco em expressão gênica diferencial: como identificar genes mais ou menos ativos em condições distintas usando RNA-seq e microarray, e como esses dados alimentam análises de redes biológicas.

### 2026-03-09 — Networks and Graphs

[resumo](aulas/2026-03-09%20-%20Networks%20and%20Graphs/README.md) | [slides](aulas/2026-03-09%20-%20Networks%20and%20Graphs/slides.pdf) | [YouTube](https://www.youtube.com/watch?v=AMRqb0UntEk)

Fundamentos matemáticos de grafos aplicados a redes biológicas: definição de nós e arestas, grafos direcionados e não-direcionados, pesos, métricas de centralidade (grau, betweenness, closeness, eigenvector) e introdução ao Cytoscape como ferramenta de visualização e análise de redes.

### 2026-03-11 — Complex Networks

[resumo](aulas/2026-03-11%20-%20Complex%20Networks/README.md) | [slides](aulas/2026-03-11%20-%20Complex%20Networks/slides.pdf) | [YouTube](https://www.youtube.com/watch?v=sIK1K8-pguI)

Propriedades emergentes de redes complexas: redes livre de escala (scale-free), mundo pequeno (small-world), hubs, comunidades e coeficiente de clustering. Apresenta algoritmos de detecção de comunidades (Louvain, MCODE) e sua aplicação em redes de interação proteína-proteína e co-expressão gênica.

### 2026-03-18 — Breast Cancer (exercício prático)

[resumo](aulas/2026-03-18%20-%20Breast%20Cancer/README.md)

Aula prática de análise de rede de interações gênicas em câncer de mama usando Cytoscape. Utilizou os slides da aula de redes complexas (11/03). Sem gravação.

### 2026-03-30 — Redes PPI, Correlação e Workflow

[resumo](aulas/2026-03-30%20-%20Redes%20PPI%2C%20Correla%C3%A7%C3%A3o%20e%20Workflow/README.md) | [slides PPI](aulas/2026-03-30%20-%20Redes%20PPI%2C%20Correla%C3%A7%C3%A3o%20e%20Workflow/slides-ppi.pdf) | [slides Correlação](aulas/2026-03-30%20-%20Redes%20PPI%2C%20Correla%C3%A7%C3%A3o%20e%20Workflow/slides-correlacao.pdf) | [slides Workflow](aulas/2026-03-30%20-%20Redes%20PPI%2C%20Correla%C3%A7%C3%A3o%20e%20Workflow/slides-workflow.pdf)

Aula tripla cobrindo redes de interação proteína-proteína (PPI) e bancos como STRING, métodos de correlação para construir redes de co-expressão gênica (Pearson, Spearman, distância de Jensen-Shannon), e introdução ao Orange Data Mining com foco em reprodutibilidade de workflows científicos.

### 2026-04-01 — Orange e Workflow (Aula Prática)

[resumo](aulas/2026-04-01%20-%20Orange%20e%20Workflow%20(Pr%C3%A1tica)/README.md) | [slides](aulas/2026-04-01%20-%20Orange%20e%20Workflow%20(Pr%C3%A1tica)/slides-workflow.pdf)

Continuação prática da aula de 30/03. Construção de redes de correlação de genes usando Orange Data Mining com datasets GEO reais (GSE45827 — câncer de mama), incluindo normalização de dados, seleção de genes diferencialmente expressos e exportação para o Cytoscape. Sem gravação.

### 2026-04-06 — Análise de Redes — Centralidade e Modularidade

[resumo](aulas/2026-04-06%20-%20An%C3%A1lise%20de%20Redes%20-%20Centralidade%20e%20Modularidade/README.md) | [slides](aulas/2026-04-06%20-%20An%C3%A1lise%20de%20Redes%20-%20Centralidade%20e%20Modularidade/slides.pdf)

Análise quantitativa de redes complexas: quatro métricas de centralidade (grau, proximidade, intermediação, autovetor), PageRank como variante da centralidade de autovetor, quatro tipos de redes biológicas (PPI, metabólica, regulatória, RNA), medicina em redes (doenças como perturbações em redes moleculares), detecção de comunidades com o algoritmo de Louvain e modularidade, motivos de rede e predição de links por similaridade local e global.

---

## Projeto Semestral

[README](projeto/README.md) | [slides](projeto/slides.pdf)

**Câncer de Pele e seus Tipos: uma Análise do Perfil de Expressão Gênica em Redes** — comparação de redes de interação gênica derivadas de amostras de melanoma, não-melanoma e tecido saudável, usando dados do GEO, STRING e Cytoscape. O projeto investiga diferenças topológicas entre as redes, identifica genes centrais (hubs) e módulos biológicos específicos de cada condição, com análise adicional via Graph Attention Networks (GAT) sobre dados do TCGA-SKCM.

### L1 — How Wolves Change Rivers

[README](projeto/L1%20-%20How%20Wolves%20Chang%20Rivers/README.md)

Modelagem de um ecossistema como grafo no Cytoscape, inspirado no fenômeno de trophic cascade do Parque Yellowstone. O subgrupo construiu tabelas de nós, arestas e expressão das populações, representando relações ecológicas (não apenas alimentares) e visualizando estados inicial, intermediário e final do sistema após a reintrodução dos lobos.

### L2 — Artigos: Redes Complexas em Expressão Gênica

[README](projeto/L2%20-%20artigos/README.md)

Revisão de artigos científicos que aplicam estratégias de redes complexas (hubs, comunidades, rewiring, GNNs) à análise de expressão gênica em câncer de pele. O subgrupo (Paulo, Naruan, Alan) revisou 5 artigos cobrindo WGCNA, CytoHubba, GraphSAGE, GCN e K-Means em melanoma e carcinoma espinocelular cutâneo, com resumos detalhados explicando metodologia e relevância para o projeto.

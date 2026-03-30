# L2 — Artigos: Redes Complexas em Expressão Gênica

Revisão de artigos científicos que aplicam estratégias de redes complexas à análise de expressão gênica em câncer de pele, como parte da fundamentação teórica do projeto semestral da equipe ALFAK.

---

## Subgrupo A — Augusto José Peterlevitz, Felipe Kennedy Carvalho Torquato, Luis Henrique Angélico

### Kaushik et al. (2015) — Gene Network Rewiring in Melanoma

[artigo](https://doi.org/10.1371/journal.pone.0142443) | [PDF](A/kaushik2015%20-%20Gene%20Network%20Rewiring%20in%20Melanoma/paper.pdf) | [resumo](A/kaushik2015%20-%20Gene%20Network%20Rewiring%20in%20Melanoma/README.md)

A partir de 642 amostras de microarray divididas em quatro estágios do melanoma (Normal → CnM → CM → LN), o estudo constrói redes de co-expressão por correlação de Pearson para cada estágio e analisa o _rewiring_ — mudanças nas conexões dos genes entre estágios, independentemente de sua expressão diferencial. A principal descoberta é que a maioria dos genes que alteram seu papel na rede tumoral **não são diferencialmente expressos**, e que hubs distintos emergem em cada fase da progressão da doença.

### Jiang et al. (2021) — Hub Genes in Melanoma via WGCNA + CytoHubba

[artigo](https://doi.org/10.3389/fonc.2021.621430) | [PDF](A/jiang2021%20-%20Hub%20Genes%20in%20Melanoma/paper.pdf) | [resumo](A/jiang2021%20-%20Hub%20Genes%20in%20Melanoma/README.md)

Combinando dados de duas fontes independentes (UCSC Xena e GEO GSE3189), o estudo aplica WGCNA para identificar módulos de co-expressão associados ao melanoma e análise de expressão diferencial (Limma) para selecionar 435 genes candidatos. A rede PPI desses genes é construída via STRING e importada no Cytoscape, onde o plugin CytoHubba (algoritmo MCC) identifica os 10 hub genes mais centrais. Cinco deles — FOXM1, EXO1, KIF20A, TPX2 e CDC20 — são associados a menor sobrevida global e validados por imuno-histoquímica.

### Cinaglia & Cannataro (2023) — GCN para Associações Gene–Doença

[artigo](https://doi.org/10.3390/e25060909) | [resumo](A/cinaglia2023%20-%20Gene%20Disease%20Associations%20via%20GNN/README.md)

Propõe um modelo de Graph Convolutional Network (GCN) sobre um grafo heterogêneo com nós de genes e doenças (fonte: DisGeNET), capaz de prever novas associações gene–doença via _link prediction_. O modelo atinge AUC de 95% em treino, validação e teste, com 93% de acerto no Top-15 de genes candidatos para doenças conhecidas, e é validado externamente no dataset BioSNAP/Stanford.

### Mastropietro et al. (2023) — XGDAG: GNN Explicável para Genes de Doença

[artigo](https://doi.org/10.1093/bioinformatics/btad482) | [resumo](A/mastropietro2023%20-%20XGDAG%20Explainable%20GNN/README.md)

Apresenta o XGDAG, um framework que usa GraphSAGE (7 camadas) sobre a rede PPI do BioGRID com aprendizado positivo-não rotulado (NIAPU) para priorizar genes candidatos a doenças. O diferencial é a incorporação de métodos de IA explicável (GNNExplainer, GraphSVX, SubgraphX) que identificam o subgrafo da rede PPI que justifica cada previsão, tornando o modelo interpretável para biólogos.

### Speranza et al. (2025) — Subtipos Moleculares de Melanoma via K-Means + WGCNA

[artigo](https://doi.org/10.3390/genes16121428) | [resumo](A/speranza2025%20-%20Melanoma%20Molecular%20Subtypes/README.md)

A partir de 194 amostras de melanoma (dataset E-MTAB-6697), aplica K-Means para estratificar os tumores em três subtipos moleculares distintos e WGCNA para identificar os módulos de co-expressão específicos de cada subtipo. Os três clusters divergem em proliferação, metabolismo e plasticidade celular, mas compartilham perfis imunológicos "quentes" (IPS 7–8), sugerindo que todos podem responder à imunoterapia por mecanismos diferentes.

---

## Subgrupo B — Paulo Costa, Naruan Francisco Ferraz e Ferraz, Alan Freitas Ribeiro

### Chen, Yang & Wu (2021) — Hub Genes em Carcinoma Espinocelular Cutâneo

[artigo](https://doi.org/10.1186/s12885-021-08604-y) | [PDF](B/chen2021%20-%20Hub%20Genes%20in%20Cutaneous%20SCC/paper.pdf) | [resumo](B/chen2021%20-%20Hub%20Genes%20in%20Cutaneous%20SCC/README.md)

Usando dois datasets de microarray (GSE45216 + GSE98774 combinados) e um de RNA-seq (GSE108008) analisados separadamente com WGCNA, o estudo identifica módulos de co-expressão associados ao carcinoma espinocelular cutâneo (cSCC) e à queratose actínica (AK, lesão pré-cancerígena). A interseção dos resultados de ambas as análises revela sete hub genes — AURKA, BUB1, CCNB1, CDK1, KIF2C, TOP2A e TPX2 — validados por expressão proteica e análise de sobrevida.

### Murgas et al. (2024) — Curvatura de Ricci e Resposta à Imunoterapia no Melanoma

[artigo](https://doi.org/10.1038/s41598-024-56459-7) | [PDF](B/murgas2024%20-%20Geometric%20Network%20Analysis%20in%20Melanoma/paper.pdf) | [resumo](B/murgas2024%20-%20Geometric%20Network%20Analysis%20in%20Melanoma/README.md)

Aplica a curvatura de Ollivier-Ricci (ORC) — uma medida geométrica derivada do transporte ótimo — a redes de co-expressão gênica de pacientes com melanoma tratados com imunoterapia. A ORC captura a "saúde" local das arestas da rede e, combinada com detecção de comunidades por Louvain, identifica módulos de genes cujas propriedades geométricas distinguem respondedores de não-respondedores ao tratamento, revelando padrões de sinalização imune e NF-κB.

### Xuan et al. (2021) — Genes de Tumorigenese do Melanoma por Co-expressão

[artigo](https://doi.org/10.2147/IJGM.S336295) | [PDF](B/xuan2021%20-%20Melanoma%20Tumorigenesis%20via%20Co-expression/paper.pdf) | [resumo](B/xuan2021%20-%20Melanoma%20Tumorigenesis%20via%20Co-expression/README.md)

A partir do dataset GSE3189 (GEO), constrói uma rede de co-expressão para identificar genes diferencialmente expressos em melanoma, importa os candidatos no STRING e usa MCODE (detecção de módulos densos) e CytoHubba no Cytoscape para identificar nove hub genes — AURKA, CCNB1, CDK1, BUB1B, KIF2C, TOP2A, BUB1, CDCA8 e TPX2 — associados à tumorigenese do melanoma e validados por análise de sobrevida no TCGA.

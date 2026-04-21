# Datasets e Bases de Dados da Disciplina

Levantamento de todas as **bases de dados públicas**, **datasets específicos** e **arquivos de exercício** mencionados ou usados nas aulas da disciplina **MO413A — Ciência e Visualização de Dados em Saúde** (UNICAMP, 2026/1).

Para cada recurso estão indicados: o que é, a URL (quando disponível), em quais aulas aparece e como foi usado.

---

## 1. Bases de Interação Proteína-Proteína (PPI)

Redes PPI mapeiam quais proteínas "trabalham juntas" dentro da célula — funcionam como um **organograma** de quem interage com quem.

### STRING

- **O que é:** base de interações proteína-proteína conhecidas e previstas, cobrindo milhares de organismos. Agrega evidências de experimentos, coexpressão, co-ocorrência em literatura, bancos curados e homologia.
- **URL:** https://string-db.org/
- **Aulas:** `2026-03-04`, `2026-03-09`, `2026-03-30`, `2026-04-06`, `2026-04-08`, `2026-04-13`
- **Uso:** fonte principal de redes PPI para importar no Cytoscape. Nas aulas práticas gera a rede PPI de melanoma (via KEGG hsa05218) e a rede PPI de câncer de mama.

### BioGRID, IntAct, MINT, BIND, HPRD, DIP

- **O que são:** outras bases especializadas em interações biológicas (proteína-proteína, genética, química). Citadas como alternativas/complementos ao STRING.
- **URLs:** https://thebiogrid.org/ · https://www.ebi.ac.uk/intact/ · https://mint.bio.uniroma2.it/
- **Aulas:** `2026-04-06`
- **Uso:** apresentadas como fontes de PPI na discussão sobre construção de redes biológicas.

---

## 2. Bases de Expressão Gênica

### GEO (Gene Expression Omnibus)

- **O que é:** repositório público do NCBI com dados de expressão gênica[^expr] (microarray e RNA-Seq) de milhares de estudos.
- **URL:** https://www.ncbi.nlm.nih.gov/geo/
- **Aulas:** `2026-03-30`, `2026-04-01`, `2026-04-13`
- **Uso:** fonte primária de dados de expressão. Formato de download: SOFT.

#### Dataset específico: **GSE45827** (câncer de mama)

- **Origem:** Gruosso et al. (2016), *EMBO Molecular Medicine*.
- **Conteúdo:** 155 amostras — 41 Triple-Negative, 30 HER2, 29 Luminal A, 30 Luminal B, 11 normais, 14 linhagens celulares.
- **Plataforma:** Affymetrix GPL570 (HG-U133 Plus 2.0).
- **Uso:** base das aulas práticas de construção de rede de correlação de expressão em Orange + Cytoscape.

---

## 3. Bases de Vias Metabólicas e Anotação Funcional

Vias ("pathways") são **receitas passo-a-passo** de processos celulares — como uma sequência de reações de uma linha de produção.

### KEGG (Kyoto Encyclopedia of Genes and Genomes)

- **O que é:** enciclopédia de vias metabólicas, de sinalização e regulatórias. Cada via tem um diagrama interativo.
- **URL:** https://www.kegg.jp/
- **Aulas:** `2026-03-02`, `2026-03-04`, `2026-03-09`, `2026-04-06`, `2026-04-08`
- **Uso:** fonte de conjuntos de genes por via (ex.: hsa05218 — Melanoma; NF-κB; MAPK) e alvo de análise de enriquecimento no DAVID.

### Reactome

- **O que é:** base de vias biológicas humanas com diagramas detalhados ("mapas de metrô" da célula).
- **URL:** https://reactome.org/
- **Aulas:** `2026-04-08`
- **Uso:** análise de enriquecimento via DAVID e extração de conjuntos de proteínas participantes (ex.: pathway **R-HSA-1474228** — organização da matriz extracelular).

### WikiPathways

- **O que é:** plataforma colaborativa de curadoria de vias biológicas (estilo Wikipedia).
- **URL:** https://www.wikipathways.org/
- **Aulas:** `2026-04-08`
- **Uso:** terceira fonte de vias no enriquecimento via DAVID.

### Gene Ontology (GO)

- **O que é:** vocabulário controlado que classifica genes em três eixos — processo biológico, função molecular, componente celular.
- **URLs:** https://geneontology.org/ · Navegador: https://www.ebi.ac.uk/QuickGO/
- **Aulas:** `2026-02-23`, `2026-02-25`, `2026-03-04`, `2026-03-09`, `2026-04-08`
- **Uso:** anotação funcional de genes e análise de enriquecimento (termos GO sobre-representados em listas de genes).

### DAVID (Database for Annotation, Visualization and Integrated Discovery)

- **O que é:** ferramenta de enriquecimento funcional que integra KEGG, Reactome, WikiPathways e GO em um mesmo teste de sobre-representação[^ora].
- **URL:** https://davidbioinformatics.nih.gov/
- **Aulas:** `2026-02-25`, `2026-03-04`, `2026-04-08`
- **Uso:** dado uma lista de genes, DAVID retorna vias/termos GO enriquecidos com p-valor (teste exato de Fisher).

---

## 4. Grafos de Conhecimento Biomédico

### Rede Humana Sintoma-Doença (Zhou et al., 2014)

- **O que é:** rede com 4.442 doenças e 322 sintomas, com 147.978 associações extraídas de literatura via TF-IDF[^tfidf].
- **Referência:** Zhou et al. (2014), *Nature Communications*, 5, 4212.
- **Arquivo usado:** `disease-disease.csv` (1.596 doenças, 133.106 arestas ponderadas por similaridade de sintomas) — disponível em [datasci4health.github.io/networks/symptom-disease](https://github.com/datasci4health/datasci4health.github.io/tree/master/networks/symptom-disease).
- **Aulas:** `2026-02-25`, `2026-03-09`, `2026-04-06`, `2026-04-08`, `2026-04-13`
- **Uso:** base do exercício prático de detecção de comunidades (algoritmo Leiden) e threshold de arestas no Cytoscape. Liga **fenoma** (sintomas) a **genoma** (genes compartilhados).

### Diseasome (Goh et al., 2007 — *The Human Disease Network*)

- **O que é:** rede bipartida de doenças e genes causadores, projetada em rede doença-doença e rede gene-gene.
- **Referência:** Goh et al. (2007), *PNAS* — dados como material suplementar.
- **Aulas:** `2026-04-08`, `2026-04-13`
- **Uso:** exemplo clássico de rede biomédica; mostra agrupamento de doenças por categoria (metabólica, ocular, renal).

### PrimeKG (Precision Medicine Knowledge Graph)

- **O que é:** grafo de conhecimento multimodal com 17.080 doenças e 4.050.249 relações integrando 20 bases biomédicas em 10 escalas (doenças, drogas, genes, fenótipos, vias, anatomia, exposições).
- **URL:** https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM
- **Referência:** Chandak, Huang & Zitnik (2023), *Scientific Data*, 10(1), 67.
- **Aulas:** `2026-02-25`, `2026-03-09`
- **Uso:** exemplo de grafo de conhecimento biomédico em larga escala (arquivo `nodes.tab` com 129.375 nós).

### OMIM (Online Mendelian Inheritance in Man)

- **O que é:** catálogo de genes humanos e fenótipos genéticos.
- **URL:** https://www.omim.org/
- **Aulas:** `2026-04-13`
- **Uso:** citado como fonte de associações doença-gene (IDs OMIM referenciados nas redes de Zhou/Goh).

---

## 5. Ontologias e Terminologias

### MeSH (Medical Subject Headings)

- **O que é:** vocabulário controlado do NLM para indexação de literatura biomédica.
- **URL:** https://www.nlm.nih.gov/mesh/
- **Aulas:** `2026-04-13`
- **Uso:** padroniza nomes de doenças e sintomas na rede de Zhou (colunas *MeSH Disease ID* e *MeSH Symptom Term*).

### MONDO (Mondo Disease Ontology)

- **O que é:** ontologia unificada de doenças que integra OMIM, DO, Orphanet, ICD etc.
- **URL:** https://mondo.monarchinitiative.org/
- **Aulas:** `2026-04-01` (arquivo de exercício OpenTargets usa `MONDO_0007254` = câncer de mama).

### WordNet

- **O que é:** base lexical que organiza palavras em *synsets* com relações semânticas (análoga ao GO, mas para linguagem natural).
- **Aulas:** `2026-03-09`
- **Uso:** exemplo comparativo de estrutura ontológica.

### DBpedia

- **O que é:** grafo de conhecimento estruturado extraído da Wikipedia.
- **URL:** https://www.dbpedia.org/
- **Aulas:** `2026-03-09`, `2026-04-06`
- **Uso:** exemplo geral de grafo de conhecimento (não específico de saúde).

---

## 6. Bases de Referência de Genes, Proteínas e Genomas

### NCBI (Entrez, RefSeq, Gene)

- **O que é:** conjunto de bases do NCBI com sequências de referência (RefSeq), identificadores únicos de genes (Entrez ID) e anotações.
- **URL:** https://www.ncbi.nlm.nih.gov/
- **Aulas:** `2026-03-02`, `2026-03-04`, `2026-04-08`
- **Uso:** mapeamento de símbolos de gene para identificadores estáveis usados no DAVID e outros.

### UniProt

- **O que é:** base de referência para proteínas (sequência, função, domínios, modificações).
- **URL:** https://www.uniprot.org/
- **Aulas:** `2026-04-08`, `2026-04-01`
- **Uso:** IDs UniProt aparecem nos mapeamentos STRING e em listas de proteínas de vias Reactome.

### UCSC Genome Browser

- **O que é:** visualizador interativo do genoma humano com trilhas de anotação (GENCODE, RefSeq, MANE Select, PhyloP).
- **URL:** https://genome.ucsc.edu/
- **Aulas:** `2026-03-02`, `2026-03-04`
- **Uso:** visualização de genes em seus contextos genômicos (ex.: BRAF no cromossomo 7).

### PubMed

- **O que é:** interface de busca para MEDLINE — a principal base de citações biomédicas.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/
- **Aulas:** `2026-02-25`, `2026-03-09`, `2026-04-13`
- **Uso:** fonte da co-ocorrência doença-sintoma na rede de Zhou (2014) e base para PrimeKG.

### Pfam

- **O que é:** base de famílias de domínios proteicos.
- **URL:** https://www.ebi.ac.uk/interpro/ (Pfam agora integrado ao InterPro).
- **Aulas:** `2026-02-23`
- **Uso:** citada no contexto de modelos de linguagem para proteínas (ESM treinado em ~19 mil famílias Pfam).

---

## 7. Drug-Target / Associação Fármaco-Doença

### Open Targets Platform

- **O que é:** plataforma que agrega evidências que ligam alvos (genes/proteínas) a doenças, combinando genética, expressão, patologia, literatura e ensaios clínicos.
- **URL:** https://platform.opentargets.org/
- **Aulas:** `2026-04-01` (exercício)
- **Uso:** arquivo `OT-MONDO_0007254-associated-targets-01_04_2026-v26_03.tsv` — alvos associados ao câncer de mama (MONDO_0007254) baixados da plataforma.

---

## 8. Ferramentas que dão acesso a dados

Não são bases em si, mas intermediam o acesso a várias bases acima:

| Ferramenta | O que acessa | Aulas |
| --- | --- | --- |
| **Cytoscape** ([cytoscape.org](https://cytoscape.org/)) | STRING, GEO, PrimeKG, Reactome, qualquer CSV/SIF de rede. Apps: STRING, clusterMaker2 (Leiden), CytoNCA, MCODE, NetworkAnalyzer. | `2026-03-09`, `2026-03-30`, `2026-04-01`, `2026-04-06`, `2026-04-08`, `2026-04-13` |
| **Orange Data Mining** ([orange.biolab.si](https://orange.biolab.si/)) | Leitura de SOFT (GEO), CSV, cálculo de correlações, pipelines visuais. | `2026-03-30`, `2026-04-01`, `2026-04-13` |
| **Dagoberto** ([datasci4health.github.io/networks/dagoberto](https://datasci4health.github.io/networks/dagoberto/)) | Visualiza redes a partir de CSVs de nós e arestas direto no navegador. | `2026-02-25`, `2026-03-09` |

---

## 9. Datasets dos Exercícios (arquivos no repo)

| Aula | Arquivo | Conteúdo |
| --- | --- | --- |
| `2026-03-11` | `zombie.cys`, `8-cities.cys` | Redes toy para análise básica no Cytoscape. |
| `2026-03-18` | `Breast Cancer - genes.csv` | Genes diferencialmente expressos (log2FC, p-valor) em câncer de mama — derivado de microarray Affymetrix GPL570. |
| `2026-03-18` | `Breast Cancer - gene interactions.csv` | Arestas da rede PPI de câncer de mama (STRING). |
| `2026-03-18` | `breast-cancer.cys` | Sessão Cytoscape pronta com a rede PPI acima. |
| `2026-04-01` | `Aula 30_03_2026.ows` | Workflow Orange completo (GEO → correlação → rede). |
| `2026-04-01` | `string_mapping.tsv`, `string_interactions_short.csv` | Mapeamento símbolo→UniProt e arestas STRING. |
| `2026-04-01` | `OT-MONDO_0007254-associated-targets-01_04_2026-v26_03.tsv` | Alvos associados a câncer de mama (Open Targets). |
| `2026-04-01` | `Resultado aula 30_03_2026.csv`, `trequinho.csv`, `exercicio.cys` | Resultado do workflow e sessão final. |
| `2026-04-08` | `Participating Molecules [R-HSA-1474228].tsv` | Proteínas da via Reactome R-HSA-1474228 (MMPs, fibrilinas, ADAMTS). |
| `2026-04-08` / `2026-04-13` | `cytoscape.cys` | Rede Zhou (sintoma-doença) com comunidades detectadas. |
| `2026-04-13` | `breast-cancer-workflow-luminal-a-coexpression-chart.ows` | Workflow Orange para rede de coexpressão em Luminal-A. |

---

## 10. Formatos de arquivo usados

| Formato | Onde aparece | Descrição |
| --- | --- | --- |
| **SOFT** | GEO | Formato texto do GEO com matriz de expressão + metadados. |
| **CSV / TSV** | Todos os exercícios | Tabelas de nós, arestas e matrizes de expressão. |
| **SIF** | Cytoscape | *Simple Interaction Format* — lista de arestas minimalista. |
| **CYS** | Cytoscape | Sessão completa (rede + layout + estilos). |
| **OWS** | Orange | Workflow visual do Orange. |
| **GMT** | Enriquecimento | *Gene Matrix Transposed* — conjuntos de genes (um por linha). |
| **FASTQ, BAM, VCF** | `2026-03-04` | Leituras de sequenciamento, alinhamentos e variantes (citados conceitualmente). |

---

## Resumo por Categoria

- **Interação proteína-proteína:** STRING (principal), BioGRID, IntAct, MINT, BIND, HPRD, DIP
- **Vias / Função:** KEGG, Reactome, WikiPathways, Gene Ontology (+ DAVID como integrador)
- **Expressão gênica:** GEO (dataset-chave das aulas: **GSE45827**)
- **Grafos de conhecimento:** Rede Zhou 2014 (sintoma-doença), Diseasome, PrimeKG
- **Ontologias:** GO, MeSH, MONDO, WordNet, DBpedia
- **Referência genômica/proteica:** NCBI (Entrez/RefSeq), UniProt, UCSC, Pfam
- **Fármaco-alvo:** Open Targets
- **Literatura:** PubMed

**Datasets do projeto semestral (não cobertos nas aulas, referidos no [README do projeto](projeto/README.md)):** GSE4570, GSE2503, GSE53462, GSE8401, GSE7553, GSE45216 (melanoma/não-melanoma/pele saudável) e TCGA-SKCM (projeto GAT).

---

[^expr]: **Expressão gênica** — o quanto um gene está sendo "lido" pela célula para produzir proteína. Medir expressão de milhares de genes em várias amostras gera uma matriz de expressão.
[^ora]: **Over-Representation Analysis (ORA)** — testa se termos (ex.: vias KEGG) aparecem mais vezes numa lista de genes do que seria esperado por acaso. Teste típico: exato de Fisher.
[^tfidf]: **TF-IDF** — *Term Frequency – Inverse Document Frequency*. Peso que valoriza termos frequentes em um documento, mas raros no corpus geral. Zhou (2014) usou isso para medir a força da associação doença-sintoma em artigos do PubMed.

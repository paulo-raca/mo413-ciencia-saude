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
- **Aulas:** `2026-03-30`, `2026-04-01`, `2026-04-13`, `2026-04-15`
- **Uso:** fonte primária de dados de expressão. Formato de download: SOFT. Na aula de miRNAs, usado para *data mining* de alvos de miRNAs do locus DLK1-DIO3 em câncer de tireoide.

### TCGA (The Cancer Genome Atlas)

- **O que é:** atlas genômico de câncer do NCI/NIH — perfis moleculares (mutações, expressão, metilação, miRNA-seq) de mais de 33 tipos de tumor em ~20.000 amostras pareadas tumor/normal.
- **URL:** https://portal.gdc.cancer.gov/ (GDC Data Portal)
- **Aulas:** `2026-04-15`, `2026-04-29`
- **Uso:** na aula de miRNAs (15/04), fonte dos dados de 57 carcinomas papilares de tireoide (PTC) vs. tireoide normal pareada para mostrar queda dos miRNAs do locus 14q32. Na aula de miRNA-mRNA Network (29/04), download da coorte THCA completa (503 pacientes) via Firehose/FireBrowse — dados clínicos, miRSeq, mRNA-seq. Também aparece no projeto semestral (TCGA-SKCM para análise de melanoma com GAT).

#### Coorte específica: **TCGA-THCA** (Thyroid Carcinoma)

- **Conteúdo:** 503 pacientes com carcinoma de tireoide (majoritariamente papilífero, PTC).
- **Versão usada na aula:** `TCGA data version 2016_01_28` (via FireBrowse).
- **Disponibilidade por tipo de dado:** Clinical 503, methylation 503, miRSeq 502, mRNASeq 501, SNP6 CopyNum 499, MAF 402, RPPA 222.
- **Arquivos-chave (Firehose):**
  - `Clinical_Pick_Tier1` — clínicos curados.
  - `illuminahiseq_mirnaseq-miR_isoform_expression` — expressão por isoforma de miRNA.
  - `illuminahiseq_rnaseqv2-RSEM_genes_normalized` — expressão de mRNA por gene, normalizada por RSEM.
- **Uso:** base do exercício de construção de rede miRNA-mRNA na aula de 29/04.

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
- **Aulas:** `2026-03-02`, `2026-03-04`, `2026-03-09`, `2026-04-06`, `2026-04-08`, `2026-04-15`, `2026-05-11`
- **Uso:** fonte de conjuntos de genes por via (ex.: hsa05218 — Melanoma; NF-κB; MAPK) e alvo de análise de enriquecimento no DAVID. Na aula de miRNAs, enriquecimento em Hippo, PI3K-Akt, Focal adhesion, VEGF signaling em câncer de tireoide. Na aula de 11/05, exemplo da via hsa05220 (Chronic Myeloid Leukemia) mostrando o gene de fusão BCR-ABL ativando PI3K e MAPK signaling, e entrada combinada `hsa:25+hsa:613` (ABL1 + BCR) com referências cruzadas para UniProt, OMIM, HGNC.

### Reactome

- **O que é:** base de vias biológicas humanas com diagramas detalhados ("mapas de metrô" da célula).
- **URL:** https://reactome.org/
- **Aulas:** `2026-04-08`, `2026-05-11`, `2026-05-20`, `2026-05-25`
- **Uso:** análise de enriquecimento via DAVID e extração de conjuntos de proteínas participantes (ex.: pathway **R-HSA-1474228** — organização da matriz extracelular). Na aula de 11/05, navegação da via R-HSA-5684996 (MAPK1/MAPK3 signaling) como exemplo de pathway detalhado para B-RAF/melanoma. Na aula de 20/05, navegação da via R-HSA-70326 (*glucose metabolism* — glicólise e gliconeogênese) como exemplo de **encadeamento de reações catalisadas por enzimas** dentro da metabolômica. Reapresentado em 25/05 no deck *Omics and Language Models*.

### WikiPathways

- **O que é:** plataforma colaborativa de curadoria de vias biológicas (estilo Wikipedia).
- **URL:** https://www.wikipathways.org/
- **Aulas:** `2026-04-08`, `2026-05-20`, `2026-05-25`
- **Uso:** terceira fonte de vias no enriquecimento via DAVID. Na aula de 20/05, download do arquivo **GMT** (`wikipathways-20251010-gmt-Homo_sapiens.gmt`) com **332 KB** de vias humanas — cada linha lista os genes de uma via — usado como entrada para gerar embeddings de vias (Document Embedding no Orange) e construir grafos bipartidos pathway↔gene no Cytoscape. Reapresentado em 25/05 como tarefa "Pathways in Space" — construir grafo bipartido `pathway↔gene` e plotar scatter colorido por cluster. Outros formatos disponíveis: GPML (XML), SVG, SPARQL, R, Python.

### Gene Ontology (GO)

- **O que é:** vocabulário controlado que classifica genes em três eixos — processo biológico, função molecular, componente celular.
- **URLs:** https://geneontology.org/ · Navegador: https://www.ebi.ac.uk/QuickGO/ · Navegador AmiGO: https://amigo.geneontology.org/ · Endpoint SPARQL: https://geneontology.org/sparql
- **Aulas:** `2026-02-23`, `2026-02-25`, `2026-03-04`, `2026-03-09`, `2026-04-08`, `2026-04-15`, `2026-05-11`
- **Uso:** anotação funcional de genes e análise de enriquecimento (termos GO sobre-representados em listas de genes). Na aula de 11/05, exemplo detalhado de hierarquia GO para `cell adhesion` (GO:0007155) → `cell-cell adhesion` (GO:0098609) → `cell-cell adhesion mediated by cadherin` (GO:0044331), com IDs estáveis e arestas tipadas (`is a`, `part of`, `regulates`).

### DAVID (Database for Annotation, Visualization and Integrated Discovery)

- **O que é:** ferramenta de enriquecimento funcional que integra KEGG, Reactome, WikiPathways e GO em um mesmo teste de sobre-representação[^ora].
- **URL:** https://davidbioinformatics.nih.gov/
- **Aulas:** `2026-02-25`, `2026-03-04`, `2026-04-08`, `2026-04-15`
- **Uso:** dado uma lista de genes, DAVID retorna vias/termos GO enriquecidos com p-valor (teste exato de Fisher). Na aula de miRNAs, usado para enriquecer alvos dos 12 miRNAs mais expressos do locus DLK1-DIO3.

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
- **Aulas:** `2026-04-13`, `2026-05-11`
- **Uso:** citado como fonte de associações doença-gene (IDs OMIM referenciados nas redes de Zhou/Goh). Na aula de 11/05, exemplos `OMIM:608232` (LEUKEMIA, CHRONIC MYELOID) e `OMIM:189980` (ABL1 PROTOONCOGENE) — mostra como OMIM ancora genes (via HGNC) a fenótipos.

### Disease Ontology (DOID)

- **O que é:** ontologia que organiza doenças humanas em hierarquia de subclasses (`is a`), com IDs estáveis no formato `DOID:N`. Integra códigos ICD, OMIM, MeSH, EFO, KEGG.
- **URL:** https://disease-ontology.org/
- **Aulas:** `2026-05-11`
- **Uso:** exemplo central da aula sobre **surrogates** — `DOID:8552` (Chronic Myeloid Leukemia) → `DOID:8692` (Myeloid Leukemia) → leukemia → hematologic cancer → cancer → disease. Cada nó tem URI estável (`https://disease-ontology.org/?id=DOID:8552`) com referências cruzadas para EFO, GARD, ICD9CM, ICDO, KEGG, OMIM, ORDO, SNOMED, UMLS.

### HGNC (HUGO Gene Nomenclature Committee)

- **O que é:** comitê que padroniza **símbolos oficiais de genes humanos** (ex.: ABL1, BRAF). Cada gene recebe um HGNC ID estável (`HGNC:76` = ABL1).
- **URL:** https://www.genenames.org/
- **Aulas:** `2026-05-11`
- **Uso:** ponte entre OMIM, KEGG e UniProt — todos referenciam o **símbolo HGNC aprovado** para garantir que estão falando do mesmo gene.

### BacDive (Bacterial Diversity Metadatabase)

- **O que é:** maior base de dados de cepas bacterianas padronizada — 99.392 cepas com taxonomia, morfologia, fisiologia, isolamento ambiental, segurança e sequência 16S. Mantida pelo DSMZ (Coleção alemã de microrganismos).
- **URL:** https://beta.bacdive.dsmz.de/
- **Aulas:** `2026-05-11`
- **Uso:** fonte de dados para o exercício de construção de Knowledge Graph de bactérias (Gram, morfologia, taxonomia até Família/Filo). Exemplo navegado em aula: *Escherichia coli* (BacDive ID 4907) com classificação Pseudomonadota → Gammaproteobacteria → Enterobacterales → Enterobacteriaceae → *E. coli*.

### EOL (Encyclopedia of Life)

- **O que é:** enciclopédia colaborativa de biodiversidade — agrega taxonomia, descrição, mídia, traits quantitativos e relações tróficas para ~2 milhões de espécies.
- **URL:** https://eol.org/
- **Aulas:** `2026-05-11`
- **Uso:** fonte de dados para predição em redes tróficas (revisita L1 — How Wolves Change Rivers). Exemplo navegado em aula: *Canis lupus* (Gray Wolf, EOL page 328607) com **Trophic Web** mostrando predadores, presas e competidores; **Data Search** estruturada permitindo consultas tipo "*Canis* que predam roedores com massa entre 100–1000 g".

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
- **Aulas:** `2026-03-09`, `2026-04-06`, `2026-05-11`
- **Uso:** exemplo geral de grafo de conhecimento (não específico de saúde). Na aula de 11/05, contrasta a página Wikipedia `BRAF_(gene)` com a página DBpedia `dbpedia.org/page/BRAF_(gene)` que expõe as propriedades de forma estruturada (`dbo:description`, `dbo:wikiPageExternalLink`).

### BioPortal

- **O que é:** portal da NCBO (National Center for Biomedical Ontology) que agrega centenas de ontologias biomédicas com navegação e endpoints REST/SPARQL.
- **URL:** https://bioportal.bioontology.org/
- **Aulas:** `2026-05-11`
- **Uso:** consulta das propriedades de relacionamento usadas em DOID (`https://bioportal.bioontology.org/ontologies/DOID?p=properties`), incluindo a relação `is_a` do **Relations Ontology (RO)** com URI `http://purl.obolibrary.org/obo/RO#_is_a`.

---

## 6. Bases de Referência de Genes, Proteínas e Genomas

### NCBI (Entrez, RefSeq, Gene)

- **O que é:** conjunto de bases do NCBI com sequências de referência (RefSeq), identificadores únicos de genes (Entrez ID) e anotações.
- **URL:** https://www.ncbi.nlm.nih.gov/
- **Aulas:** `2026-03-02`, `2026-03-04`, `2026-04-08`, `2026-05-11`
- **Uso:** mapeamento de símbolos de gene para identificadores estáveis usados no DAVID e outros. Na aula de 11/05, exemplo `gene/999` (CDH1, cadherin 1) como gene anotado em GO:0044331 (cell-cell adhesion mediated by cadherin).

### UniProt

- **O que é:** base de referência para proteínas (sequência, função, domínios, modificações). Expõe **endpoint SPARQL** em `https://sparql.uniprot.org/`.
- **URL:** https://www.uniprot.org/
- **Aulas:** `2026-04-08`, `2026-04-01`, `2026-05-11`
- **Uso:** IDs UniProt aparecem nos mapeamentos STRING e em listas de proteínas de vias Reactome. Na aula de 11/05, central ao caso B-RAF (`uniprot:P15056`) e ABL1 (`uniprot:P00519`); aula traz consulta SPARQL completa para encontrar **paralogs de B-RAF via OrthoDB** (KSR1, KSR2, A-RAF, C-RAF).

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
- **Aulas:** `2026-02-23`, `2026-05-20`, `2026-05-25`
- **Uso:** citada no contexto de modelos de linguagem para proteínas (ESM treinado em ~19 mil famílias Pfam). Na aula de 20/05 e reapresentada em 25/05, **ProGen** (Madani et al. 2023) é apresentado como protein language model treinado em **280 milhões de sequências e 19 mil famílias Pfam** — gera proteínas artificiais funcionais quando *condicionado* por uma tag de família (Immunoglobulin, Chorismate mutase, Glucosaminidase, Phage lysozyme).

### Ensembl BioMart

- **O que é:** ferramenta de *data-mining* do **Ensembl** que permite **exportar datasets customizados** sobre genomas vertebrados — dado um conjunto de filtros (lista de genes, região, fenótipo, GO term) e atributos (sequência, posição, ID em outras bases), gera uma tabela ou FASTA.
- **URL:** https://www.ensembl.org/biomart/ (também acessível em https://www.ensembl.org/ → menu *BioMart*)
- **Aulas:** `2026-05-20`, `2026-05-25`
- **Uso:** pipeline central da aula de modelos de linguagem para biologia — partindo de uma lista de genes (ex.: PLA2G4C, JMJD7, STMN1, NFKB1, RELA, MAPK1, MAPK3, BRAF...), seleciona-se o dataset **Human genes (GRCh38.p14)**, marca-se *Ensembl Canonical: Only* e exporta-se a **sequência peptídica** + nome do gene como **FASTA**. O FASTA serve de entrada para o Clinical BERT Embeddings (gerar embeddings de proteínas). Variante: filtrar por **miRBase transcript name** (`hsa-miR-6766-3p` etc.) ou **miRBase accession** (`MI0000060`) para baixar sequências de miRNAs. Reapresentado em 25/05 no deck *Omics and Language Models*.

### Clinical BERT Embeddings (Hugging Face Space)

- **O que é:** Space público no Hugging Face do prof. André Santanchè que **gera embeddings** de texto clínico ou sequências biológicas (CSV ou FASTA) usando modelos pré-treinados (**ProteinBERT**, **Clinical BERT** etc.) com diferentes estratégias de pooling (Mean, CLS, Max).
- **URL:** https://huggingface.co/santanche — seis spaces ativos: **Clinical NER Pipeline Comparison**, **Clinical Ner**, **Clinical Embedding**, **Sentiment Analysis Oid**, **Factory ML**, **Cancer Predictor**.
- **Aulas:** `2026-05-20`, `2026-05-25`
- **Uso:** segunda etapa do pipeline iniciado em BioMart — recebe um arquivo FASTA com sequências peptídicas (ou CSV de texto), aplica ProteinBERT com pooling Mean e devolve um **CSV com um vetor de embedding por sequência**. O CSV é importado no Orange para visualização (scatter colorido por cluster) ou no Cytoscape (atributos de nó). Na aula de 25/05, demonstração ao vivo do *Clinical Embedding* com frases polissêmicas (`cold` médico vs. ambiente, `depression` clínica vs. geográfica) mostra que **Clinical BERT** distingue os contextos enquanto **Word2Vec** colapsa-os no mesmo vetor.

### CARBON (HuggingFaceBio / CARE)

- **O que é:** **foundation model genômico autorregressivo** treinado diretamente sobre sequências de DNA. Arquitetura decoder-only (estilo GPT), tokenização por **6-mers** (cada token = 6 bases), **janela de contexto de 393.216 BP** (~393 kb) e **1 trilhão de tokens** de treino. Permite gerar sequências artificiais de DNA, prever variantes e completar regiões — analogamente a como Llama completa texto, mas no espaço do genoma.
- **URL:** https://huggingface.co/spaces/HuggingFaceBio/carbon-demo (Space interativo com abas DNA Lab, Carbon Recipe e Sandbox)
- **Aulas:** `2026-05-25`
- **Uso:** apresentado como exemplo de **language model aplicado a DNA** — fechamento do paralelo "Language Model → Protein Sequences (ProGen) → DNA Sequences (CARBON)". Demonstra que a mesma arquitetura decoder-only que gera texto pode aprender a gramática do genoma.

---

## 7. Drug-Target / Associação Fármaco-Doença

### Open Targets Platform

- **O que é:** plataforma que agrega evidências que ligam alvos (genes/proteínas) a doenças, combinando genética, expressão, patologia, literatura e ensaios clínicos.
- **URL:** https://platform.opentargets.org/
- **Aulas:** `2026-04-01` (exercício)
- **Uso:** arquivo `OT-MONDO_0007254-associated-targets-01_04_2026-v26_03.tsv` — alvos associados ao câncer de mama (MONDO_0007254) baixados da plataforma.

---

## 7b. Bases e Ferramentas de microRNAs

### miRBase

- **O que é:** banco de dados central de sequências e anotações de microRNAs — nomenclatura oficial (`hsa-miR-485-5p`, `cel-let-7` etc.), sequências pre- e maduras, homologias entre espécies.
- **URL:** https://mirbase.org/
- **Aulas:** `2026-04-15`, `2026-04-29`
- **Uso:** referência para identificar miRNAs mencionados na literatura e recuperar suas sequências. Na aula de 29/04, download do arquivo `miRNA.xls` (release 22.1) usado como tabela De-Para entre **MIMAT IDs** (saída do FireBrowse/miRWalk) e nomes canônicos (`hsa-miR-...`).

### TargetScan

- **O que é:** preditor de alvos de miRNAs baseado em *seed region* e conservação evolutiva. Variantes por organismo (TargetScanHuman, Mouse, Worm, Fly, Fish).
- **URL:** https://www.targetscan.org/
- **Referências:** Agarwal et al. (2015); McGeary, Lin et al. (2019).
- **Aulas:** `2026-04-15`
- **Uso:** dado um miRNA, retorna lista de mRNAs-alvo conservados com *context score*. Ex.: let-7/98 → 819 alvos conservados (HMGA2, LIN28B, IGF2BP1, TRIM71…).

### miRWalk

- **O que é:** plataforma que agrega predições de múltiplos algoritmos (12) de alvos de miRNA.
- **URL:** http://mirwalk.umm.uni-heidelberg.de/
- **Aulas:** `2026-04-15`, `2026-04-29`
- **Uso:** predição de alvos complementar ao TargetScan. Na aula de 15/04, geração da lista de ~1.200 mRNAs-alvo dos miRNAs do locus DLK1-DIO3. Na aula de 29/04, exercício de **Target Mining** com lista de MIMAT IDs diferencialmente expressos no THCA, com filtro por `miRTarBase` para reter só interações experimentalmente validadas e exportação como CSV.

### miRTarBase

- **O que é:** banco de dados de interações miRNA-alvo **validadas experimentalmente** (luciferase reporter, Western blot, microarray, qPCR, CLIP-seq etc.) — diferente de TargetScan/miRWalk, que apenas predizem.
- **URL:** https://mirtarbase.cuhk.edu.cn/
- **Aulas:** `2026-04-29`
- **Uso:** filtro `miRTarBase` aplicado na tabela de saída do miRWalk para reter só pares miRNA-mRNA com evidência de bancada — antes de exportar a lista de arestas para a rede miRNA-mRNA do THCA.

### Firehose / Broad GDAC

- **O que é:** plataforma do Broad Institute que arquiva e versiona os dados pré-processados do TCGA. Funciona como o "atacadão congelado" do TCGA — *snapshots* completos prontos para download em massa, com checksums MD5.
- **URL:** https://gdac.broadinstitute.org/
- **Aulas:** `2026-04-29`
- **Uso:** ponto de entrada para baixar uma coorte inteira do TCGA (no caso da aula, THCA). A página lista todas as coortes (BRCA, COAD, SKCM, THCA, ...) com coluna **Browse** que abre a interface FireBrowse. Acesso CLI via `firehose_get`.

### FireBrowse

- **O que é:** interface web do Firehose para explorar uma coorte específica do TCGA — mostra contagem de alíquotas por tipo de análise (Clinical, miRSeq, mRNASeq, methylation, copy number, mutations, RPPA) e oferece download direto dos arquivos.
- **URL:** http://firebrowse.org/ (ex.: `?cohort=THCA`)
- **Aulas:** `2026-04-29`
- **Uso:** download dos arquivos `Clinical_Pick_Tier1`, `illuminahiseq_mirnaseq-miR_isoform_expression` e `illuminahiseq_rnaseqv2-RSEM_genes_normalized` para a coorte THCA. Também acessível via app `firehose_get` ou exportação para GenomeSpace.

### miTEA-HiRes

- **O que é:** ferramenta computacional que infere **atividade de miRNAs em nível de célula única ou *spot* espacial** a partir de dados de transcriptômica (Visium, scRNA-seq) — sem precisar sequenciar os próprios miRNAs.
- **Referência:** Herbst et al. (2025), *Communications Biology*, https://doi.org/10.1038/s42003-025-07454-9
- **Aulas:** `2026-04-15`
- **Uso:** mapa de atividade de miRNAs (ex.: miR-7a-1-3, miR-590-3p) em cérebro de camundongo sobreposto à histologia H&E.

---

## 7c. Bases e Ferramentas de Metabolômica e Quimioinformática

### EMBL-EBI Metabolomics Training

- **O que é:** curso online gratuito do **EMBL-EBI** introduzindo metabolômica — definição, tecnologias (MS, NMR), análise de dados, integração com outras ômicas.
- **URL:** https://www.ebi.ac.uk/training/online/courses/metabolomics-introduction/
- **Aulas:** `2026-05-20`, `2026-05-25`
- **Uso:** material de referência usado para apresentar metabolômica na aula — figuras de **omics e metabolômica** (gene → mRNA → proteína → metabólito), exemplos de **moléculas pequenas** (glicose, ácido esteárico, colesterol, lisina) e **reações metabólicas** (binding, dissociation, degradation, modification, transport). Reapresentado em 25/05.

### BioTransformer

- **O que é:** ferramenta computacional para **predição de metabolismo de pequenas moléculas** e identificação de metabólitos — dado um composto, prevê quais metabólitos podem se formar via reações enzimáticas humanas e do microbioma.
- **URL:** https://biotransformer.ca/
- **Referência:** Djoumbou-Feunang, Y., Fiamoncini, J., Gil-de-la-Fuente, A., Greiner, R., Manach, C., & Wishart, D. S. (2019). BioTransformer: A comprehensive computational tool for small molecule metabolism prediction and metabolite identification. *Journal of Cheminformatics*, 11(1), 1–25. https://doi.org/10.1186/s13321-018-0324-5
- **Aulas:** `2026-05-20`, `2026-05-25`
- **Uso:** apresentada como ferramenta para prever metabolitos a partir de moléculas-substrato — ponte entre uma reação química descrita em SMILES e seu produto biológico. Reapresentado em 25/05.

#### Dataset associado: **MetXBioDB Metabolite Biotransformations** (Kaggle)

- **Origem:** versão do banco de biotransformações que alimenta o BioTransformer, publicada como dataset no Kaggle (`thedevastator/metxbiodb-metabolite-biotransformations`).
- **URL:** https://www.kaggle.com/datasets/thedevastator/metxbiodb-metabolite-biotransformations
- **Arquivo central:** `MetXBioDB_substances.csv`.
- **Mirror local:** https://github.com/datasci4health/datasci4health.github.io/tree/master/language-model/metabolites/metaxbiodb
- **Uso:** dataset para exercícios de predição de metabolitos com modelos de linguagem aplicados a quimioinformática.

---

## 8. Ferramentas que dão acesso a dados

Não são bases em si, mas intermediam o acesso a várias bases acima:

| Ferramenta | O que acessa | Aulas |
| --- | --- | --- |
| **Cytoscape** ([cytoscape.org](https://cytoscape.org/)) | STRING, GEO, PrimeKG, Reactome, qualquer CSV/SIF de rede. Apps: STRING, clusterMaker2 (Leiden), CytoNCA, MCODE, NetworkAnalyzer. | `2026-03-09`, `2026-03-30`, `2026-04-01`, `2026-04-06`, `2026-04-08`, `2026-04-13` |
| **Orange Data Mining** ([orange.biolab.si](https://orange.biolab.si/)) | Leitura de SOFT (GEO), CSV, cálculo de correlações, pipelines visuais. | `2026-03-30`, `2026-04-01`, `2026-04-13` |
| **Dagoberto** ([datasci4health.github.io/networks/dagoberto](https://datasci4health.github.io/networks/dagoberto/)) | Visualiza redes a partir de CSVs de nós e arestas direto no navegador. | `2026-02-25`, `2026-03-09` |
| **Firehose / FireBrowse** ([gdac.broadinstitute.org](https://gdac.broadinstitute.org/) · [firebrowse.org](http://firebrowse.org/)) | Snapshots versionados do TCGA — clínicos, miRSeq, mRNAseq, methylation, CNV, mutações, RPPA. CLI: `firehose_get`. | `2026-04-29` |
| **Ensembl BioMart** ([ensembl.org/biomart](https://www.ensembl.org/biomart/)) | Exportação customizada de sequências, IDs e anotações do Ensembl (filtros por gene, miRBase ID, GO term; atributos: Peptide, Gene name, Sequence, Variants). Formatos: TSV, FASTA, XML. | `2026-05-20` |
| **Clinical BERT Embeddings** ([huggingface.co/santanche](https://huggingface.co/santanche)) | Geração de embeddings a partir de FASTA ou CSV usando ProteinBERT / Clinical BERT. Pooling: Mean, CLS, Max. Saída: CSV de vetores. | `2026-05-20` |
| **BertViz** ([github.com/jessevig/bertviz](https://github.com/jessevig/bertviz)) | Visualização interativa do **mecanismo de atenção** em modelos Transformer (cabeças, camadas, mapas de atenção entre tokens). | `2026-05-20`, `2026-05-25` |
| **GAT Attention Explorer** ([datasci4health.github.io/language-model/gat/visualizer](https://datasci4health.github.io/language-model/gat/visualizer/)) | Visualizador web dos CSVs do exercício de GAT (THCA + MAPK). Filtra por camada, hops, edge type e attention head; mostra outgoing/incoming attention por nó. Código em [github.com/datasci4health/datasci4health.github.io/.../gat](https://github.com/datasci4health/datasci4health.github.io/tree/master/language-model/gat). | `2026-05-25` |
| **CARBON** ([huggingface.co/spaces/HuggingFaceBio/carbon-demo](https://huggingface.co/spaces/HuggingFaceBio/carbon-demo)) | Foundation model genômico autorregressivo (decoder-only, 6-mer tokenizer, 393.216 BP context, 1T tokens). Permite completar/gerar sequências de DNA. | `2026-05-25` |
| **Ollama** ([ollama.com](https://ollama.com/)) | *Runtime* local de SLMs/LLMs com servidor HTTP em `localhost:11434`. Permite rodar modelos open-source em CPU/GPU local sem depender de API externa. CLI: `ollama run <modelo>`. Suporta tags como Cloud, Embedding, Vision, Tools, Thinking. | `2026-06-01` |
| **Pub/Sub Multi-Agent System** ([huggingface.co/spaces/santanche/sml-agents-publish-subscribe](https://huggingface.co/spaces/santanche/sml-agents-publish-subscribe)) | Space do prof. André Santanchè que orquestra múltiplos SLMs (rodando no Ollama local do usuário) num pipeline **publish/subscribe**. Cada agente assina um tópico, processa com um prompt template e publica em outro tópico. Suporta Data Sources (com subscribe → vira **Memory**) e human-in-the-loop. Backup: [santanche.github.io/lab2learn/machine-learning/agents](https://santanche.github.io/lab2learn/machine-learning/agents/). | `2026-06-01` |
| **MedGemma 1.5** ([deepmind.google/models/gemma/medgemma](https://deepmind.google/models/gemma/medgemma/) · Ollama: [`MedAIBase/MedGemma1.5`](https://ollama.com/MedAIBase/MedGemma1.5)) | SLM **4B** da DeepMind otimizado para texto e imagem médica (raio-X, CT, MRI, histopatologia), fine-tune do Gemma. Tag `4b` recomendada (a `4b-it-q4_0` apresenta overfitting). Usado como Health Extractor Agent. | `2026-06-01` |
| **DeepSeek Coder** ([deepseekcoder.github.io](https://deepseekcoder.github.io/) · Ollama: [`deepseek-coder`](https://ollama.com/library/deepseek-coder)) | Família de SLMs treinada do zero em **87% código + 13% NL** com 2T tokens. Tamanhos: 1.3B / 6.7B / 33B. Usado na aula como JSON Generator Agent (1.3B). | `2026-06-01` |
| **Phi-4 Mini / PhiCookBook** ([github.com/microsoft/PhiCookBook](https://github.com/microsoft/PhiCookBook) · Ollama: [`phi4-mini`](https://ollama.com/library/phi4-mini)) | Família Phi da Microsoft (licença MIT) com seis trilhas: Language, Coding, Vision, Audio, Advanced Reasoning, MoE. **`phi4-mini` (3.8B)** suporta function calling e multilíngue. Disponível em HF, Ollama, NVIDIA NIM, AITK, LM Studio, Azure AI Foundry, GitHub Models. Usado como JSON Validator/Comparator Agent. | `2026-06-01` |
| **Flowise** ([flowiseai.com](https://flowiseai.com/)) | Plataforma open-source de **agentic workflow** no-code — nós tipados (Start, Detect User Intention, Agent) ligando modelos comerciais e open-source (gpt-4.1, gemini-2.0-flash, claude-3-7-sonnet-latest, gpt-4o-mini). | `2026-06-01` |
| **Computer tldraw** ([computer.tldraw.com](https://computer.tldraw.com/)) | Ferramenta visual no-code em que cada caixa do canvas (Frame, Instruction, Text, Image, Speech) é uma chamada a um modelo. Exemplo: borboleta → história → review → áudio. | `2026-06-01` |
| **Orange LMSci** (plugin do Orange) | Widget `LM Task` do Orange que invoca SLM via Ollama (`http://localhost:11434`) usando um prompt template com placeholders `{column_name}` para colunas da tabela de entrada. Saída como texto ou nova coluna na tabela. | `2026-05-25`, `2026-06-01` |

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
| `2026-05-13` | `microRNA/cytoscape/limma_pathway*/...` | Snapshots Cytoscape filtrando a rede miRNA-mRNA do THCA pela via **MAPK signaling (KEGG hsa04010)**. |
| `2026-05-13` | `microRNA/kegg/hsa04010.xml`, `hsa_genes.tsv` | KGML da via MAPK signaling do KEGG e mapeamento de genes humanos por via — usados como filtro de pathway. |
| `2026-05-13` | `microRNA/thca-mirna-mrna_limma_pathway*.ows` | Workflows Orange que adicionam ao pipeline o filtro por pertença ao pathway MAPK. |
| `2026-05-20` | `pathway-mir-mrna/mart_export.fasta` | Export do **Ensembl BioMart** com 337 peptídeos da via MAPK signaling (cabeçalhos por símbolo HGNC). |
| `2026-05-20` | `pathway-mir-mrna/mapk-gene-embeddings.csv` | **11 MB** — embeddings de proteína gerados pelo ProteinBERT/Clinical BERT sobre o FASTA do BioMart. |
| `2026-05-20` | `pathway-mir-mrna/genes-pathway-to-mirwalk.csv` | 300 genes da via MAPK (coluna `label`) prontos para submissão ao miRWalk. |
| `2026-05-20` | `pathway-mir-mrna/mir-mrna-embed.ows` | Workflow Orange que carrega o FASTA, gera embeddings e visualiza. |
| `2026-05-20` | `mapk/5684996.owl` | **Reactome BioPAX Level 3** (4,1 MB) da via *MAPK1/MAPK3 signaling* (R-HSA-5684996), exportável também por GMT, SVG, R, Python. |
| `2026-05-20` | `mapk/kegg/hsa04010.xml`, `hsa_genes.tsv` | Cópia da via MAPK signaling do KEGG e mapeamento KEGG ID → símbolo HGNC. |
| `2026-05-20` | `mapk/miRBase/miRNA.csv`, `mapk/ensembl/mir-ensembl.csv` | miRBase 22.1 (8,3 MB) e lista de 1.105 miRNAs no Ensembl para o pipeline KG + miRNA. |
| `2026-05-20` | `mapk/miRWalk/miRWalk_miRNA_Targets.csv` | 1,5 MB — alvos preditos pelo miRWalk para os 300 genes da MAPK. |
| `2026-05-20` | `mapk/cytoscape/mapk-kg{,-mir,-mir-lm}/{nodes,edges}*.csv` | Grafo de conhecimento da MAPK signaling em três camadas: (i) só genes + functional units com lógica AND/OR (423 nós), (ii) + miRNAs (1.527 nós), (iii) + clusters de language model. |
| `2026-05-20` | `mapk/clusters/mapk-gene-embeddings.csv` | 338 genes → cluster (C1..C9) — resultado da clusterização sobre os embeddings ProteinBERT. |
| `2026-05-20` | `mapk/mapk-to-kg{,-mir,-mir-lm}.ows` | Três workflows Orange encadeados: KGML → KG, KG → KG+miRNA, KG+miRNA → KG+miRNA+LM. |
| `2026-05-20` | `mapk/mapk-kg-aggregated.cys` | Sessão Cytoscape final com o grafo agregado. |
| `2026-05-25` | `gat/node_metadata.csv` | 562 nós do GAT — 300 genes (com `logFC` TCGA-THCA), 244 unidades funcionais lógicas KEGG (AND/OR), 18 miRNAs (MIMAT IDs), todos com `embedding_l2_norm` inicial via ProteinBERT. |
| `2026-05-25` | `gat/node_embeddings.csv` | **2,2 MB** — embeddings de cada nó nas **3 camadas** do GAT, cada uma com **64 dimensões** (formato long: `node_id, layer, dim_0..dim_63`). |
| `2026-05-25` | `gat/edge_metadata.csv` | 1.101 arestas: `self_loop` (562), `gene_to_fu` (322), `protein_protein_interaction` (163), `mir_to_gene` (53), com `final_layer_mean_attn` e `final_layer_max_attn`. |
| `2026-05-25` | `gat/attention_weights.csv` | Pesos de atenção das **4 cabeças** (`head_1`..`head_4` + `mean_attention`) em cada uma das 3 camadas — 3.303 linhas. |

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
| **FASTA** | `2026-05-20` | Sequências biológicas em texto plano (`>nome` + linhas com a sequência). Saída de Ensembl BioMart para peptídeos, entrada do Clinical BERT Embeddings. |
| **OWL / BioPAX Level 3** | `2026-05-20` | Ontologia RDF/XML — formato com que Reactome distribui vias como instâncias `bp:Pathway`, `bp:BiochemicalReaction`, `bp:Protein` etc. Usado para `5684996.owl` (MAPK1/MAPK3 signaling). |
| **KGML** | `2026-05-13`, `2026-05-20` | XML do KEGG para uma via — descreve entries (genes, compostos), relations e reactions. Arquivo `hsa04010.xml`. |
| **GAT outputs (CSV plano)** | `2026-05-25` | Saída de Graph Attention Network: `node_metadata.csv` (metadados), `node_embeddings.csv` (vetores 64-dim por camada), `edge_metadata.csv` (arestas + atenção final), `attention_weights.csv` (atenção por cabeça × camada). |

---

## Resumo por Categoria

- **Interação proteína-proteína:** STRING (principal), BioGRID, IntAct, MINT, BIND, HPRD, DIP
- **Vias / Função:** KEGG, Reactome, WikiPathways, Gene Ontology (+ DAVID como integrador)
- **Expressão gênica e câncer:** GEO (dataset-chave das aulas: **GSE45827**), TCGA (coorte-chave: **TCGA-THCA**, via Firehose/FireBrowse)
- **microRNAs:** miRBase, TargetScan, miRWalk, miRTarBase, miTEA-HiRes
- **Metabolômica e quimioinformática:** EMBL-EBI Metabolomics, BioTransformer, MetXBioDB
- **Grafos de conhecimento:** Rede Zhou 2014 (sintoma-doença), Diseasome, PrimeKG
- **Ontologias:** GO, **DOID**, MeSH, MONDO, WordNet, DBpedia, BioPortal (agregador)
- **Referência genômica/proteica:** NCBI (Entrez/RefSeq), UniProt, UCSC, Pfam, **Ensembl BioMart**, **HGNC**
- **Modelos de linguagem para biologia:** **Clinical BERT Embeddings** (Hugging Face), **BertViz**, **CARBON** (genomic foundation model), **GAT Attention Explorer** (visualizador), ProGen (referenciado), ProteinBERT (referenciado)
- **SLMs locais e orquestração de agentes:** **Ollama** (runtime), **MedGemma 1.5** (clínico), **DeepSeek Coder** (código), **Phi-4 Mini** (propósito geral, raciocínio), **Pub/Sub Multi-Agent System** (santanche), **Flowise** (workflow), **Computer tldraw** (visual), **Orange LMSci** (plugin Orange)
- **Fármaco-alvo:** Open Targets
- **Literatura:** PubMed
- **Microbiologia / Biodiversidade:** BacDive (cepas bacterianas), EOL (Encyclopedia of Life)

**Datasets do projeto semestral (referidos no [README do projeto](projeto/README.md)):** GSE4570, GSE2503, GSE53462, GSE8401, GSE7553, GSE45216 (melanoma/não-melanoma/pele saudável) e TCGA-SKCM (projeto GAT — TCGA também aparece em aula; ver seção 2).

---

[^expr]: **Expressão gênica** — o quanto um gene está sendo "lido" pela célula para produzir proteína. Medir expressão de milhares de genes em várias amostras gera uma matriz de expressão.
[^ora]: **Over-Representation Analysis (ORA)** — testa se termos (ex.: vias KEGG) aparecem mais vezes numa lista de genes do que seria esperado por acaso. Teste típico: exato de Fisher.
[^tfidf]: **TF-IDF** — *Term Frequency – Inverse Document Frequency*. Peso que valoriza termos frequentes em um documento, mas raros no corpus geral. Zhou (2014) usou isso para medir a força da associação doença-sintoma em artigos do PubMed.

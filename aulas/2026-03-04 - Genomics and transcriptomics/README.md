# Genômica e Transcriptômica

[slides](slides.pdf) | [YouTube](https://www.youtube.com/watch?v=lI1nm7oQE8E)


**Disciplina:** Biologia Molecular e Celular
**Docente:** Murilo V. Geraldo — Dep. Biologia Estrutural e Funcional, Instituto de Biologia, UNICAMP

---

## Dogma Central da Biologia Molecular

O fluxo de informação genética segue a sequência clássica:

- **DNA** → (transcrição) → **RNA** → (tradução) → **Proteína**
- O DNA também sofre replicação, reparo e recombinação genética.
- Um mesmo gene pode originar diferentes quantidades de mRNA e proteína dependendo do tipo celular e do contexto biológico (ex.: embrião, pele, neurônio).

---

## As "Ômicas"

As tecnologias "ômicas" permitem estudar em larga escala as moléculas de cada nível do dogma central:

| Molécula    | Disciplina ômica                       |
| ----------- | -------------------------------------- |
| DNA         | Genômica, Epigenômica                  |
| RNA         | Transcriptômica                        |
| Proteínas   | Proteômica (Surfaceômica, Secretômica) |
| Metabólitos | Metabolômica                           |

---

## Genômica

### Genoma de Referência e Browsers

- O genoma humano é organizado em cromossomos e anotado em bancos de dados públicos.
- O **UCSC Genome Browser** (genome.ucsc.edu) permite visualizar genes, transcritos, elementos conservados e variantes em qualquer região do genoma (ex.: gene _BRAF_ no cromossomo 7).
- Anotações incluem: GENCODE, RefSeq (NCBI), MANE Select (transcrito representativo consenso RefSeq/GENCODE) e conservação em vertebrados (PhyloP).

### Sequenciamento de Próxima Geração (NGS — Next-Generation Sequencing)

- Plataformas NGS geram **milhões de reads** (sequências curtas) em paralelo por meio de **sequenciamento em array cíclico** (_cyclic array sequencing_): a cada ciclo, uma base fluorescente é incorporada e identificada.
- Os reads são armazenados no formato **FASTQ**, que contém:
  - Label (identificador)
  - Sequência de nucleotídeos
  - Escore de qualidade Q (caracteres ASCII); ex.: Base T, Q=25
- **Montagem do genoma:** os milhões de reads curtos são alinhados ao **genoma de referência** por análise bioinformática, gerando uma sequência consenso que permite identificar variantes.

### DNA-Seq: Aplicações em Genômica

- **Detecção de mutações (SNVs/SNPs):** reads alinhados ao genoma de referência revelam substituições de bases (ex.: gene _MYH7_, variante p.Y162H confirmada simultaneamente por NGS e sequenciamento de Sanger).
- **Variação no número de cópias (CNV):** diferenças na profundidade de cobertura entre amostras indicam amplificação ou deleção de regiões (ex.: amplificação do gene A na Amostra A vs. gene B na Amostra B).
- **Rearranjos cromossomiais em câncer:** reads híbridos que mapeiam simultaneamente em dois cromossomos distintos (chr1 e chr2) evidenciam fusões gênicas ou translocações.
- **Visualização circular (Circos plot):** representa variantes, CNVs e rearranjos ao longo de todos os cromossomos simultaneamente.

---

## Transcriptômica

### Conceito

A transcriptômica estuda o conjunto de todos os RNAs expressos (o **transcriptoma**) em um determinado tipo celular, condição ou momento biológico. Diferentemente do genoma (estático), o transcriptoma é dinâmico.

### Níveis de Controle da Expressão Gênica

A expressão gênica é regulada em múltiplos níveis:

1. **Controle transcricional** — transcrição, metilação do DNA, modificações de histonas
2. **Processamento do RNA** — splicing, capping, poliadenilação
3. **Transporte e sublocalização celular** do mRNA
4. **Degradação do mRNA** — regulação por microRNAs (pós-transcricional)
5. **Controle traducional** — eficiência de tradução
6. **Controle pós-traducional** — fosforilação, glicosilação, sulfonação, geranilação, isoprenilação, palmitoilação

### RNA-Seq (Sequenciamento de Transcriptoma)

- Utiliza a mesma plataforma NGS do DNA-Seq, mas a partir de RNA convertido em cDNA.
- Permite quantificar a expressão de todos os genes simultaneamente e identificar genes **diferencialmente expressos (DE)** entre condições experimentais.

---

## Análise de Expressão Diferencial e Bioinformática

### O Problema da Escala

Experimentos de transcriptômica podem revelar **milhares de genes diferencialmente expressos**, levantando a questão: como interpretar essa informação biologicamente?

### Anotação Funcional e Enriquecimento de Vias

- A sequência de DNA → RNA → proteína permite inferir a **função** de um gene por homologia com proteínas conhecidas.
- Ferramentas como o **DAVID** (david.ncifcrf.gov) realizam análise de enriquecimento funcional: dado um conjunto de genes DE, verifica-se quais **vias (pathways)** e termos de **Gene Ontology (GO)** estão sobre-representados estatisticamente.
- Lógica do enriquecimento: se uma via contém 300 genes (1% do genoma ~30.000 genes) e em uma lista de 1.500 genes DE observa-se 12 genes dessa via (esperado: 15), calcula-se o desvio estatístico. Vias com mais genes observados do que o esperado são consideradas enriquecidas.

### Gene Ontology (GO)

- Termos GO classificam genes em categorias de **processo biológico**, **função molecular** e **componente celular**.
- Exemplo de resultado: miRNAs do locus DLK1-DIO3 enriquecem termos como organização de matriz extracelular, adesão celular, angiogênese e regulação de apoptose.

### KEGG Pathways

- O banco **KEGG** (kegg.jp) fornece mapas de vias de sinalização (ex.: via NF-kB) onde genes diferencialmente expressos podem ser sobrepostos visualmente, permitindo identificar nós regulatórios críticos.
- Exemplo: em carcinoma anaplásico de tireoide (ATC), genes da via NF-kB apresentam expressão muito elevada; o miR-654-3p regula negativamente _IRAK1_ nessa via tanto em carcinoma papilífero (PTC) quanto em ATC.

---

## Proteômica

- Estuda o conjunto de proteínas expressas em uma amostra.
- Fluxo de trabalho típico: células/tecido → mistura de proteínas → separação (gel 1D) → digestão em peptídeos → cromatografia líquida → ionização por electrospray → espectrometria de massas em tandem (MS/MS) → identificação de sequências peptídicas pelo espectro m/z.

---

## Biologia de Sistemas (Systems Biology)

- Integra dados de múltiplas camadas ômicas (genômica, transcriptômica, proteômica, metabolômica) para compreender o comportamento emergente de redes biológicas.
- Redes de interação proteína-proteína (ex.: STRING) identificam hubs e módulos funcionais enriquecidos em vias específicas.
- Circuitos celulares relevantes incluem: circuitos de proliferação (Ras, Myc, receptores tirosina-quinase), motilidade (E-caderina, integrinas, β-catenina), citostasia/diferenciação (p16, Rb, Smads) e viabilidade (Bcl-2, p53).

---

## Aplicação Clínica: microRNAs como Biomarcadores

### Reprodução Humana Assistida

Estudo de caso do próprio grupo (Geraldo/UNICAMP — Mulato et al., 2023):

- **Contexto:** mulheres submetidas a Estimulação Ovariana Controlada (EOC) para ciclos de ICSI podem apresentar resposta pobre (PR), normal (NR) ou exacerbada/hiperestimulação (HR).
- **Abordagem:** microTranscriptoma do soro periférico **pré-estímulo** → identificação de miRNAs diferencialmente expressos entre PR, NR e HR → validação experimental individual.
- **Resultado:** painel de miRNAs séricos capaz de predizer a resposta ovariana antes do tratamento (ex.: hsa-miR-181d-5p com fold change de 52,99 em HR vs. NR; AUC = 0,739; p = 0,002 na curva ROC).
- **Vias enriquecidas:** sinalização de estrógeno, prolactina, GnRH, ErbB, MAPK, maturação de oócitos — confirmando relevância biológica dos alvos dos miRNAs identificados.

---

## Conceitos-Chave Resumidos

| Conceito              | Definição breve                                                                    |
| --------------------- | ---------------------------------------------------------------------------------- |
| NGS                   | Sequenciamento massivo paralelo; gera milhões de reads curtos                      |
| FASTQ                 | Formato de arquivo com sequência + escore de qualidade (Q score)                   |
| Alinhamento           | Mapeamento de reads ao genoma de referência                                        |
| SNV/SNP               | Variante de nucleotídeo único; detectada por profundidade de cobertura             |
| CNV                   | Variação no número de cópias; detectada por diferença de cobertura                 |
| Transcriptoma         | Conjunto de RNAs expressos em uma condição                                         |
| Expressão diferencial | Genes com expressão significativamente diferente entre condições                   |
| Gene Ontology         | Sistema de classificação funcional de genes em termos padronizados                 |
| Enriquecimento (GSEA) | Teste estatístico para identificar vias sobre-representadas em uma lista de genes  |
| miRNA                 | Pequeno RNA não-codificante (~22 nt) que regula pós-transcricionalmente genes-alvo |
| Biologia de Sistemas  | Integração de dados ômicos para modelar redes e circuitos biológicos               |

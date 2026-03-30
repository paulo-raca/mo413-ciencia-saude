# Biologia Celular e Molecular

[slides](slides.pdf) | [YouTube](https://www.youtube.com/watch?v=V0h4nsmtv2g)


**Fonte:** Aula de Murilo V. Geraldo — Dep. Biologia Estrutural e Funcional, Instituto de Biologia, UNICAMP

---

## Dogma Central da Biologia Molecular

O Dogma Central, proposto por Francis Crick em 1958, descreve o fluxo de informação genética:

- **DNA → RNA → Proteína**
- O DNA é replicado (DNA → DNA), transcrito em RNA e o RNA é traduzido em proteína
- A **transcrição reversa** (RNA → DNA) é possível (ex.: retrovírus), mas a informação nunca flui a partir de proteínas
- O fenótipo de um organismo resulta da combinação de proteínas, carboidratos, lipídios e metabólitos produzidos pela célula

---

## Gene: Definição e Estrutura

- **Gene:** segmento de DNA transcrito em RNA, que pode ou não ser traduzido em proteína
- **Código genético ≠ Genoma:** o código genético é o conjunto de regras de tradução (universal para todos os organismos); o genoma é o conjunto haploide de moléculas de ácido nucleico característico de um organismo
- **Expressão gênica** = quantidade de transcritos produzidos a partir de um gene

### Estrutura de um gene eucariótico

- **Promotor** e **Operador:** regiões regulatórias upstream (à montante) que controlam o início da transcrição
- **Éxons:** regiões codificantes do gene
- **Íntrons:** regiões não codificantes intercaladas entre os éxons (removidas por splicing)
- **5'UTR e 3'UTR:** regiões não traduzidas nas extremidades do mRNA
- **Códon de início (AUG/Met)** e **códon de parada (UAA, UAG, UGA)**
- **Fita molde:** a fita de DNA lida pela RNA polimerase (3'→5'); a **fita codificadora** tem a mesma sequência do RNA produzido (exceto T→U)

---

## Código Genético

- É formado por **códons** de três nucleotídeos (tripletos)
- É **universal** (compartilhado por todos os organismos conhecidos)
- É **degenerado:** vários códons podem codificar o mesmo aminoácido
- **AUG** = códon de iniciação (Metionina)
- **UAA, UAG, UGA** = códons de parada
- Decifrado por Marshall Nirenberg e colaboradores (Nobel de Fisiologia/Medicina, 1968)

---

## Genoma

- Conjunto haploide de moléculas de ácido nucleico características de um organismo (específico por espécie)
- Tamanhos comparativos:
  - _E. coli_: ~5 Mbp
  - _H. sapiens_: ~3,2 Gbp
  - _Ambystoma mexicanum_ (axolote): ~32 Gbp (maior que o humano)
- O tamanho do genoma não se correlaciona diretamente com a complexidade do organismo
- O genoma humano possui 46 cromossomos (23 pares) e pode ser explorado em bases de dados como o **UCSC Genome Browser** (genome.ucsc.edu)

---

## Transcrição

### Etapas do processamento do RNA em eucariotos

1. **Iniciação da transcrição** pela RNA polimerase no promotor
2. **Capping** (adição de cap 5') e **elongação** da fita de RNA
3. **Splicing:** remoção dos íntrons e junção dos éxons
4. **Clivagem e poliadenilação:** adição da cauda poli-A (AAAA...) na extremidade 3'
5. **Exportação** do mRNA maduro para o citoplasma
6. No citoplasma: **tradução** pelos ribossomos ou **degradação** do mRNA

### Fita molde vs. fita codificadora

- Diferentes genes no mesmo cromossomo podem ser transcritos em direções opostas, utilizando diferentes fitas como molde

---

## Regulação da Expressão Gênica

A expressão gênica pode ser controlada em múltiplos níveis:

1. **Controle transcricional:** transcrição do DNA em RNA primário
   - Envolve metilação do DNA, modificações de histonas e fatores de transcrição
2. **Controle pós-transcricional:** processamento do RNA, splicing alternativo, transporte e sublocalização do mRNA
3. **Controle traducional:** regulação da tradução do mRNA
4. **Controle pós-traducional:** modificações da proteína (fosforilação, glicosilação, sulfonação, geranilação, isoprenilação, palmitoilação)
5. **microRNAs (miRNAs):** pequenos RNAs não codificantes que promovem a degradação ou repressão da tradução de mRNAs-alvo

### Elementos regulatórios no DNA

- **Elementos cis-atuantes:** sequências regulatórias próximas ou distantes do gene alvo (enhancers, silencers)
- **Elementos isoladores (insulators):** delimitam domínios de cromatina ativamente transcritos, impedindo que elementos regulatórios de um gene afetem genes vizinhos
- **Heterocromatina vs. Eucromatina:** regiões condensadas (inativas) vs. abertas (ativas) da cromatina

### Estrutura tridimensional da cromatina

- O genoma possui organização espacial no núcleo (territórios cromossômicos)
- Domínios ativos tendem a localizar-se na superfície do território cromossômico
- LADs (Lamin-Associated Domains) tendem a localizar-se na periferia nuclear e são enriquecidos em regiões silenciosas

---

## Vias de Sinalização Celular

As células se comunicam por meio de moléculas sinalizadoras que ativam cascatas intracelulares:

- **Ligante** liga-se ao **receptor** na membrana plasmática
- O sinal é transmitido por **proteínas sinalizadoras intracelulares** (2os mensageiros)
- As **proteínas efetoras** executam a resposta: alteram o metabolismo, a expressão gênica ou a forma/movimento celular

### Via RAS-RAF-MEK-ERK (MAPK)

- Ativada por fatores de crescimento via RTKs (receptores tirosina quinase)
- Regula crescimento e divisão celular
- **Mutações em K-RAS:** presentes em 1/4 a 1/3 dos carcinomas de pulmão; coexiste frequentemente com mutações em TP53
- **Mutações em B-RAF:** presentes em 62% dos carcinomas papilares de tiroide e 70% dos melanomas; associadas a pior prognóstico
- **Rearranjos RET/PTC:** presentes em 15-20% dos carcinomas papilares de tiroide

### Vias como alvos terapêuticos

- Inibidores de B-RAF (ex.: PLX4032/Vemurafenibe) promovem regressão tumoral em melanomas com mutação BRAF
- O banco de dados **KEGG** (kegg.jp) mapeia vias metabólicas e de sinalização

### Via NF-kB

- Ativada por citocinas (TNF-α, IL-1), antígenos, vírus e agentes genotóxicos
- Regula sobrevivência celular, inflamação e resposta imune
- Apresenta vias canônica, atípica e não canônica

---

## "OMICS": Abordagens em Larga Escala

| Molécula    | Campo                                  |
| ----------- | -------------------------------------- |
| DNA         | Genômica, Epigenômica                  |
| RNA         | Transcriptômica                        |
| Proteínas   | Proteômica (Surfaceômica, Secretômica) |
| Metabólitos | Metabolômica                           |

---

## Genômica e Transcriptômica

### Sequenciamento de Nova Geração (NGS)

- Gera milhões de sequências curtas (reads) que são alinhadas ao **genoma de referência**
- Permite identificar mutações pontuais (SNPs), inserções, deleções e rearranjos cromossômicos
- O formato **FASTQ** armazena as sequências e os escores de qualidade (Q scores) de cada base
- **DNA-Seq:** sequenciamento do DNA genômico para detecção de variantes somáticas e germinativas
- **Rearranjos cromossômicos no câncer:** detectados por "hybrid reads" que mapeiam em dois cromossomos diferentes

### RNA-Seq / Transcriptômica

- Sequenciamento do transcriptoma (conjunto de todos os RNAs expressos)
- Permite quantificar a expressão gênica e identificar genes diferencialmente expressos entre condições

---

## Bioinformática e Análise de Dados

### Enriquecimento funcional

- Listas de genes diferencialmente expressos são analisadas contra bancos de dados de vias e funções (Gene Ontology - GO)
- Ferramentas: **DAVID** (david.ncifcrf.gov), **KEGG**, **STRING**
- O enriquecimento estatístico identifica quais vias biológicas estão sobre-representadas na lista de genes de interesse

### Biologia de Sistemas

- Integra dados de múltiplas camadas "ômicas" para compreender o funcionamento celular como um todo
- Analisa redes de interação entre genes, proteínas e metabólitos

---

## Proteômica

- Estudo do conjunto de proteínas expressas por uma célula, tecido ou organismo
- Técnica principal: **espectrometria de massa (LC-MS/MS)**
  - Proteínas são digeridas em peptídeos, separados por cromatografia líquida e identificados pelo espectrômetro de massa

---

## microRNAs (miRNAs) como Biomarcadores

- miRNAs são pequenos RNAs não codificantes (~22 nt) que regulam a expressão gênica pós-transcricional
- Podem ser detectados no **soro sanguíneo** como biomarcadores circulantes
- **Exemplo de aplicação clínica:** perfil de miRNAs séricos como preditores de resposta à estimulação ovariana controlada em reprodução assistida (Mulato MGF et al., 2023)
  - miR-181d-5p identificado como biomarcador de hiperesposta ovariana (AUC = 0,739; P = 0,002)
  - miRNAs alvos de vias de sinalização de estrógeno, prolactina, GnRH e maturação de oócitos

---

## Câncer: Integração dos Conceitos

O câncer resulta do acúmulo de alterações moleculares que desregulam:

- **Proliferação celular** (circuitos de proliferação: Ras, RTKs, fatores de crescimento)
- **Motilidade** (circuitos de motilidade: E-caderina, integrinas, b-catenina)
- **Viabilidade/apoptose** (Bcl-2, p53, Bax)
- **Citoestase e diferenciação** (p16, ciclina D, pRb, E2F, Smads, p21)

As vias de sinalização (MAPK, PI3K/AKT/mTOR, WNT/b-catenina, TGF-β, NF-kB) são os principais alvos moleculares para terapias oncológicas.

---

## Níveis de Controle da Expressão Gênica (Resumo)

```
DNA
 ↓ (1) Controle transcricional: metilação DNA, histonas, fatores de transcrição
RNA primário
 ↓ (2) Controle pós-transcricional: processamento, splicing
mRNA (núcleo)
 ↓ (3) Transporte e sublocalização celular
mRNA (citoplasma)
 ↓ (4) Regulação por microRNAs / degradação do mRNA
 ↓ (5) Tradução
Proteína
 ↓ (6) Modificações pós-traducionais: fosforilação, glicosilação, etc.
```

Cada nível representa um ponto de regulação que determina qual proteína é produzida, em qual quantidade e com qual atividade — determinando, em última instância, o **fenótipo** celular e do organismo.

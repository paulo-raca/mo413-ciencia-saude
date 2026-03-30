# Resumo: Visão Geral da Disciplina — Ciência de Dados para Saúde

[slides](slides.pdf) | [YouTube](https://www.youtube.com/watch?v=Yb-ygbFyeAc)

**Página da disciplina:** https://datasci4health.github.io/

---

## Natureza Interdisciplinar da Disciplina

A disciplina é explicitamente **interdisciplinar**, integrando três grandes áreas do conhecimento:

- Ciências Exatas
- Biologia
- Saúde

A composição temática central é: **Saúde + Biologia de Sistemas + Ciência de Dados + Ciência de Redes**.

Uma questão central que motiva o curso é dupla: o que um biólogo precisa saber sobre computação? E o que um cientista da computação precisa saber sobre biologia?

---

## Panorama da Disciplina

### Composição do Conhecimento

O curso parte da premissa de que a biologia moderna e a medicina geram dados de altíssima complexidade, exigindo ferramentas computacionais sofisticadas para sua interpretação. A disciplina é construída sobre quatro pilares:

1. **Saúde** — problemas clínicos reais como cânceres, doenças cardiovasculares, leucemias
2. **Biologia de Sistemas** — visão integrada dos sistemas biológicos
3. **Ciência de Dados** — métodos de análise, aprendizado de máquina, modelos de linguagem
4. **Ciência de Redes** — grafos, redes de interação, propriedades topológicas

---

## Biologia de Sistemas e o Dogma Central

### Fluxo da Informação Genética

O curso apresenta o dogma central da biologia molecular como ponto de partida:

- **DNA** — informação genética armazenada na dupla hélice
- **DNA → RNA** — transcrição via RNA polimerase; geração de pre-mRNA e mRNA maduro
- **RNA → Proteína** — tradução via ribossomo; geração de polipeptídios (Clancy & Brown, 2008)

### Expressão Gênica Diferencial

Células diferentes (embrionárias, epiteliais, neurônios) expressam os mesmos genes de formas distintas, resultando em diferentes perfis de proteínas. O conceito de **genes diferencialmente expressos** é central — visualizado por heatmaps e volcano plots, com aplicação em contextos como leucemia mieloide crônica (CML).

### Interações DNA/RNA/Proteínas

O curso aborda a complexidade das interações entre moléculas biológicas (Dai et al., 2020):

- miRNA, mRNA, lncRNA, snoRNA, tiRNA, piRNA
- Fluxo de informação genética, transdução de sinal e regulação

### Proteínas e Sinalização Celular

- Vias de sinalização celular: GPCR, PKA, MAPK, JAK/STAT, PI3K/AKT, WNT/Frizzled
- Sinalização em câncer: ciclo celular, apoptose, proliferação
- **Hallmarks of Cancer** (Hanahan, 2022): 14 características do câncer, incluindo sinalização proliferativa sustentada, evasão de supressores de crescimento, imortalidade replicativa, invasão, angiogênese, metabolismo desregulado, plasticidade fenotípica, microbioma polimórfico

### Ômicas e Metabolômica

Cadeia completa das ciências ômicas:

| Nível      | Ciência         |
| ---------- | --------------- |
| Gene       | Genômica        |
| mRNA       | Transcriptômica |
| Proteína   | Proteômica      |
| Metabólito | Metabolômica    |

---

## Complexidade e Abstração

### Complexidade

Citação motivadora de **John von Neumann**: _"If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is."_

A complexidade biológica exige ferramentas de abstração para tornar os sistemas compreensíveis e analisáveis.

### Abstração em Biologia

Hierarquia de abstração nos sistemas biológicos (do mais concreto ao mais abstrato):

1. Proteínas e genes
2. Reações bioquímicas
3. Vias metabólicas (pathways)
4. Células
5. Tecidos e culturas

### Abstração em Informação / Redes

Conceitos de abstração em redes complexas:

- **Nós** (nodes) e **arestas** (edges)
- **Hub**: nó central com muitas conexões
- **Community**: agrupamento denso de nós
- **Network motif**: padrão recorrente de conectividade
- **High centrality node/edge**: elementos mais importantes na rede

---

## Dimensões de Ciência de Dados em Saúde

O curso apresenta duas representações fundamentais dos dados biológicos:

### Redes

Dados representados como grafos: nós são entidades (proteínas, genes, doenças, pacientes) e arestas representam relações (interações, co-expressão, similaridade).

### Vetores no Espaço

Dados representados como vetores em espaço multidimensional: cada entidade é um ponto no espaço, permitindo calcular distâncias e agrupamentos.

---

## Ciência de Redes Aplicada à Biologia e Saúde

### Rede de Interação Proteína-Proteína (PPI)

- Métodos de predição: acoplamento de resíduos, machine learning, mineração de literatura, co-ocorrência, co-expressão gênica, fusão de domínios
- Exemplo clássico: rede PPI de levedura com 1.870 proteínas e 2.240 interações (Jeong et al., 2001)
- Aplicação em vírus: interações SARS-CoV-2, SARS-CoV-1 e MERS-CoV com proteínas humanas (Gordon et al., 2020)
- Interação vírus-hospedeiro: identificação de receptores de entrada do SARS-CoV-2

### Rede Regulatória de Genes (GRN)

- Regulação transcricional, traducional e pós-traducional
- Interações RNA-RNA e pós-traducionais
- Aplicação: GRN com genes específicos de câncer para câncer de bexiga, colorretal, hepático, de mama e pulmonar (Oh et al., 2014)

### Redes Complexas

Propriedades e conceitos de redes complexas (Vulliard & Menche, 2021):

- **Centralidade e importância**: genes essenciais e genes de doenças ocupam posições centrais na rede de proteínas (Barabási et al., 2011)
- **Community detection**: identificação de módulos funcionais
- **Network motifs**: tipos incluem feedback loop, feed-forward loop, bi-fan, bi-parallel, etc.
- **Link prediction**: predição de novas interações a partir da topologia da rede

### Doenças no Espaço de Redes

- Regiões agrupadas no interactoma correspondem a mesma categoria de doença
- Exemplo: doenças metabólicas (diabetes, obesidade, síndrome metabólica) formam clusters distintos de doenças renais e oculares

---

## Representações de Dados em Saúde

### Vetores e Embeddings

- **Semântica vetorial**: entidades representadas como vetores (ex: queen, king, peasant como pontos no espaço)
- **Knowledge Graph**: estruturas hierárquicas de conhecimento (ontologias)
- **Embedding**: representação densa aprendida por modelos (ex: animais que podem "voar sobre colinas")

### Métricas de Células Cancerosas

Representação de células como vetores com atributos:

- Raio, perímetro, área, compacidade, concavidade, suavidade, textura, dimensão fractal (Street et al., 1993)
- Diagnóstico de tumor benigno (B) vs. maligno (M) com base na posição no espaço vetorial

### Pacientes como Vetores

- Pacientes representados por sintomas (pressão arterial, náusea, dor no peito, frequência cardíaca, etc.)
- Clusterização de prontuários: exemplo com infarto — prontuários MIMIC agrupados em clusters por similaridade de sintomas
- Representação 2D via redução de dimensionalidade (MDS)

---

## Modelos de Linguagem em Biologia e Saúde

### Linguagem Natural e Dados Clínicos

- **BERT**: modelo bidirecional para extração de informação clínica (ex: sintomas como "chronic cough", "barrel chest" classificados como físicos)
- **Llama**: modelo autoregressivo para completar sequências clínicas (ex: "pain radiating to the chest")

### Modelos de Linguagem para Proteínas

- Analogia entre sequências de texto e sequências de aminoácidos (Madani et al., 2023)
- **ProGen**: geração de sequências proteicas funcionais condicionadas a famílias específicas (imunoglobulina, corismato mutase, etc.)
- Treinado em 280 milhões de sequências de ~19 mil famílias Pfam
- AUC de 0,85–0,94 na avaliação de funcionalidade

### Modelos de Linguagem para Química

- Predição de reações químicas via tradução de strings SMILES com encoder-decoder (Strieth-Kalthoff et al., 2020)

### Modelos de Linguagem como Ferramentas

- Uso de LLMs para construção de grafos de conhecimento: exemplo com Neo4j e Cypher para conectar doenças a sintomas (ex: Diabetes Mellitus → Obesity)

---

## Gene Ontology e Ontologias Biológicas

### Gene Ontology (GO)

Sistema de anotação de genes em três dimensões:

1. **Processos biológicos**: processos celulares que o gene participa
2. **Funções moleculares**: atividade molecular da proteína
3. **Componentes celulares**: localização da proteína na célula

Exemplo: GO:0043504 — "mitochondrial DNA repair", localizado no grafo hierárquico do GO.

### Enriquecimento (Enrichment Analysis)

- Identificação de conjuntos de genes/proteínas super-representados em condições experimentais
- Aplicação em leucemia/linfoma de células T do adulto (Wang & Iha, 2023): identificação de alvos farmacológicos como EGFR, AKT, HSP90, HDAC

---

## Modelos, Análise e Ferramentas

### Modelos de Dados

Duas representações complementares:

- **Grafo**: nós com propriedades e arestas com pesos (ex: rede PPI com scores experimental e de banco de dados)
- **Tabela**: mesma informação em formato tabular (pares de proteínas com scores)

### Tipos de Análise

O curso aborda cinco formas de análise computacional:

1. **Perguntas de pesquisa** — ponto de partida científico
2. **Exploração e descoberta de conhecimento**
3. **Predição** — classificação de novos casos
4. **Inferência** — relações causais e estatísticas
5. **Classificação** — agrupamento e categorização

### Ferramentas

- **Modelos de linguagem** para construção de bases de dados e grafos
- **Visualização** de redes e dados multidimensionais
- **Aprendizado de máquina** para classificação e predição

---

## Estudos de Caso e Problemas Reais

O curso parte de **problemas biológicos e clínicos reais**, com participação de professores de Biologia e Saúde:

### Câncer de Mama

- Subtipos moleculares: ER+/PR+/HER2−, ER+/PR+/HER2+, ER−/PR−/HER2+, triplo-negativo
- Análise histológica (H&E) e imunohistoquímica (ER, PR, HER2)

### Melanoma

- Resistência a inibidores de RAF (PLX4072) via via RAS/B-RAF/MEK/ERK
- Perfil genômico de tumor para dissecar mecanismos de resistência (Wagle et al., 2011)

### Leucemias

- Tipos: AML, ALL, CML, CLL — cada um originado em estágio diferente da hematopoiese
- **Imatinib**: inibidor de BCR-ABL para leucemia mieloide crônica — exemplo de terapia-alvo bem-sucedida (Savage & Antman, 2002)

### Câncer de Tireoide

- Modelo _in vivo_: camundongo FVB Tg-BRAF com mutação BRAF V600E
- miR-485-5p como regulador de migração e invasão em células TPC-1 e BCPAP (Leonardo Marson)

---

## Dinâmica do Curso

### Grupos Mistos

Os alunos trabalham em **grupos mistos** compostos por estudantes de Ciências Exatas e de Saúde, com papéis complementares:

- **Alunos de exatas**: foco na parte computacional
- **Alunos de Biologia e Saúde**: foco na parte biológica e clínica

### Abordagem Pedagógica

- Parte de **problemas reais** de biologia e saúde
- Participação ativa de professores das áreas de Biologia e Saúde
- Projetos práticos com dados reais (ex: MIMIC, dados de expressão gênica)

### Professor

- **André Santanchè** — Instituto de Computação, UNICAMP (https://www.ic.unicamp.br/~santanche/)

---

## Referências Principais

- Barabási et al. (2011) — centralidade e importância em redes de proteínas
- Clancy & Brown (2008) — tradução: DNA → mRNA → Proteína
- Dai et al. (2020) — interações de RNA e funcionalidades
- Gordon et al. (2020) — redes de interação hospedeiro-coronavírus
- Hanahan (2022) — Hallmarks of Cancer: novas dimensões
- Jeong et al. (2001) — letalidade e centralidade em redes de proteínas
- Keskin et al. (2016) — interações proteína-proteína
- Madani et al. (2023) — modelos de linguagem geram sequências proteicas funcionais
- Oh et al. (2014) — classificação baseada em redes para associações droga-doença
- Savage & Antman (2002) — Imatinib mesylate como terapia oral alvo
- Thomas et al. (2014) — chaveamento fenotípico em redes regulatórias de genes
- Vulliard & Menche (2021) — redes complexas em biologia
- Wagle et al. (2011) — resistência à inibição de RAF em melanoma

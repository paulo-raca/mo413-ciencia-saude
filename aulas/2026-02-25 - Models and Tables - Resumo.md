# Modelos e Tabelas em Ciência de Dados para Saúde

Aula de André Santanchè (UNICAMP) — 25 de fevereiro de 2026

---

## Modelos Conceituais

Um **modelo** é uma representação simplificada da realidade, usada para comunicar, projetar e analisar sistemas de dados. A escolha do modelo impacta diretamente como os dados são armazenados, trocados e analisados.

### Níveis de Modelo

| Nível                 | Descrição                                                                                                                                                                            |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Modelo Conceitual** | Representa a semântica dos dados de forma independente de tecnologia. Exemplo: usar o DAVID Bioinformatics para análise de enriquecimento de termos GO em miRNAs do locus DLK1-DIO3. |
| **Modelo Lógico**     | Representa como os dados são organizados independentemente da implementação física. Desafio: representar dados independentemente da implementação.                                   |
| **Modelo Físico**     | Representa a camada de armazenamento real dos dados (Data Storage), conectada ao gerenciamento de dados e às aplicações.                                                             |

---

## Modelos Lógicos Clássicos

Existem cinco tipos principais de modelos lógicos para organização de dados:

| Modelo                        | Características                                                                                                                                    |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Flat File (Arquivo Plano)** | Dados em registros simples, sem estrutura relacional. Ex.: registros de rotas com milhas e atividades.                                             |
| **Hierárquico**               | Dados organizados em árvore (pai-filho). Ex.: prontuário > paciente > atendimentos > atendimento > motivo/data.                                    |
| **Relacional**                | Dados em tabelas interligadas por chaves. Ex.: tabela de atividades com código e nome.                                                             |
| **Orientado a Objetos**       | Dados encapsulados em objetos com atributos e instâncias. Ex.: Relatório de Manutenção com código de atividade, data, rota, horas.                 |
| **Rede (Network)**            | Dados com múltiplas relações entre nós, sem hierarquia estrita. Ex.: tipos de manutenção preventiva ramificando em pavimentos rígidos e flexíveis. |

---

## Tabelas

### Definição

Uma **tabela** é a estrutura central de representação de dados. É composta por:

- **Esquema** (schema): a linha de cabeçalho que define as colunas (atributos). Exemplo: `name | height | weight`.
- **Instâncias**: as linhas de dados. Exemplo:

| name      | height | weight |
| --------- | ------ | ------ |
| Doriana   | 1.87   | 60     |
| Quincas   | 1.81   | 110    |
| Asdrúbal  | 1.74   | 74     |
| Lucinda   | 1.49   | 46     |
| Dulcinéia | 1.65   | 64     |

### Por que Tabelas?

Tabelas são o formato **pivô** na ciência de dados: todas as ferramentas analíticas principais (R, Python/pandas, SPSS, Orange, Tableau, QIIME2) trabalham nativamente com tabelas. Isso reduz a complexidade de integração entre aplicações.

### Vantagens das Tabelas

- **Previsibilidade**: a estrutura é sempre conhecida — esquema fixo + instâncias.
- **Seleção e recuperação**: fácil selecionar linhas específicas.
- **Corte por atributos**: fácil operar estatísticas sobre colunas inteiras.

---

## Troca de Dados e Complexidade

### O Problema da Alta Complexidade

Quando múltiplas aplicações com formatos diferentes se comunicam diretamente entre si, a complexidade cresce de forma combinatória (N × M conexões).

### A Solução: Pivot Agreement

A tabela funciona como um **pivô de acordo** entre aplicações: cada aplicação só precisa conhecer um formato (a tabela), reduzindo a complexidade para N + M conversões.

### Pivot em Pipeline

Tabelas também podem ser encadeadas em **pipelines**, onde a saída de uma aplicação (em formato de tabela) é a entrada da próxima.

### Convergência de Formatos

Dados heterogêneos (árvores, grafos, séries temporais, linked data) podem todos ser convertidos para o formato tabular, que serve como formato universal de interoperabilidade.

---

## Três Tipos de Uso de Tabelas

### 1. Tabelas como Vetores

Cada linha representa um **vetor de atributos fixos** no espaço multidimensional. Cada instância é um ponto nesse espaço.

- **Requisito**: número fixo de atributos por instância.
- **Aplicação**: machine learning, classificação, clustering.
- **Exemplo biomedico**: dataset Breast Cancer Wisconsin (UCI) — 569 instâncias, 30 atributos numéricos extraídos de imagens de biópsia por agulha fina (FNA). Atributos incluem: raio, perímetro, área, compacidade, concavidade, pontos côncavos, textura, suavidade, simetria, dimensão fractal. Diagnóstico: B (benigno) ou M (maligno).

Métricas das células cancerígenas:

- Suavidade (smoothness)
- Concavidade (concavity)
- Simetria (symmetry)
- Dimensão fractal (fractal dimension)
- Raio, perímetro, área, compacidade, textura

Exemplo de tabela de células cancerígenas:

| name       | radius | fractal dimension | diagnosis |
| ---------- | ------ | ----------------- | --------- |
| 862722     | 6.981  | 0.07818           | B         |
| 9111157302 | 21.100 | 0.05661           | M         |
| 889719     | 17.190 | 0.05580           | M         |
| 8910251    | 10.600 | 0.06491           | B         |
| 8510653    | 13.080 | 0.06811           | B         |

Quando a tabela tem número variável de atributos por instância (ex: itens consumidos num restaurante — Natilli et al., 2019), usa-se formato **largo/estreito** (wide/narrow ou unstacked/stacked):

- **Formato largo (wide/unstacked)**: cada atributo é uma coluna — uma linha por instância.
- **Formato estreito (narrow/stacked)**: colunas `name | attribute | value` — múltiplas linhas por instância.

### 2. Tabelas como Relações

Representam **relacionamentos entre entidades** do modelo relacional. Permitem ligar múltiplas tabelas por chaves.

**Chave Estrangeira (Foreign Key)**: referência ao identificador de outra tabela.

Exemplo — Pessoa ocupa Armário:

- Variante 1 (1:1): coluna `Armário` na tabela `PESSOA`, referenciando código do armário.
- Variante 2 (N:M): tabela intermediária `OCUPA` com colunas `CodPessoa`, `CodArmário`, `Data`, `Hora`.

Exemplo completo — Modelo de Táxi:

| Tabela       | Chave                      | Atributos             |
| ------------ | -------------------------- | --------------------- |
| Cliente (C)  | Cliid                      | Nome, CPF             |
| Táxi (TX)    | Placa                      | Marca, Modelo, AnoFab |
| Corrida (R1) | (Cliid, Placa, DataPedido) | —                     |

**Tabela de Doenças e Sintomas** (exemplo de relação com peso de associação):

| disease                | symptom    | association |
| ---------------------- | ---------- | ----------- |
| Influenza              | Fever      | 136         |
| Influenza              | Headache   | 17          |
| Myocardial Infarction  | Chest Pain | 1005        |
| Diabetes Complications | Obesity    | 126         |

### 3. Tabelas como Redes (Grafos)

Permitem representar grafos usando duas tabelas:

- **Tabela de Nós**: cada linha é um nó com seus atributos (id/prop1, prop2, prop3...).
- **Tabela de Arestas**: cada linha é uma aresta com colunas `origin | target | prop1 | prop2...`.

Exemplo — Rede de proteínas:

Tabela de nós:
| #node | identifier | degree |
|---|---|---|
| AKT1 | 9606.ENSP00000451828 | 24 |
| BRAF | 9606.ENSP00000419060 | 12 |

Tabela de arestas:
| #node1 | node2 | experimental | database |
|---|---|---|---|
| AKT1 | BRAF | 0.631 | 0 |
| ARAF | KRAS | 0.745 | 0.9 |

---

## Formatos de Arquivo para Tabelas

### CSV — Comma Separated Values

O formato mais simples e universal para tabelas:

- Fácil de implementar
- Reconhecido por todas as ferramentas
- Evita incompatibilidades futuras

Exemplo:

```
nome,altura,peso
Doriana,1.87,60
Quincas,1.81,110
```

### TSV — Tab Separated Values

Similar ao CSV, mas usa tabulação como separador. Útil quando os dados contêm vírgulas.

---

## Estudo de Caso 1: Rede Humana Sintoma-Doença

**Referências**:

- Goh et al. (2007). The human disease network. PNAS 104(21), 8685–8690.
- Zhou et al. (2014). Human symptoms–disease network. Nature Communications, 5(1), 4212.

**Estrutura dos dados**:

- 4.442 doenças no PubMed
- 322 sintomas
- 147.978 registros de co-ocorrências sintoma-doença (TF-IDF)
- 133.106 conexões entre 1.596 doenças distintas

**Resultado**: regiões clusterizadas da rede agrupam doenças relacionadas (ex: doenças metabólicas, doenças oculares, complicações da gravidez, doenças renais).

**Dados disponíveis no DataSci4Health**: formato TSV em https://github.com/datasci4health/datasci4health.github.io

---

## Estudo de Caso 2: PrimeKG — Grafo de Conhecimento para Medicina de Precisão

**Referência**: Chandak, P., Huang, K., & Zitnik, M. (2023). Building a knowledge graph to enable precision medicine. Scientific Data, 10(1), 1–16.

**Estrutura do PrimeKG**:

- 17.080 doenças
- 4.050.249 relacionamentos
- 10 escalas biológicas: doenças, medicamentos, genes, fenótipos, regiões anatômicas, vias (pathways), exposições, processos biológicos (BP, CC, MF)

**Tipos de relacionamentos**:

- Indicações droga-doença
- Contraindicações droga-doença
- Uso off-label
- Associações doença-fenótipo (+/-)
- Associações doença-proteína
- Associações doença-exposição

**Formato dos dados**: CSV/TSV hospedado no Harvard Dataverse. Tabela de nós (`nodes.tab`) com 5 variáveis e 129.375 observações.

**Acesso**: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM

---

## Ferramenta: Dagoberto

Ferramenta web para visualização de grafos a partir de tabelas CSV:

- URL: https://datasci4health.github.io/networks/dagoberto/
- Entrada: duas tabelas CSV — nós e arestas
- Saída: visualização do grafo e gráfico dos nós

---

## Resumo: Hierarquia de Modelos

```
Modelo Conceitual  →  o que os dados significam
        |
Modelo Lógico      →  como os dados são organizados (tabela, grafo, hierarquia...)
        |
Modelo Físico      →  onde e como os dados são armazenados
```

A **tabela** é o ponto de convergência prático: independente do modelo lógico original (hierárquico, em grafo, relacional), os dados podem ser convertidos para o formato tabular para análise com ferramentas padrão como R, Python/pandas, SPSS, Orange e Tableau.

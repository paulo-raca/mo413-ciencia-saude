# Redes e Grafos (Networks and Graphs)

Resumo da aula de 09/03/2026 — André Santanchè (UNICAMP)

---

## Introdução: O que é uma Rede?

Uma rede é um conjunto de **entidades** (nós/vértices) conectadas por **relações** (arestas). Redes são usadas para modelar fenômenos do mundo real: redes sociais, redes de proteínas, vias metabólicas, sistemas de transporte, cadeias alimentares, etc.

A motivação central é que **propriedades emergentes** surgem da estrutura da rede — o todo é mais do que a soma das partes (ex: bandos de pássaros, consciência no cérebro).

---

## Modelo Matemático de Grafos

Um grafo é definido como um par de conjuntos:

```
G = (V, E)
```

- **V** — conjunto de vértices (nós)
- **E** — conjunto de arestas (edges)

### Grafo Não-Dirigido (Undirected)

As arestas não têm direção. Representadas como conjuntos: `{a, b}`.

Exemplo:

- V = {a, b, c, d}
- E = { {a,b}, {a,c}, {a,d}, {b,d}, {c,d} }

### Grafo Dirigido (Directed / Dígrafo)

As arestas têm direção (origem → destino). Representadas como pares ordenados: `(a, b)`.

Exemplo:

- V = {a, b, c, d}
- E = { (a,b), (a,c), (d,a), (d,b), (d,c) }

---

## Representações Computacionais

### Matriz de Adjacência

- Matriz quadrada N×N onde `M[i][j] = 1` se existe aresta de i para j, 0 caso contrário.
- Em grafos não-dirigidos, a matriz é simétrica.
- Em grafos dirigidos, a matriz pode ser assimétrica.

### Lista de Arestas (Edge List)

- Tabela com colunas `source` e `target` (e opcionalmente atributos/pesos).
- Formato tabular simples, adequado para armazenamento em CSV/TSV.
- Cada linha representa uma aresta.

### Tabela de Nós (Node Table)

- Cada linha representa um nó com seus atributos (id, propriedades, etc.).

---

## Modelo Lógico vs. Físico

O grafo é um modelo **lógico** que pode ser armazenado fisicamente de diferentes formas:

- **Armazenado como Grafo** — estrutura de ponteiros em memória/banco de dados de grafos.
- **Armazenado como Tabela** — duas tabelas relacionais: uma de nós e uma de arestas (com colunas `origem` e `destino`).

A **desnormalização** combina atributos de nós e arestas em uma única tabela plana para facilitar análise.

---

## Tipos de Redes

### Grafo de Fenômenos (Phenomena Graph)

Representa relações causais ou de interação observadas empiricamente.

Exemplo: via de sinalização em melanoma (PLX4072 → B-RAF → MEK → ERK), representando como um fármaco inibe proteínas na cascata MAPK.

### Grafo de Conhecimento (Knowledge Graph)

Representa conhecimento formal e estruturado sobre conceitos e suas relações.

- Nós = conceitos (ex: "Leucemia", "Leucemia Mieloide Crônica")
- Arestas = relações semânticas (ex: `is a`, `part of`, `regulates`)
- Exemplos: DBpedia, WordNet, Gene Ontology, Disease Ontology

---

## Semântica Explícita e Ontologias

### Problema de Ambiguidade

Uma mesma palavra pode ter múltiplos significados (ex: "cell" pode ser célula biológica ou cela de convento). Humanos inferem o contexto; máquinas precisam de representação formal.

### Web Semântica

Proposta por Berners-Lee et al. (2001): dados estruturados na web com semântica explícita, permitindo que agentes de software raciocinem e integrem informações automaticamente.

### Ontologia

> "Uma ontologia é uma especificação formal e explícita de uma conceitualização compartilhada." (Studer et al., 1998)

**Espectro de ontologias** (do menos ao mais formal):

- Catálogo / ID
- Termos / glossário
- Tesauro (relações "narrower term")
- Formal is-a / instância
- Frames (restrições de valor)
- Restrições lógicas gerais

### WordNet

Rede lexical que organiza palavras em conjuntos de sinônimos (synsets), conectados por relações semânticas: hiperônimos, hipônimos, merônimos, holônimos, sinônimos.

### Gene Ontology (GO)

Ontologia biomédica com três dimensões:

1. **Processos Biológicos** (ex: reparo de DNA mitocondrial — GO:0043504)
2. **Funções Moleculares**
3. **Componentes Celulares**

Exemplo de hierarquia no QuickGO: nucleus → intracellular membrane-bounded organelle → ... → cellular component.

---

## Ferramentas

### Dagoberto

Ferramenta web para visualização e exploração interativa de redes a partir de arquivos CSV/TSV de nós e arestas.

- https://datasci4health.github.io/networks/dagoberto/

### Cytoscape

Software desktop para análise e visualização de redes biológicas e de outros domínios. Suporta importação de tabelas (TSV/CSV), estilização visual e plugins de análise.

- https://cytoscape.org/

---

## Estudos de Caso

### Melanoma — Rede de Interação Proteína-Proteína (PPI)

- Fonte de dados: banco **STRING** (https://string-db.org/) — banco de interações proteína-proteína conhecidas e preditas.
- Tipos de evidência no STRING: interações de bancos curados, determinadas experimentalmente, vizinhança gênica, fusões, co-ocorrência, co-expressão, mineração de texto, homologia de proteínas.
- Fluxo de trabalho: buscar "Melanoma" no STRING → selecionar gene set KEGG hsa05218 → exportar como TSV ("short tabular output") → importar no Cytoscape.
- Resultado: rede de ~72 proteínas relacionadas ao melanoma.

### Leucemia Mieloide Crônica (CML)

- Causada pela translocação cromossômica t(9;22) → Cromossomo Filadélfia → gene de fusão BCR-ABL1.
- A rede de interações pode ser explorada no STRING e visualizada no Cytoscape.
- Análise de enriquecimento permite identificar drogas-alvo (ex: inibidores de HDAC, EGFR, AKT).

### Rede Humana Sintoma-Doença (Human Symptom-Disease Network)

Referência: Zhou et al. (2014), _Nature Communications_, 5, 4212.

- Construída a partir da literatura biomédica (PubMed): 4.442 doenças, 322 sintomas, 147.978 registros de co-ocorrência sintoma-doença.
- Doenças da mesma categoria tendem a se agrupar em regiões do grafo.
- Dataset disponível como material suplementar do artigo (Supplementary Data 3).

### PrimeKG — Grafo de Conhecimento para Medicina de Precisão

Referência: Chandak, Huang & Zitnik (2023), _Scientific Data_, 10, 67.

- Grafo multimodal integrando 20 bases de dados de alta qualidade.
- 17.080 doenças, 4.050.249 relações em 10 escalas biológicas.
- Tipos de nós: doenças, drogas, genes, fenótipos, vias, regiões anatômicas, exposições.
- Tipos de relações: indicação droga-doença, contraindicação, uso off-label, associações doença-proteína, doença-fenótipo, etc.
- Disponível no Harvard Dataverse.

---

## Aplicações em Saúde

| Tipo de Rede            | Exemplo                        | Uso                                 |
| ----------------------- | ------------------------------ | ----------------------------------- |
| PPI (proteína-proteína) | STRING — melanoma, CML         | Identificar alvos terapêuticos      |
| Via de sinalização      | KEGG — MAPK pathway            | Entender mecanismos de doença       |
| Sintoma-doença          | Zhou et al. 2014               | Descoberta de associações clínicas  |
| Grafo de conhecimento   | PrimeKG, DBpedia               | Inferência, medicina de precisão    |
| Cadeia alimentar        | FishBase (Cavoto et al., 2015) | Análise ecológica                   |
| Ontologia de genes      | Gene Ontology                  | Anotação e enriquecimento funcional |

---

## Distinção: Descoberta vs. Inferência

- **Grafo de Fenômenos** → suporta **Descoberta**: revela padrões e relações nos dados observados (ex: quais proteínas interagem na via do melanoma).
- **Grafo de Conhecimento** → suporta **Inferência**: permite raciocinar sobre relações entre conceitos e deduzir novo conhecimento (ex: CML `is a` leucemia mieloide `is a` leucemia hematológica).

A abordagem do curso combina os dois: usar grafos de fenômenos para descoberta e grafos de conhecimento para contextualizar e inferir.

---

## Referências Principais

- Berners-Lee, T., Hendler, J., & Lassila, O. (2001). The Semantic Web. _Scientific American_, 284(5), 28–37.
- Cavoto, P., Cardoso, V., Lebbe, R. V., & Santanche, A. (2015). FishGraph: A network-driven data analysis. _IEEE EScience 2015_.
- Zhou, X., Menche, J., Barabási, A.-L., & Sharma, A. (2014). Human symptoms–disease network. _Nature Communications_, 5(1), 4212.
- Chandak, P., Huang, K., & Zitnik, M. (2023). Building a knowledge graph to enable precision medicine. _Scientific Data_, 10(1), 1–16.
- Ji, S. et al. (2022). _(Knowledge Graph survey — exemplo Albert Einstein)_.
- Studer, R. et al. (1998). _(Definição de ontologia)_.
- Welty, C. et al. (1999). _(Espectro de ontologias)_.

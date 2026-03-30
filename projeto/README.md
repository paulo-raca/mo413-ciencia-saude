# Câncer de Pele e seus Tipos: uma Análise do Perfil de Expressão Gênica em Redes

**Disciplina:** MO413A - Ciência e Visualização de Dados em Saúde (UNICAMP)

**Equipe ALFAK**

| Subgrupo | Integrantes |
| -------- | ----------- |
| A        | Augusto José Peterlevitz, Felipe Kennedy Carvalho Torquato, Luis Henrique Angélico |
| B        | Paulo Costa, Naruan Francisco Ferraz e Ferraz, Alan Freitas Ribeiro |

---

## Resumo

Comparar redes de interação gênica derivadas de amostras de câncer de pele melanoma, não-melanoma e tecido saudável. Serão analisadas as diferenças na topologia da rede, nos genes centrais e nos módulos biológicos, com objetivo de observar padrões específicos da doença e mecanismos compartilhados, fornecendo informações sobre a biologia tumoral e potenciais biomarcadores.

---

## Contexto: Câncer de Pele

**Classificação:** por localização e tipo celular de origem.

**Tipos:**

- Carcinoma Basocelular
- Carcinoma Espinocelular
- Melanoma

**Epidemiologia:** 1,57 milhão de casos em 2022, com projeção de 2,96 milhões até 2045 (Global Cancer Observatory / IARC).

---

## Perguntas de Pesquisa

1. Como as redes gênicas diferem entre melanoma, não-melanoma e tecido saudável?
2. Existem genes "exclusivos" em cada tipo de câncer?
3. Existem vias moleculares compartilhadas entre melanoma e não-melanoma?
4. Quais interações são adquiridas ou perdidas em cada tipo de câncer?
5. Podemos identificar módulos (clusters) específicos para cada tipo de câncer?

---

## Metodologia

1. **Obtenção de dados** via Gene Expression Omnibus (GEO) — grupos: Saudável, Melanoma, Não-melanoma
2. **Expressão diferencial** — comparações: Saudável vs Melanoma, Saudável vs Não-melanoma, Melanoma vs Não-melanoma
3. **Consulta ao STRING** — interações proteína-proteína com scores de confiança
4. **Análise no Cytoscape:**
   - Eigenvector centrality (CytoNCA)
   - Degree e clustering coefficient (NetworkAnalyzer)
   - Clusterização (clusterMaker2 / MCODE)
5. **Comparação entre redes:**
   - Genes ganhos/perdidos (saudável vs não-saudável)
   - Genes centrais e arestas exclusivas
   - Métricas: degree, betweenness centrality, closeness centrality
   - Semelhanças entre melanoma e tecido saudável

---

## Datasets (GEO)

| Grupo        | Datasets                    |
| ------------ | --------------------------- |
| Saudável     | GSE4570, GSE2503, GSE53462  |
| Melanoma     | GSE4570, GSE8401, GSE7553   |
| Não-melanoma | GSE2503, GSE45216, GSE53462 |

---

## Análises Adicionais — Deep Learning

- **Graph Attention Networks (GAT)** com dataset TCGA-SKCM
- Construir grafo proteína-proteína (PPI)
- Treinar modelo GAT e mapear coeficientes de atenção como propriedades visuais no grafo
- Interface visual mostrando mudanças nos pesos de atenção entre tecido normal, carcinoma e melanoma

---

## Ferramentas

- **Dados:** GEO, Excel
- **Redes:** STRING, Cytoscape (CytoNCA, NetworkAnalyzer, MCODE, clusterMaker2)
- **Programação:** Python — PyTorch, Pandas, Scikit-learn

---

## Modelo Lógico da Base de Grafos

**Expressão diferencial:**

- `Gene` —[Expressão diferencial]→ `Comparação` —[Resulta em]→ `Tecido`
- Atributos da aresta: `log2fc`, `p_value`, `adj_p_value`

**Centralidade:**

- `Gene` —[Centralidade]→ `Tecido`
- Atributos: `Betweenness`, `Closeness`, `EigenVector` (float)

**Clustering:**

- `Gene` —[Pertence a]→ `Cluster` → `Carcinoma`
- Atributos do cluster: `Nome`, `Algoritmo`

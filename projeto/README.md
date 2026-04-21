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

1. **Obtenção de dados** via Gene Expression Omnibus (GEO), com download automatizado pelo accession (GEOparse)
2. **Expressão diferencial** — comparações com granularidade por **estágio/tipo** (e não por grupo agregado):
   - Pele normal × Melanoma in situ
   - Pele normal × Melanoma primário
   - Pele normal × Melanoma metastático
   - Pele normal × Carcinoma basocelular (BCC)
   - Pele normal × Carcinoma espinocelular (SCC)
   - *(Opcional)* Comparações de progressão: in situ → primário → metastático; AK → SCC
3. **Anotação externa — Open Targets**: anexa ao nó o `globalScore` de associação com a doença (EFO_0000756 = melanoma; EFO/MONDO correspondentes para BCC/SCC) como atributo de *drogabilidade*/relevância clínica
4. **Consulta ao STRING** — interações proteína-proteína com scores de confiança (`combined_score`)
5. **Análise no Cytoscape:**
   - Eigenvector centrality (CytoNCA)
   - Degree e clustering coefficient (NetworkAnalyzer)
   - Clusterização (clusterMaker2 / MCODE / Leiden)
6. **Comparação entre redes:**
   - Genes ganhos/perdidos entre estágios (saudável → in situ → primário → metastático)
   - Hubs compartilhados vs. específicos por tipo/estágio
   - Métricas: degree, betweenness, closeness, eigenvector
   - Semelhanças estágio-a-estágio e entre tipos (melanoma vs. não-melanoma)

---

## Datasets (GEO)

### Por comparação

| Grupo        | Datasets                    |
| ------------ | --------------------------- |
| Saudável     | GSE4570, GSE2503, GSE53462  |
| Melanoma     | GSE4570, GSE8401, GSE7553   |
| Não-melanoma | GSE2503, GSE45216, GSE53462 |

### Por dataset — subgrupos de amostra

| Dataset       | Subgrupos / classes de amostra | Observações |
| ------------- | ------------------------------ | ----------- |
| **GSE4570**   | Melanócitos saudáveis · Melanoma primário · Melanoma metastático | Cobre o eixo sadio → primário → metastático no mesmo estudo |
| **GSE2503**   | Pele saudável (NO) · Carcinoma espinocelular (SCC) · Queratose actínica (AK) | **AK descartada** — lesão pré-cancerígena fora do escopo das comparações principais |
| **GSE7553**   | Pele normal · Carcinoma basocelular · Carcinoma espinocelular · Melanoma in situ · Melanoma primário · Melanoma metastático | Dataset mais rico — cobre todos os tipos e estágios |
| **GSE8401**   | Melanoma primário · Melanoma metastático | Só melanoma |
| **GSE45216**  | Carcinoma espinocelular · Queratose actínica | AK aqui **é aproveitada** como precursora de ~65% dos casos de espinocelular — permite estudar características adquiridas na progressão AK → SCC. Também traz estágio de diferenciação e imunossupressão (esta última fora do escopo) |
| **GSE53462**  | *(a confirmar na coleta)* | — |

---

## Análises Adicionais — Deep Learning

- **Graph Attention Networks (GAT)** com dataset TCGA-SKCM
- Construir grafo proteína-proteína (PPI)
- Treinar modelo GAT e mapear coeficientes de atenção como propriedades visuais no grafo
- Interface visual mostrando mudanças nos pesos de atenção entre tecido normal, carcinoma e melanoma

---

## Ferramentas

- **Dados:** GEO (via [GEOparse](https://geoparse.readthedocs.io/)), [Open Targets Platform](https://platform.opentargets.org/) (anotação `globalScore` por gene-doença)
- **Redes:** STRING, Cytoscape (CytoNCA, NetworkAnalyzer, MCODE, clusterMaker2)
- **Programação:** Python — Pandas, NumPy, Marimo (notebook), PyTorch / PyTorch Geometric (GAT), Scikit-learn

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

---

## Entregas

Apresentações sucessivas do projeto ao longo do semestre — na pasta [`entregas/`](entregas/).

| Entrega | Descrição | Links |
| --- | --- | --- |
| **P1** | Proposta inicial — contexto, perguntas, metodologia, datasets, ferramentas, modelo lógico de grafos | [resumo](entregas/P1%20-%20Projeto%20inicial/README.md) · [slides](entregas/P1%20-%20Projeto%20inicial/slides.pdf) |
| **P2** | Segunda entrega — mesmo escopo + primeira rede PPI construída (GSE4216, Eigenvector Centrality) | [resumo](entregas/P2%20-%20Segunda%20entrega/README.md) · [slides](entregas/P2%20-%20Segunda%20entrega/slides.pdf) |

---

## Laboratórios

Exercícios de laboratório relacionados ao projeto — na pasta [`laboratorios/`](laboratorios/).

| Lab | Tema | Link |
| --- | --- | --- |
| **L1** | How Wolves Change Rivers — modelagem de ecossistema como grafo (trophic cascade de Yellowstone) | [resumo](laboratorios/L1%20-%20How%20Wolves%20Chang%20Rivers/README.md) |
| **L2** | Revisão de artigos científicos sobre redes complexas em expressão gênica | [resumo](laboratorios/L2%20-%20artigos/README.md) |

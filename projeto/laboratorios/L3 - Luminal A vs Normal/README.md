# L3 — Analisando a Expressão de Luminal A vs Normal

**Tarefa por subgrupo** — apresentada na aula de **27 de abril de 2026**.

Entrega: uma submissão por subgrupo, contendo o documento de análise (a partir do [template](#template-de-submissão)) e o projeto do Cytoscape.

---

## Enunciado

Dado o projeto no submodule [`datasci4health.github.io/`](../../../datasci4health.github.io/networks/breast-cancer/geo-subtypes/04-enrichment/matrix/) que contém um pipeline para análise enriquecida de expressão gênica diferencial **Luminal A vs Normal**[^LUMA] em câncer de mama.

O projeto traz os seguintes arquivos de interesse:

- [**`breast-cancer-luminal-a-matrix-all-nodes.ows`**](../../../datasci4health.github.io/networks/breast-cancer/geo-subtypes/04-enrichment/matrix/breast-cancer-luminal-a-matrix-all-nodes.ows) — workflow Orange[^OWS] que produz a rede com todos os nós.
  - Exige instalar `orange-biosci` (última versão) e `orange-biosci-r` (mas não é preciso executá-lo).

![Workflow Orange — Luminal A vs Normal](workflow.png)

- [**`breast-cancer-luminal-a-matrix-all-genes.cys`**](../../../datasci4health.github.io/networks/breast-cancer/geo-subtypes/04-enrichment/matrix/breast-cancer-luminal-a-matrix-all-genes.cys) — arquivo Cytoscape contendo a rede Luminal A vs Normal — **base para o trabalho**.
- [**`breast-cancer-luminal-a-matrix-all-genes(leiden-8-9).cys`**](../../../datasci4health.github.io/networks/breast-cancer/geo-subtypes/04-enrichment/matrix/breast-cancer-luminal-a-matrix-all-genes%28leiden-8-9%29.cys) — arquivo com **exemplo de análise** Luminal A vs Normal já realizada.

### O que entregar

Elaborar uma análise sobre as redes **Luminal A** e **Luminal B**[^LUMB], confrontando de forma **visual e criativa** as seguintes camadas de informação:

- **Comunidades** descobertas por diversos algoritmos (atributos com prefixo `community`) — recomenda-se `Community Leiden - Modularity`.
- **Pathways**[^PATHWAY] do **Reactome**[^REACTOME] anotados nos nós:
  - [Extracellular matrix organization (R-HSA-1474244)](https://reactome.org/PathwayBrowser/#/R-HSA-1474244)[^ECM]
  - [Degradation of the extracellular matrix (R-HSA-1474228)](https://reactome.org/PathwayBrowser/#/R-HSA-1474228)
  - [Collagen formation (R-HSA-1474290)](https://reactome.org/PathwayBrowser/#/R-HSA-1474290)
  - Cada pathway aparece como uma coluna binária: `0` — não pertence ao pathway; `1` — pertence ao pathway.
- **Expressão gênica diferencial** (logFC[^LOGFC]).
- **Medidas de centralidade**[^CENT].

---

## Template de submissão

Para cada característica a ser analisada, incluir pelo menos:

### Subgrupo

- nome — RA
- nome — RA
- nome — RA

### Análise X

- **Subredes criadas:**
  - falar brevemente da subrede
- **Parâmetros de filtragem usados:**
  - *Exemplo:* `Community Leiden - Modularity is between 8 and 9`
- **Estilos adotados:**
  - *Exemplo:* `Node - Fill Color - LogFC - Continuous`

\<imagens de recortes do grafo — podem ter mais ou menos zoom, enfatizando alguma parte do grafo\>

Escrever um texto comentando o que pode ser observado no grafo escolhido para a apresentação.

---

## Submissão

- Documento seguindo o template (PDF ou Markdown no GitHub).
- Projeto Cytoscape (`.cys`).
- Apenas **um membro** de cada subgrupo submete.

---

## Notas

[^LUMA]: **Luminal A** — subtipo molecular de câncer de mama. "Luminal" porque as células tumorais lembram as células que revestem a parte interna (lúmen) dos dutos mamários. O subtipo **A** é o de melhor prognóstico: tem receptor de estrógeno positivo (ER+), receptor de progesterona positivo (PR+), HER2 negativo e baixa proliferação (Ki-67 baixo). Tipicamente responde bem à terapia hormonal.
[^LUMB]: **Luminal B** — também ER+, mas com proliferação mais alta (Ki-67 alto) e/ou HER2 positivo. Prognóstico intermediário, pior que Luminal A. Comparar as duas redes ajuda a identificar mecanismos que diferenciam a agressividade entre subtipos próximos.
[^OWS]: **`.ows`** — arquivo de *workflow* do **Orange Data Mining**, um software de análise visual onde se conecta blocos (caixas) que representam etapas do pipeline. O arquivo é XML descrevendo as caixas, suas configurações e conexões — abrir no Orange reproduz a análise.
[^PATHWAY]: **Pathway** (via biológica) — conjunto de reações bioquímicas ou de proteínas que trabalham juntas para realizar uma função celular específica. Pense em uma "receita coletiva": cada proteína é um passo da receita, e o pathway é o resultado final (ex.: "construir matriz extracelular").
[^REACTOME]: **Reactome** — base de dados curada que cataloga pathways biológicos humanos (~2.500 vias). Cada pathway tem um ID (`R-HSA-...`), descrição e a lista de proteínas/genes envolvidos. É uma das principais fontes para anotação funcional em redes biológicas.
[^ECM]: **ECM** (*Extracellular Matrix* — matriz extracelular) — malha de proteínas e açúcares **fora** das células, que dá estrutura aos tecidos (como o "esqueleto" de cimento entre os "tijolos" das células). Em câncer, alterações na ECM são fortemente associadas à invasão tumoral e metástase: o tumor reorganiza esse cimento para abrir caminho.
[^LOGFC]: **logFC** (*log fold change*) — medida de quanto a expressão de um gene mudou entre duas condições, em escala logarítmica (base 2). `logFC = +1` significa expressão duplicada no grupo de teste; `logFC = -1` significa expressão reduzida pela metade.
[^CENT]: **Centralidade** — família de métricas que mede o quão "importante" um nó é na rede: grau (quantas conexões tem), proximidade (distância média aos outros nós), intermediação (quantos caminhos mínimos passam por ele), autovetor (conectado a nós também muito conectados). Análogo: numa rede de metrô, uma estação central é hub não só por ter muitas linhas mas por estar conectada a outras estações importantes.

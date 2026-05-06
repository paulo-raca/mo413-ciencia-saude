# Análise Prática — Continuação das aulas de 29/abril e 4/maio

[slides: PPI](slides-ppi.pdf) | [slides: miRNA-mRNA](slides-mirna-mrna.pdf)

Aula de André Santanchè (Laboratory of Information Systems — LIS, IC/UNICAMP) — 6 de maio de 2026

> Sem gravação.

---

## Em uma frase

Aula prática de **análise** que dá continuidade aos exercícios das aulas de [29/abril (miRNA-mRNA Network)](../2026-04-29%20-%20miRNA-mRNA%20Network/README.md) e 04/maio — mãos no Cytoscape e no workflow Orange para fechar o pipeline que constrói a rede miRNA-mRNA sobre os dados do TCGA-THCA e analisa sua topologia.

---

## Material de referência

Os PDFs nesta pasta são versões dos slides apresentados nas aulas anteriores, que voltaram a ser usadas como referência durante a prática:

- **slides-ppi.pdf** — bloco de redes PPI da aula de [30/03 — Redes PPI, Correlação e Workflow](../2026-03-30%20-%20Redes%20PPI%2C%20Correlação%20e%20Workflow/README.md).
- **slides-mirna-mrna.pdf** — slides da aula de [29/04 — miRNA-mRNA Network: Carcinoma de Tireoide (THCA)](../2026-04-29%20-%20miRNA-mRNA%20Network/README.md).

Os resumos conceituais detalhados de cada bloco estão nos READMEs das aulas originais linkados acima.

---

## Exercícios

A pasta [`exercicios/microRNA/`](exercicios/microRNA/) traz uma versão atualizada (06/maio) do mesmo conjunto de dados do exercício de 29/04 — agora menor e mais curado, com novos artefatos do Cytoscape (entre eles `projection-mRNA-mRNA_limma-backbone.csv`, uma extração de **backbone**[^BACKBONE] da projeção mRNA-mRNA filtrada por DEA[^DEA]) e os workflows Orange (`thca-mirna-mrna.ows` e `thca-mirna-mrna-r.ows`).

> Esta mesma pasta de exercícios é compartilhada com a aula de [04/05 — Análise Prática](../2026-05-04%20-%20Análise%20Prática/README.md) (via symlink), já que 29/04, 04/05 e 06/05 iteram sobre o mesmo conjunto de dados.

---

## Notas

[^BACKBONE]: **Backbone** de uma rede — sub-rede formada pelas arestas mais relevantes/fortes, obtida por algoritmos como o *disparity filter*. Serve para enxugar redes muito densas mantendo a estrutura central, como reduzir um mapa rodoviário só às rotas principais.
[^DEA]: **DEA** (*Differential Expression Analysis*) — análise estatística que identifica genes cuja expressão muda entre duas condições (ex.: tumor vs. tecido saudável). Filtrar por DEA antes de construir a rede concentra a análise nos genes biologicamente relevantes.

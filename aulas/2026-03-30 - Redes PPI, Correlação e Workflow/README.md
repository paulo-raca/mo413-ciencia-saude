# Redes PPI, Correlação e Workflow

[slides: PPI](slides-ppi.pdf) | [slides: Correlação](slides-correlacao.pdf) | [slides: Workflow](slides-workflow.pdf) | [guia Orange](guia-orange.pdf)

Aula de André Santanchè (UNICAMP) — 30 de março de 2026

---

## Redes PPI (Interação Proteína-Proteína)[^PPI]

Uma **rede PPI**[^PPI] é um mapa de quais proteínas[^PROTEINA] "conversam" entre si dentro da célula — pense num organograma de empresa onde os cargos são proteínas e as linhas entre eles são interações físicas.

Cada proteína é fabricada a partir de um **gene**[^GENE]. Por isso é possível ligar dois mundos:

```
gene A  ──codifica──►  proteína A
                            │
                        interação
                            │
gene B  ──codifica──►  proteína B
```

### Correlação de Expressão

**Expressão gênica**[^EXPRESSAO] é o quanto um gene está sendo "lido" e executado. Dois genes têm **expressão correlacionada** quando, ao longo de várias amostras, suas atividades sobem e descem juntas — como dois vendedores cujos resultados mensais sempre se movem no mesmo sentido.

Na rede PPI isso se representa assim:

```
gene A (expresso alto)  ──── alto correlado ───►  gene B (expresso alto)
gene C (expresso alto)  · · · baixo correlado · ·  gene D (expresso baixo)
```

A aresta (linha) só fica sólida quando a correlação ultrapassa um limiar; caso contrário ela é descartada ou pontilhada.

### Correlação de Expressão Diferencial

Variante mais específica: em vez de medir a expressão bruta, compara-se o **quanto a expressão mudou** em relação a um controle (ex.: tecido saudável vs. tumoral). Dois genes com variações correlacionadas são conectados; dois com variações descoladas não.

Referência central da aula: Chuang et al. (2007) — *Network-based classification of breast cancer metastasis*. Molecular Systems Biology, 3(1). DOI: 10.1038/msb4100180

---

## Rede de Correlação — Câncer de Mama

Aplicação prática do conceito acima usando o dataset público **GSE45827**[^GEO] (155 amostras de câncer de mama, subtipos Luminal-A, HER2 e Triple-Negative, + tecidos normais). Artigo de origem: Gruosso et al. (2016), EMBO Mol Med.

### Workflow GEO → Orange → Cytoscape

```
GEO (GSE45827)
     │
     ▼ download formato SOFT[^SOFT]
Arquivo .soft
     │
     ▼ importar no Orange[^ORANGE]
Expressão média por gene
     │
     ├──► Caminho dos Nós ──────────────────────► arquivo nodes.csv
     │    (Entrez ID, Gene Symbol, Expressão Média)
     │
     └──► Caminho das Arestas
          │  filtra Log2 > 12, Gene ID definido
          │  Unique Entrez ID
          │  Transpõe (genes nas colunas)
          │  Calcula correlação entre amostras
          │  Filtra correlação > 0.5
          │  Renomeia Source/Target
          └──────────────────────────────────────► arquivo edges.csv
                                                        │
                                                        ▼
                                               Cytoscape (análise de rede)
```

O dataset e o workflow do professor estão disponíveis em: `datasci4health.github.io/networks/breast-cancer/geo-subtypes/05-expression-correlation`

---

## Workflow, Método Científico e Reprodutibilidade

### Por que reprodutibilidade importa?

A pesquisa científica deve poder ser **repetida** por outras pessoas — e até pelo próprio autor. Uma pesquisa de 1.576 cientistas (Baker, 2016, *Nature*) mostrou que a maioria já falhou em reproduzir experimentos de outros ou os próprios. Os maiores culpados: *selective reporting*, pressão para publicar e código/métodos não disponíveis.

Tipos de reprodutibilidade (Holdgraf et al., 2018):
- **Técnica**: é *possível* reproduzir o resultado
- **Prática**: qualquer pessoa consegue reproduzir *sem dificuldade* — esta é a meta

### Workflow como ferramenta de reprodutibilidade

Um **workflow** é um padrão de processo repetível — como uma receita de bolo que organiza ingredientes (recursos) e passos (atividades) de forma que qualquer um possa refazer o experimento e obter o mesmo resultado.

Modelo básico:

```
[Atividade A] ──── Fluxo de Dados ────► [Atividade B]
                       │
                  [Artefato / Arquivo]
```

Uma atividade pode gerar múltiplos artefatos que alimentam atividades paralelas.

---

## Guia Orange

**Orange** é uma ferramenta visual de ciência de dados: em vez de escrever código, você arrasta blocos (chamados *widgets*) e conecta-os para montar o pipeline de análise — como montar um circuito elétrico com peças.

### Operações fundamentais

| Operação | Widget | O que faz |
|---|---|---|
| Importar dados | CSV File Import | Lê um arquivo `.csv` e cria uma tabela |
| Ver tabela | Data Table | Mostra a tabela na tela |
| Remover duplicatas | Unique | Mantém apenas uma linha por valor de coluna escolhida |
| Projeção (colunas) | Select Columns | Seleciona quais colunas manter — "recorta" colunas |
| Seleção (linhas) | Select Rows | Filtra linhas por condição — "recorta" linhas |
| Junção | Merge Data | Une duas tabelas por uma coluna-chave (equivalente ao JOIN do SQL) |

Cada widget recebe dados pela entrada (esquerda) e entrega pela saída (direita); você conecta widgets puxando uma linha de saída para entrada.

---

[^PPI]: **PPI** — *Protein-Protein Interaction*, interação proteína-proteína. Mapa de quais proteínas se encaixam fisicamente ou trabalham juntas dentro da célula.
[^PROTEINA]: **Proteína**: molécula fabricada a partir da receita de um gene. É a "máquina" que realiza funções na célula — defesa imune, transporte, estrutura, sinalização.
[^GENE]: **Gene**: trecho do DNA que contém a receita para fabricar uma proteína específica.
[^EXPRESSAO]: **Expressão gênica**: o nível de atividade de um gene — o quanto ele está sendo lido e transformado em proteína num dado momento ou tipo de célula.
[^GEO]: **GEO** — *Gene Expression Omnibus*, repositório público do NCBI onde pesquisadores depositam dados de expressão gênica. Acesso: ncbi.nlm.nih.gov/geo
[^SOFT]: **SOFT** — *Simple Omnibus Format in Text*, formato de arquivo texto usado pelo GEO para armazenar dados de expressão gênica junto com metadados das amostras.
[^ORANGE]: **Orange**: plataforma de código aberto para ciência de dados visual (orange.biolab.si). Permite montar pipelines de análise arrastando blocos sem escrever código.

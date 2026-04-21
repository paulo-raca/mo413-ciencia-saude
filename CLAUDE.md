# CLAUDE.md — Instruções para o Assistente

## Contexto

Este repositório é material de estudo da disciplina **MO413A — Ciência e Visualização de Dados em Saúde** (UNICAMP, 1º semestre de 2026). O usuário é estudante de **biologia computacional / bioinformática** mas **não tem background em biologia** — todos os termos e conceitos biológicos devem ser explicados como se o leitor nunca tivesse estudado biologia. Use analogias do cotidiano sempre que possível.

---

## Estrutura do Repositório

```
.
├── README.md                          # Visão geral da disciplina
├── CLAUDE.md                          # Este arquivo
├── DATASETS.md                        # Índice de bases de dados usadas nas aulas
├── aulas/                             # Uma subpasta por aula
│   └── YYYY-MM-DD - Assunto/
│       ├── slides.pdf                 # Slides originais da aula
│       ├── README.md                  # Resumo + links para slides e YouTube
│       └── exercicios/                # Arquivos de exercício (se houver)
│           └── ...
├── projeto/                           # Projeto semestral da equipe ALFAK
│   ├── README.md                      # Resumo do projeto semestral
│   ├── slides.pdf                     # Slides de apresentação do projeto
│   ├── L1 - How Wolves Chang Rivers/  # Entrega L1
│   │   └── README.md
│   └── L2 - artigos/                  # Entrega L2
│       ├── README.md
│       └── artigos/
│           ├── README.md              # Índice com resumo de um parágrafo por artigo
│           ├── A/                     # Artigos do subgrupo A (Augusto, Felipe, Luis)
│           │   └── {autor}{ano} - {Assunto}/
│           │       ├── paper.pdf      # PDF do artigo
│           │       └── README.md      # Resumo detalhado
│           └── B/                     # Artigos do subgrupo B (Paulo, Naruan, Alan)
│               └── {autor}{ano} - {Assunto}/
│                   ├── paper.pdf
│                   └── README.md
└── datasci4health.github.io/          # Submodule — site oficial da disciplina
```

---

## Como Adicionar uma Nova Aula

1. Criar subpasta: `aulas/YYYY-MM-DD - Assunto/`
2. Copiar o PDF dos slides para `slides.pdf` dentro dessa pasta
3. Criar `README.md` com o seguinte cabeçalho:

```markdown
# Título da Aula

[slides](slides.pdf) | [YouTube](https://youtube.com/watch?v=ID)

Aula de NOME (UNICAMP) — DD de mês de 2026
```

4. Ler o PDF dos slides e escrever o resumo em português, explicando **todos** os termos biológicos para leigos
5. Adicionar a aula na seção "Aulas" do `README.md` raiz com um parágrafo de resumo e links
6. Atualizar o `DATASETS.md` da raiz (ver seção "Como Atualizar o DATASETS.md" abaixo) com qualquer base de dados, ontologia, dataset específico ou ferramenta de acesso a dados nova que apareça na aula

Se não houver gravação, omitir o link do YouTube e mencionar isso no README da aula.

---

## Como Adicionar um Exercício

Se o exercício for da mesma data de uma aula existente:

- Criar subpasta `exercicios/` dentro da pasta da aula correspondente
- Colocar os arquivos (`.cys`, `.csv`, `.md`, imagens) dentro

Se for uma aula prática sem slides próprios (como 2026-03-18):

- Criar subpasta nova em `aulas/YYYY-MM-DD - Assunto/`
- Criar `README.md` mencionando qual aula usou os mesmos slides
- Criar subpasta `exercicios/` com os arquivos

Se o exercício trouxer um arquivo novo baixado de uma base pública (ex.: export do Open Targets, TSV do Reactome, CSV do GEO), **adicionar a linha correspondente na tabela "Datasets dos Exercícios" do `DATASETS.md`**.

---

## Como Atualizar o DATASETS.md

O arquivo `DATASETS.md` na raiz é o **índice único** de todas as bases de dados, ontologias, datasets específicos e ferramentas de acesso a dados mencionadas nas aulas. Ele deve ser mantido sincronizado com as aulas.

**Quando atualizar:**

- Ao adicionar uma aula nova que mencione qualquer base ou ferramenta não listada
- Ao adicionar um exercício que use um arquivo baixado de uma base pública
- Ao perceber que uma entrada existente ficou incompleta ou desatualizada

**Como atualizar uma base já listada:**

- Acrescentar a data da aula nova ao campo "**Aulas:**" da seção correspondente
- Complementar o campo "**Uso:**" se a aula trouxer uso novo relevante

**Como adicionar uma base nova:**

- Escolher a seção temática apropriada (PPI, Expressão, Vias, Grafos de Conhecimento, Ontologias, Referência, Fármaco-alvo, Ferramentas)
- Seguir o mesmo template das entradas existentes: **O que é**, **URL**, **Aulas**, **Uso** (+ **Referência** quando for um dataset/artigo específico)
- Se for um dataset específico (ex.: GSE45827), aninhá-lo sob a base que o hospeda (ex.: sob GEO)
- Atualizar a tabela final "Resumo por Categoria" se for uma categoria nova
- Se houver arquivo de exercício novo, adicionar também na tabela "Datasets dos Exercícios"
- Se introduzir uma sigla nova, criar footnote `[^KEY]: definição` no final do arquivo — em linguagem simples, sem assumir background em biologia

---

## Como Adicionar uma Nova Entrega de Projeto (L3, L4, ...)

1. Criar subpasta em `projeto/L{N} - Titulo/`
2. Criar `README.md` com enunciado e/ou resumo da entrega
3. Adicionar seção correspondente no `README.md` raiz (em "Projeto Semestral")

---

## Como Atualizar o Submodule

O diretório `datasci4health.github.io/` é um submodule apontando para o repositório oficial da disciplina. Para atualizar para a versão mais recente:

```bash
git submodule update --remote datasci4health.github.io
git add datasci4health.github.io
git commit -m "Atualiza submodule datasci4health.github.io"
```

---

## Arquivos Binários e Git LFS

Todos os arquivos binários do repositório são rastreados via **Git LFS** (Large File Storage). As extensões configuradas em `.gitattributes` são:

- `*.pdf` — slides e artigos
- `*.png` — imagens
- `*.cys` — sessões do Cytoscape

Ao adicionar novos arquivos binários dessas extensões, o LFS os captura automaticamente. Para novos tipos binários, adicionar ao `.gitattributes` antes de commitar:

```bash
git lfs track "*.extensao"
git add .gitattributes
```

---

## Convenções de Nomenclatura

| Item             | Padrão                                               |
| ---------------- | ---------------------------------------------------- |
| Pasta de aula    | `YYYY-MM-DD - Assunto`                               |
| Slides           | `slides.pdf`                                         |
| Resumo de aula   | `README.md`                                          |
| Pasta de artigo  | `{autor}{ano} - {Assunto com espaços e maiúsculas}/` |
| Resumo de artigo | `{autor}{ano} - {Assunto}/README.md`                 |
| PDF de artigo    | `{autor}{ano} - {Assunto}/paper.pdf`                 |

---

## Como Escrever Resumos

### Resumos de Aulas

- Ler o PDF dos slides com a ferramenta `Read`
- Escrever em **português**
- Começar com o cabeçalho padrão (links para slides e YouTube)
- Explicar **todo termo biológico** na primeira vez que aparecer — não assumir conhecimento prévio
- Usar analogias simples: genes como "receitas", proteínas como "máquinas", redes como "mapas de metrô"
- Estruturar com cabeçalhos `##` por tema
- Usar **diagramas Mermaid** (`graph TD`, `flowchart`, `sequenceDiagram`) sempre que possível para ilustrar fluxos, pipelines e relações entre conceitos

### Resumos de Artigos Científicos

Estrutura padrão (`artigos/{subgrupo}/{autor}{ano} - {Assunto}/README.md`):

1. **Metadados** — tabela com título, autores, revista, ano, DOI, acesso
2. **Problema investigado** — o que o artigo tenta resolver e por quê importa
3. **Dados utilizados** — fontes, tamanho, tipo
4. **Pipeline/Metodologia** — diagrama ASCII do fluxo do trabalho; **adicionar também um diagrama Mermaid** (`graph TD`) sempre que possível para melhor visualização
5. **Estratégia de grafo** — que modelo de grafo foi usado e qual algoritmo de rede complexa foi aplicado; **obrigatoriamente incluir um diagrama Mermaid** (`graph TD`) mostrando nós, arestas e o pipeline do algoritmo
6. **Resultados principais** — tabela com os achados mais importantes
7. **Relevância para o projeto** — por que este artigo importa para o projeto de câncer de pele
8. **Referência completa** — formatos ABNT, Vancouver e APA
9. **Notas** — footnotes Markdown (`[^KEY]: definição`) para cada sigla usada no texto; no texto, marcar a primeira ocorrência de cada sigla com `[^KEY]`

Não usar seção de Glossário separada — as definições ficam exclusivamente nas notas de rodapé.

---

## Contexto do Projeto Semestral

**Título:** Câncer de Pele e seus Tipos: uma Análise do Perfil de Expressão Gênica em Redes

**Equipe ALFAK:** Alan Freitas Ribeiro, Augusto José Peterlevitz, Felipe Kennedy Carvalho Torquato, Luis Henrique Angélico, Naruan Francisco Ferraz e Ferraz, Paulo Costa

**Subgrupo A (artigos L2 — pasta `artigos/A/`):** Augusto José Peterlevitz, Felipe Kennedy Carvalho Torquato, Luis Henrique Angélico

**Subgrupo B (artigos L2 — pasta `artigos/B/`):** Paulo Costa, Naruan Francisco Ferraz e Ferraz, Alan Freitas Ribeiro

**Objetivo:** Comparar redes de interação gênica de melanoma, não-melanoma e tecido saudável usando dados do GEO, STRING e Cytoscape. Identificar hubs, módulos e diferenças topológicas entre as redes. Análise adicional com Graph Attention Networks (GAT) sobre TCGA-SKCM.

**Datasets GEO:**

- Saudável: GSE4570, GSE2503, GSE53462
- Melanoma: GSE4570, GSE8401, GSE7553
- Não-melanoma: GSE2503, GSE45216, GSE53462

**Ferramentas:** STRING, Cytoscape (CytoNCA, NetworkAnalyzer, MCODE), Python (PyTorch, Pandas, Scikit-learn)

---

## Nota sobre Biologia

O usuário **não tem background em biologia**. Sempre que aparecer um termo biológico — gene, proteína, RNA, expressão gênica, melanoma, carcinoma, via metabólica, etc. — explicar como se fosse a primeira vez, usando linguagem simples e analogias. Exemplos:

- **Gene**: como uma receita dentro de um livro de culinária (o DNA). A célula lê a receita para fabricar uma proteína.
- **Expressão gênica**: o quanto um gene está sendo "lido" e executado pela célula. Um gene muito expresso está muito ativo.
- **Proteína**: a molécula fabricada a partir da receita do gene. Faz o trabalho real na célula.
- **Rede PPI**: mapa de quais proteínas trabalham juntas, como um organograma de uma empresa.
- **Hub**: gene/proteína muito conectado na rede — como uma estação central de metrô.
- **Melanoma**: câncer originado nos melanócitos (células que produzem o pigmento da pele).

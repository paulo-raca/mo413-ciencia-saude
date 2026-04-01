# Orange e Workflow (Aula Prática)

[slides: Workflow e Câncer de Mama](slides-workflow.pdf) | [guia Orange](guia-orange.pdf)

Aula de André Santanchè (UNICAMP) — 1º de abril de 2026

> Aula prática de continuação. A teoria de Workflow e Reprodutibilidade foi introduzida na aula de [30/03](../2026-03-30%20-%20Redes%20PPI%2C%20Correla%C3%A7%C3%A3o%20e%20Workflow/README.md). Esta aula aprofunda o Guia Orange com novos widgets e realiza o exercício prático de construção de rede de correlação.

---

## Novos Widgets Orange

Esta aula expande o guia apresentado em 30/03 com dois widgets novos.

### Formula — Criar colunas calculadas

O widget **Formula** cria novas colunas a partir de expressões matemáticas ou de texto aplicadas às colunas existentes — como uma fórmula do Excel, mas dentro de um pipeline visual.

```
[Tabela] ──Data──► [Formula] ──Data──► [Nova tabela com coluna extra]
```

#### Fórmulas sobre texto (Strings)

| Operação | Sintaxe | O que faz |
|---|---|---|
| Substring | `campo[início:fim]` | Extrai parte do texto. Índice começa em 0; fim é excluído; `-1` = último caractere |
| Minúsculas | `campo.lower()` | Converte todo o texto para minúsculas |
| Dividir | `campo.split('sep')` | Divide o texto pelo separador e retorna lista |
| Substituir | `campo.replace('a','b')` | Troca todas as ocorrências de `a` por `b` |
| Remover espaços | `campo.strip()` | Remove espaços extras no início e fim |
| Converter para inteiro | `int(campo)` | Transforma texto em número inteiro |
| Converter para decimal | `float(campo)` | Transforma texto em número decimal |

**Exemplo prático:** a expressão `Feature_name[0:12].lower()` pega os primeiros 12 caracteres do campo `Feature_name` e converte para minúsculas.

### Join — Unir duas tabelas

O widget **Merge Data** une duas tabelas por uma coluna em comum — exatamente como o JOIN do SQL ou o PROCV do Excel.

```
[Tabela 1] ──Data──────────►
                             [Merge Data] ──Data──► [Tabela unida]
[Tabela 2] ──Extra Data──►
```

**Como configurar:** no painel do widget, escolher qual coluna da Tabela 1 (`Data`) corresponde a qual coluna da Tabela 2 (`Extra Data`).

Exemplo: unir uma tabela de **armários** (com coluna `Ocupante`) a uma tabela de **pessoas** (com coluna `IdPessoa`) — o widget cruza os valores iguais e adiciona Nome e Telefone a cada linha de armário.

---

## Revisão: Workflow e Reprodutibilidade

Os slides desta aula retomam o tema de método científico e workflow introduzido em 30/03. Pontos principais:

### Método Científico (Descartes, 1637)

Quatro regras do *Discurso do Método*:
1. Só aceitar como verdadeiro o que se conhece claramente
2. Dividir cada problema em partes menores
3. Começar pelos objetos mais simples e avançar gradualmente
4. Fazer enumerações completas para não omitir nada

Lavoisier (1789) aplicou esse método documentando cada experimento químico com desenhos detalhados dos aparatos — tornando o trabalho **reproduzível** por outros.

### Por que Reprodutibilidade é um Problema Hoje?

Pesquisa Nature com 1.576 cientistas (Baker, 2016): a maioria já falhou em reproduzir experimentos — dos outros e os próprios. Principais causas:
- *Selective reporting*: publicar apenas os resultados favoráveis
- Pressão para publicar
- Código e métodos não disponíveis

### Tipos de Reprodutibilidade (Holdgraf et al., 2018)

| Tipo | Definição |
|---|---|
| **Técnica** | É *possível* reproduzir — o mínimo necessário |
| **Prática** | Qualquer pessoa consegue reproduzir *sem dificuldade* — a meta real |

### Workflow como Solução

Um **workflow** organiza sistematicamente recursos e tarefas num padrão repetível. Benefícios: reprodutibilidade, reuso e documentação automática do processo.

```
[Atividade A] ──Fluxo de Dados──► [Atividade B] ──► [Atividade C]
                    │                    │
              [Artefato/Arquivo]   [Artefato/Arquivo]
```

---

## Exercício

O arquivo de exercício está em [`exercicios/`](exercicios/). Trata-se de um workflow Orange (`.ows`) para construção da rede de correlação de expressão gênica[^EXPRESSAO] a partir do dataset GSE45827[^GEO].

---

[^EXPRESSAO]: **Expressão gênica**: o nível de atividade de um gene — o quanto ele está sendo lido e transformado em proteína. Genes muito expressos estão "ligados no máximo"; genes pouco expressos estão "no mudo".
[^GEO]: **GEO** — *Gene Expression Omnibus*, repositório público do NCBI com dados de expressão gênica de milhares de estudos. O dataset GSE45827 contém dados de 155 amostras de câncer de mama (subtipos Luminal-A, HER2, Triple-Negative e tecido normal).

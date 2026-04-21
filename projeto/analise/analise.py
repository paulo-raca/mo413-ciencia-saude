import marimo

__generated_with = "0.21.1"
app = marimo.App(width="medium")


@app.cell
def imports():
    import marimo as mo
    import GEOparse
    import pandas as pd
    import numpy as np
    from pathlib import Path

    return GEOparse, Path, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Câncer de Pele — Análise de Expressão Gênica em Redes

    **Equipe ALFAK** | MO413A — UNICAMP 2026

    ---

    ## Datasets GEO

    | Dataset | Grupos | Amostras | Descrição |
    |---------|--------|----------|-----------|
    | [GSE4570](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE4570) | Saudável, Melanoma | 8 | Melanócitos normais vs. linhagens de melanoma avançado (Affymetrix HG-U133A) |
    | [GSE2503](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE2503) | Saudável, Não-melanoma | 15 | Pele normal vs. queratose actínica vs. SCC em pacientes transplantados (Affymetrix HG-U133A) |
    | [GSE53462](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE53462) | Saudável, Não-melanoma | 26 | Pele normal vs. BCC vs. SCC — classificação molecular (Illumina HumanHT-12 v4) |
    | [GSE8401](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE8401) | Melanoma | 83 | Melanoma primário vs. metástases — assinatura de agressividade (Affymetrix HG-U133A) |
    | [GSE7553](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE7553) | Melanoma | 87 | Espectro completo: pele normal, melanoma in situ, primário, metastático, BCC, SCC (Affymetrix U133 Plus 2.0) |
    | [GSE45216](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE45216) | Não-melanoma | 40 | Queratose actínica vs. SCC cutâneo — 196 DEGs identificados (Affymetrix U133 Plus 2.0) |

    ---

    ## Pipeline

    - [x] **1. Download dos datasets GEO** — GEOparse, cache local em `data/geo/`
    - [ ] **2. Pré-processamento**
        - [ ] Extrair matrizes de expressão (genes × amostras) de cada `.soft.gz`
        - [ ] Mapear subgrupo de amostra (ex.: *in situ*, primário, metastático, BCC, SCC, normal) a partir da metadata `characteristics_ch1`
        - [ ] Verificar normalização (log2 já aplicado pelo depositante?) e aplicar se necessário
        - [ ] Deduplicar sondas por gene (equivalente ao widget `Unique` do Orange)
        - [ ] *(Depois, ao integrar múltiplos GEOs)* correção de batch effect
    - [ ] **3. Análise de Expressão Diferencial (DEA)** — granularidade fina, por estágio/tipo
        - [ ] Pele normal × Melanoma in situ *(GSE7553)*
        - [ ] Pele normal × Melanoma primário *(GSE7553, GSE4570, GSE8401)*
        - [ ] Pele normal × Melanoma metastático *(GSE7553, GSE8401)*
        - [ ] Pele normal × Carcinoma basocelular (BCC) *(GSE7553, GSE53462)*
        - [ ] Pele normal × Carcinoma espinocelular (SCC) *(GSE7553, GSE2503, GSE45216, GSE53462)*
        - [ ] *(Opcional)* progressões: in situ → primário → metastático; AK → SCC *(GSE45216)*
        - [ ] Dois passes por comparação: completo + filtrado por `p ≤ 0.001` (replica o Orange); avaliar também `|logFC| > 1`
    - [ ] **4. Anotação externa — Open Targets**
        - [ ] Baixar alvos associados às doenças via API (melanoma: `EFO_0000756`; BCC/SCC: MONDO correspondentes)
        - [ ] Anexar `globalScore` a cada gene como atributo de nó (0–1, drogabilidade/relevância clínica)
    - [ ] **5. Construção da rede PPI**
        - [ ] Query dos DEGs na API do STRING
        - [ ] Filtrar por `combined_score` (ex.: ≥ 0.4 = confiança média)
    - [ ] **6. Análise de rede** (Cytoscape / Python — NetworkX, igraph)
        - [ ] Hubs (degree, betweenness, closeness, eigenvector)
        - [ ] Detecção de módulos (MCODE / Louvain / Leiden)
    - [ ] **7. Comparação entre redes**
        - [ ] Hubs compartilhados vs. específicos por tipo/estágio
        - [ ] Genes ganhos/perdidos entre estágios
        - [ ] Diferenças topológicas (distribuição de grau, clustering)
    - [ ] **8. Graph Attention Network (GAT)** — análise adicional sobre TCGA-SKCM
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 1. Download dos Datasets GEO
    """)
    return


@app.cell
def config(Path):
    GEO_DIR = Path("data/geo")
    GEO_DIR.mkdir(parents=True, exist_ok=True)

    DATASETS = {
        "saudavel":     ["GSE4570", "GSE2503", "GSE53462"],
        "melanoma":     ["GSE4570", "GSE8401", "GSE7553"],
        "nao_melanoma": ["GSE2503", "GSE45216", "GSE53462"],
    }

    ALL_IDS = sorted({gse for ids in DATASETS.values() for gse in ids})
    return ALL_IDS, GEO_DIR


@app.cell
def download(ALL_IDS, GEO_DIR, GEOparse, mo):
    gse_objects = {}
    for _gse_id in mo.status.progress_bar(ALL_IDS, title="Baixando datasets GEO"):
        gse_objects[_gse_id] = GEOparse.get_GEO(
            geo=_gse_id,
            destdir=str(GEO_DIR),
            silent=True,
        )
    return (gse_objects,)


@app.cell
def summary(gse_objects, mo):
    _rows = []
    for _gse_id, _gse in gse_objects.items():
        _rows.append({
            "Dataset": _gse_id,
            "Título": _gse.metadata.get("title", [""])[0][:60],
            "Amostras": len(_gse.gsms),
            "Plataforma": ", ".join(_gse.metadata.get("platform_id", ["?"])),
        })
    mo.ui.table(_rows, label="Datasets carregados")
    return


if __name__ == "__main__":
    app.run()

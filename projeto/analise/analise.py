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

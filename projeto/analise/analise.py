import marimo

__generated_with = "0.21.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def imports():
    import marimo as mo
    import GEOparse
    import pandas as pd
    import numpy as np
    from pathlib import Path
    from scipy import stats

    return GEOparse, Path, mo, np, pd, stats


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
def download_datasets(GEOparse, Path, mo):
    mo.output.append(mo.md("## 1. Download dos Datasets GEO"))

    GEO_DIR = Path("data/geo")
    GEO_DIR.mkdir(parents=True, exist_ok=True)

    DATASETS = {
        "saudavel":     ["GSE4570", "GSE2503", "GSE53462"],
        "melanoma":     ["GSE4570", "GSE8401", "GSE7553"],
        "nao_melanoma": ["GSE2503", "GSE45216", "GSE53462"],
    }
    ALL_IDS = sorted({gse for ids in DATASETS.values() for gse in ids})

    # Cache persistente: o parsing do .soft.gz é caro (~30s no total), mas o
    # resultado só muda se ALL_IDS mudar. Primeiro run baixa+parseia; depois
    # restaura do pickle em __marimo__/cache/.
    with mo.persistent_cache("geo_datasets"):
        gse_objects = {}
        for _gse_id in mo.status.progress_bar(
            ALL_IDS,
            title="Baixando datasets GEO",
            remove_on_exit=True,
        ):
            gse_objects[_gse_id] = GEOparse.get_GEO(
                geo=_gse_id,
                destdir=str(GEO_DIR),
                silent=True,
            )
    return (gse_objects,)


@app.cell(hide_code=True)
def datasets_summary(gse_objects, mo, pd):
    def _panel(gsid, gse):
        title = gse.metadata.get("title", [""])[0]
        platform = ", ".join(gse.metadata.get("platform_id", ["?"]))
        submitted = gse.metadata.get("submission_date", ["?"])[0]
        summary_text = gse.metadata.get("summary", [""])[0]
        if len(summary_text) > 500:
            summary_text = summary_text[:500].rstrip() + "…"

        header = mo.md(f"""
        **[{gsid}](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={gsid})** — {title}

        | Plataforma | Amostras | Submissão |
        | --- | --- | --- |
        | `{platform}` | {len(gse.gsms)} | {submitted} |

        {summary_text}

        #### Amostras
        """)

        samples_df = pd.DataFrame([
            {
                "GSM": gsm_id,
                "Título": gsm.metadata.get("title", [""])[0],
                "Características": " · ".join(gsm.metadata.get("characteristics_ch1", [])),
            }
            for gsm_id, gsm in gse.gsms.items()
        ])

        return mo.vstack([header, samples_df])

    mo.ui.tabs({gsid: _panel(gsid, g) for gsid, g in gse_objects.items()})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ## 2. Reprodução do pipeline Orange — Metastatic Melanoma

    Esta seção reproduz fielmente `workspace/Metastatic Melanoma/Melanoma.ows` em Python,
    servindo como **baseline de validação** antes de generalizar para os outros subgrupos.

    Passos (espelham o `.ows`):

    1. Filtrar amostras do GSE7553 — **Metastatic Melanoma** × **Normal Skin**.
    2. Construir matriz de expressão (sondas × amostras) e deduplicar sondas.
    3. DEA com Welch's t-test; filtros combinados `|logFC| ≥ 2.3` **e** `p ≤ 0.001`.
    4. Anotar cada gene com `oncogeneScore` do Open Targets (EFO_0000756).
    5. Validar contra `workspace/Metastatic Melanoma/Nodes_cytoscape.csv`.
    """)
    return


@app.cell
def mm_samples(gse_objects):
    gse_mm = gse_objects["GSE7553"]

    def _has_char(gsm, substr):
        return any(substr.lower() in c.lower()
                   for c in gsm.metadata.get("characteristics_ch1", []))

    metastatic_gsms = [gid for gid, gsm in gse_mm.gsms.items()
                       if _has_char(gsm, "metastatic melanoma")]
    normal_gsms = [gid for gid, gsm in gse_mm.gsms.items()
                   if _has_char(gsm, "normal skin")]
    return gse_mm, metastatic_gsms, normal_gsms


@app.cell(hide_code=True)
def mm_samples_show(metastatic_gsms, mo, normal_gsms):
    mo.md(f"""
    **Seleção de amostras do GSE7553** (espelha `sample_substring` do Orange):

    - Metastatic Melanoma: **{len(metastatic_gsms)}** amostras
    - Normal Skin: **{len(normal_gsms)}** amostras
    """)
    return


@app.cell
def mm_expression(gse_mm, metastatic_gsms, normal_gsms, pd):
    selected = metastatic_gsms + normal_gsms
    cols = [
        gse_mm.gsms[gid].table.set_index("ID_REF")["VALUE"].rename(gid)
        for gid in selected
    ]
    expr_mm = pd.concat(cols, axis=1)

    # Unique do Orange: deduplica sondas (primeira ocorrência vence)
    expr_mm = expr_mm[~expr_mm.index.duplicated(keep="first")]

    # IMPORTANTE: mantemos valores brutos — no Melanoma.ows o GEO SOFT Extractor
    # está com transform_log2=False, e a fórmula do Orange para LogFC é
    # log2(mean_a / mean_b) calculada sobre valores brutos.
    expr_mm = expr_mm.dropna(how="all")
    return (expr_mm,)


@app.cell
def mm_platform(gse_mm):
    # GPL570 (HG-U133 Plus 2.0) — mapeia probe ID -> Gene Symbol + Entrez ID.
    # Sondas multi-mapeadas (p.ex. 'DDR1 /// MIR4640') ficam com o primeiro gene
    # só — mesmo comportamento de deduplicação do Orange.
    gpl_id = next(iter(gse_mm.gpls))
    gpl_table = gse_mm.gpls[gpl_id].table
    probe_map = gpl_table.set_index("ID")[["Gene Symbol", "ENTREZ_GENE_ID"]].copy()
    probe_map["Gene Symbol"] = (
        probe_map["Gene Symbol"].astype(str).str.split(" /// ").str[0].str.strip()
    )
    probe_map["Entrez ID"] = (
        probe_map["ENTREZ_GENE_ID"].astype(str).str.split(" /// ").str[0].str.strip()
    )
    probe_map = probe_map[["Gene Symbol", "Entrez ID"]]
    probe_map = probe_map.replace({"nan": None, "": None}).dropna()
    return (probe_map,)


@app.cell
def mm_dea(expr_mm, metastatic_gsms, normal_gsms, np, pd, probe_map, stats):
    m_cols = [c for c in expr_mm.columns if c in metastatic_gsms]
    n_cols = [c for c in expr_mm.columns if c in normal_gsms]

    m = expr_mm[m_cols].to_numpy()
    n = expr_mm[n_cols].to_numpy()

    # LogFC no estilo Orange: log2 da razão entre médias brutas.
    # NB: não equivale a mean(log2(A)) - mean(log2(B)).
    logfc = np.log2(m.mean(axis=1) / n.mean(axis=1))

    # Student's t-test (equal_var=True) em valores brutos — é o que o widget
    # 'Differential Expression' da Orange3-Bioinformatics usa por padrão.
    _t, pval = stats.ttest_ind(m, n, axis=1, equal_var=True, nan_policy="omit")

    dea_mm = pd.DataFrame(
        {"LogFC": logfc, "p-value": pval},
        index=expr_mm.index,
    ).join(probe_map, how="left")
    return (dea_mm,)


@app.cell
def mm_filter(dea_mm):
    # Replica o Merge do Orange: filtros combinados |logFC| >= 2.3 E p <= 0.001
    mask = (dea_mm["LogFC"].abs() >= 2.3) & (dea_mm["p-value"] <= 0.001)
    filtered_mm = dea_mm.loc[mask].copy()

    # Agrega por gene: múltiplas sondas -> mantém a de maior |LogFC|
    filtered_mm["_abs_fc"] = filtered_mm["LogFC"].abs()
    filtered_mm = (
        filtered_mm
        .sort_values("_abs_fc", ascending=False)
        .drop_duplicates(subset="Entrez ID", keep="first")
        .drop(columns="_abs_fc")
        .dropna(subset=["Entrez ID", "Gene Symbol"])
    )
    return (filtered_mm,)


@app.cell
def mm_opentargets(Path, pd):
    ot_path = Path("workspace/Metastatic Melanoma/OT-EFO_0000756-associated-targets-4_20_2026-v26_03.tsv")
    ot = pd.read_csv(ot_path, sep="\t")
    ot_scores = (
        ot[["symbol", "globalScore"]]
        .dropna(subset=["symbol"])
        .drop_duplicates(subset="symbol", keep="first")
        .rename(columns={"symbol": "Gene Symbol", "globalScore": "oncogeneScore"})
    )
    return (ot_scores,)


@app.cell
def mm_final(filtered_mm, ot_scores, pd):
    final_mm = (
        filtered_mm
        .merge(ot_scores, on="Gene Symbol", how="left")
        .loc[:, ["Entrez ID", "Gene Symbol", "LogFC", "p-value", "oncogeneScore"]]
        .reset_index(drop=True)
    )
    # Entrez ID no baseline do Orange é inteiro — coage para permitir comparação.
    final_mm["Entrez ID"] = pd.to_numeric(final_mm["Entrez ID"], errors="coerce").astype("Int64")
    return (final_mm,)


@app.cell(hide_code=True)
def mm_validate(Path, final_mm, mo, pd):
    expected = pd.read_csv(Path("workspace/Metastatic Melanoma/Nodes_cytoscape.csv"))

    got_genes = set(final_mm["Gene Symbol"].dropna())
    exp_genes = set(expected["Gene Symbol"].dropna())

    common = got_genes & exp_genes
    only_got = got_genes - exp_genes
    only_exp = exp_genes - got_genes

    union = got_genes | exp_genes
    jaccard = len(common) / len(union) if union else 0.0

    mo.md(f"""
    ### Comparação com baseline do Orange

    | Métrica | Valor |
    | --- | --- |
    | Genes no notebook | {len(final_mm)} |
    | Genes esperados (Orange) | {len(expected)} |
    | Em comum | {len(common)} |
    | Só no notebook | {len(only_got)} |
    | Só no Orange | {len(only_exp)} |
    | Similaridade de Jaccard | {jaccard:.2%} |

    **Status conhecido:** pipeline tem **recall ~100 %** (quase todos os genes do
    Orange aparecem no resultado do notebook) mas **precision ~45 %** — o notebook
    marca mais genes como significativos. Valores absolutos de `LogFC` também
    divergem sistematicamente (ex.: KRT14 = −4.25 aqui, −3.74 no Orange).

    Investigação futura: identificar se o widget `Differential Expression` da
    Orange3-Bioinformatics aplica algum filtro/normalização adicional (expressão
    mínima, quantile norm, piso em valores baixos) não óbvio no `.ows`.
    """)
    return


@app.cell
def mm_save(Path, final_mm):
    # Salva a saída do notebook para conferência lado a lado com o Nodes_cytoscape.csv
    out_dir = Path("output/Metastatic Melanoma")
    out_dir.mkdir(parents=True, exist_ok=True)
    final_mm.to_csv(out_dir / "Nodes_cytoscape.csv", index=False)
    return


if __name__ == "__main__":
    app.run()

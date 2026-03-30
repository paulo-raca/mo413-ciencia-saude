# Resumo: Chen et al. (2021)

**Título:** Seven key hub genes identified by gene co-expression network in cutaneous squamous cell carcinoma
**Revista:** BMC Cancer, vol. 21, artigo 852
**DOI:** https://doi.org/10.1186/s12885-021-08604-y
**Autores:** Huizhen Chen, Jiankang Yang, Wenjuan Wu

> **Nota:** O artigo é frequentemente citado como "Zhang et al." por engano; os autores corretos são Chen, Yang e Wu.

---

## Glossário de Termos

| Termo                         | O que significa                                                                                                                                                                                                                                                 |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **cSCC**                      | _Cutaneous Squamous Cell Carcinoma_ — Carcinoma Espinocelular Cutâneo: o segundo tipo de câncer de pele mais comum, originado nas células escamosas da camada externa da pele                                                                                   |
| **AK**                        | _Actinic Keratosis_ — Queratose Actínica: lesão pré-cancerosa da pele causada por exposição crônica ao sol. É considerada o estágio precursor do cSCC                                                                                                           |
| **Gene hub**                  | Gene altamente conectado dentro de uma rede biológica — funciona como um "nó central" que se comunica com muitos outros genes. Genes hub tendem a ser mais importantes para o funcionamento (ou mau funcionamento) do sistema                                   |
| **WGCNA**                     | _Weighted Gene Co-expression Network Analysis_ — Análise de Rede de Co-expressão Gênica Ponderada: método que constrói uma rede de genes onde a "força" da conexão entre dois genes é proporcional ao quanto suas expressões se correlacionam entre as amostras |
| **Módulo**                    | Grupo de genes altamente co-expressos entre si (conectados com alta correlação na rede). Cada módulo tende a representar um processo biológico específico                                                                                                       |
| **GEO**                       | _Gene Expression Omnibus_: banco de dados público do NCBI onde pesquisadores depositam seus dados de expressão gênica para que outros possam reutilizá-los                                                                                                      |
| **DEG**                       | _Differentially Expressed Gene_ — Gene diferencialmente expresso: gene que está significativamente mais ativo ou menos ativo em células cancerosas comparado a células normais                                                                                  |
| **GO**                        | _Gene Ontology_: sistema de classificação que descreve as funções dos genes em três categorias: processo biológico, função molecular e componente celular                                                                                                       |
| **KEGG**                      | _Kyoto Encyclopedia of Genes and Genomes_: banco de dados de vias moleculares (rotas de reações químicas e sinalizações dentro da célula). Permite descobrir em qual "circuito" celular um gene está envolvido                                                  |
| **TCGA**                      | _The Cancer Genome Atlas_: projeto que sequenciou o genoma de amostras de 33 tipos de câncer de milhares de pacientes — um dos maiores bancos de dados genômicos de câncer                                                                                      |
| **log2FC**                    | _log2 Fold Change_: medida de quanto a expressão de um gene mudou. Um valor de 1 significa que o gene está 2× mais expresso; 2 significa 4× mais expresso. Valores negativos indicam redução de expressão                                                       |
| **FDR**                       | _False Discovery Rate_: correção estatística aplicada quando se testam milhares de genes simultaneamente, para reduzir o número de falsos positivos                                                                                                             |
| **ME**                        | _Module Eigengene_: resumo matemático do comportamento de expressão de todos os genes de um módulo — funciona como um "representante único" do módulo para análises de correlação                                                                               |
| **Escala livre (scale-free)** | Propriedade de redes biológicas em que poucos nós têm muitas conexões (hubs) e muitos nós têm poucas conexões — segue uma distribuição em lei de potência                                                                                                       |

---

## Problema Investigado

O Carcinoma Espinocelular Cutâneo (cSCC) é o segundo câncer de pele mais comum e pode se espalhar para outros órgãos (metástase) em ~10% dos casos. Não existem biomarcadores clínicos confiáveis para diagnosticar e tratar o cSCC precocemente. Os autores queriam identificar genes-chave (hubs) envolvidos no desenvolvimento do cSCC e da queratose actínica (AK), sua lesão precursora.

---

## Dados Utilizados

Todos os dados foram obtidos do banco público **GEO**:

| Dataset   | Amostras de cSCC | Amostras de AK | Amostras normais | Descrição                                                            |
| --------- | ---------------- | -------------- | ---------------- | -------------------------------------------------------------------- |
| GSE45216  | 30               | 10             | —                | Microarray de pele (cSCC e AK); plataforma Affymetrix HG-U133 Plus 2 |
| GSE98774  | —                | 28             | 36               | Microarray de AK vs. pele normal; plataforma Affymetrix HG-U133A 2.0 |
| GSE108008 | 10               | 10             | 10               | RNA-seq de cSCC, AK e pele normal pareada do mesmo paciente          |

Os datasets GSE45216 e GSE98774 foram combinados num único dataset (GSE45216–98774) para aumentar o poder estatístico. Isso foi possível porque ambos usam a mesma tecnologia (microarray Affymetrix HG-U133), tornando os valores de expressão diretamente comparáveis. GSE108008, por ser RNA-seq, produz valores em escala e distribuição completamente distintas do microarray — combiná-lo com os outros introduziria ruído técnico que mascararia o sinal biológico, mesmo com correção de batch. Por isso o WGCNA foi rodado separadamente para GSE108008, e os resultados foram comparados ao final para identificar genes consistentes em ambas as análises.

---

## O Que Foi Feito

### 1. Construção da Rede de Co-expressão (WGCNA)

Para cada par de genes, calculou-se a correlação entre seus níveis de expressão em todas as amostras. Quanto mais dois genes "se comportam juntos" (sobem e descem juntos entre os pacientes), mais forte é a aresta entre eles na rede.

Os pesos das arestas foram definidos como |r|^β — a correlação elevada à potência β — de forma que a distribuição de graus da rede se aproxime de uma lei de potência (propriedade **scale-free**, comum em redes biológicas reais). O valor de β foi escolhido como o menor inteiro para o qual R² ≥ 0.8 no ajuste linear entre log(grau) e log(frequência do grau), resultando em β = 5 para o dataset combinado e β = 6 para GSE108008.

Vale notar que redes biológicas reais (como redes de interação proteína-proteína medidas em laboratório) já são naturalmente scale-free. A rede do WGCNA, porém, é construída artificialmente a partir de correlações — e correlações brutas produzem uma distribuição de graus aproximadamente normal, não uma lei de potência. O β é portanto um artifício para forçar a rede construída a se comportar como uma rede biológica real. Embora o WGCNA teste por convenção apenas valores inteiros de β, isso é uma escolha de implementação: valores não-inteiros são matematicamente válidos, mas raramente necessários na prática, pois o critério R² ≥ 0.8 costuma ser atingido em algum inteiro pequeno.

### 2. Identificação de Módulos

O algoritmo agrupou os genes em módulos. Foram encontrados:

- **26 módulos** no dataset GSE45216–98774
- **12 módulos** no dataset GSE108008

Cada módulo recebeu uma cor como identificador (MEblue, MEred, MEcyan, etc.).

### 3. Correlação dos Módulos com Características Clínicas

Para cada módulo, calculou-se a correlação entre seu ME (representante do módulo) e as características das amostras: cSCC, AK ou normal.

- **Módulo 5** foi o mais correlacionado com cSCC (1.742 genes)
- **Módulo 23** foi o mais correlacionado com AK (31 genes)

### 4. Enriquecimento Funcional (GO e KEGG)

Os genes do módulo 5 (relevante para cSCC) foram associados a funções como:

- Colágeno e matriz extracelular (estrutura de suporte dos tecidos)
- Via de sinalização TNF (inflamação)
- Interação citocina-citocina (comunicação entre células imunes)
- Adesão focal (como as células se prendem aos tecidos)

### 5. Identificação dos Genes Hub

Genes presentes no módulo mais relevante **e** significativamente diferencialmente expressos (DEGs) foram candidatos a hub. Genes hub foram definidos como aqueles com alta "pertinência ao módulo" (correlação > 0,8 com o ME). Apenas os genes hub encontrados nos **dois datasets** foram considerados validados.

### 6. Validação em Pan-câncer

Os 7 genes hub validados foram testados em 33 tipos de câncer usando dados do **TCGA**, verificando se sua expressão se correlaciona com sobrevida dos pacientes.

---

## Estratégia de Grafo Utilizada

**Detecção de módulos por co-expressão ponderada (WGCNA) + identificação de hubs**

```
Expressão gênica (amostras de cSCC, AK e normal)
                    ↓
        Rede de co-expressão ponderada (WGCNA)
        (aresta = correlação de expressão entre genes)
                    ↓
        Agrupamento hierárquico → Módulos (comunidades)
                    ↓
        Correlação módulo × característica clínica
        (qual módulo representa melhor o cSCC?)
                    ↓
        Módulo 5 (mais relevante para cSCC)
                    ↓
        Interseção: genes do módulo 5 ∩ DEGs
                    ↓
        Genes hub (alta pertinência ao módulo, MM > 0,8)
        validados nos dois datasets
                    ↓
        7 genes hub identificados
```

![Figura 1 do artigo — fluxograma completo do processo de análise](zhang2021-hub-genes-cscc.pdf)

---

## Resultados

Os **7 genes hub** validados para cSCC foram:

| Gene         | O que se sabe sobre ele                                                               |
| ------------ | ------------------------------------------------------------------------------------- |
| **GATM**     | Envolvido no metabolismo de aminoácidos                                               |
| **ARHGEF26** | Regula a forma e movimento das células                                                |
| **PTHLH**    | Relacionado ao crescimento celular e diferenciação                                    |
| **MMP1**     | Enzima que degrada colágeno — importante na invasão tumoral                           |
| **POU2F3**   | Fator de transcrição (controla a ativação de outros genes)                            |
| **MMP10**    | Outra enzima de degradação de matriz — também ligada à invasão                        |
| **GATA3**    | Fator de transcrição; o único dos 7 associado à sobrevida especificamente em melanoma |

Todos os 7 genes tiveram expressão significativamente diferente entre tecido normal e cSCC, e cada um foi associado à sobrevida em pelo menos algum tipo de câncer no pan-câncer TCGA.

---

## Por Que Este Artigo É Relevante para o Nosso Projeto

Nosso projeto analisa câncer de pele não-melanoma (que inclui cSCC) usando exatamente os datasets do GEO **GSE45216** e **GSE53462** — o mesmo tipo de dado usado neste artigo. A metodologia de WGCNA para encontrar módulos e genes hub em cSCC é diretamente comparável à nossa abordagem com Cytoscape/MCODE, e os genes hub identificados (especialmente MMP1, MMP10) são candidatos naturais a aparecerem como nós centrais nas nossas redes de interação proteica via STRING.

---

## Referência

Chen, H., Yang, J. & Wu, W. (2021). Seven key hub genes identified by gene co-expression network in cutaneous squamous cell carcinoma. _BMC Cancer_, 21, 852. https://doi.org/10.1186/s12885-021-08604-y

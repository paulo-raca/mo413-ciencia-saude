# Redes Complexas (Complex Networks)

[slides](slides.pdf) | [YouTube](https://www.youtube.com/watch?v=sIK1K8-pguI)

Aula de 11/03/2026 — Paula D. Paro Costa & André Santanchè (UNICAMP)

---

## Introdução e Motivação

Redes complexas surgem da necessidade de modelar sistemas do mundo real que não são puramente regulares nem puramente aleatórios. A arquitetura de redes encontradas em domínios tão distintos quanto biologia, tecnologia e ciências sociais apresenta similaridades surpreendentes — o que motivou o surgimento de uma **ciência de redes** (Network Science) como paradigma unificador.

Exemplos de sistemas modelados como redes:

- Redes de interação proteína-proteína (PPI)
- Internet e World Wide Web
- Redes sociais e de colaboração científica
- Redes de interação gene-gene
- Redes neurais biológicas
- Redes de co-autoria, atores de cinema, etc.

---

## Conceitos Fundamentais de Grafos

Uma rede é representada como um **grafo** G = (V, E), onde:

- **V** = conjunto de vértices (nós)
- **E** = conjunto de arestas (links/conexões)

### Grau (Degree)

- **K_i**: grau do nó i — número de links que ele possui com outros nós
- Exemplo em grafo de 4 nós (a, b, c, d): K_a = 3, K_b = 2, K_c = 2, K_d = 3

### Distribuição de Grau

- **P(k)**: probabilidade de um nó escolhido aleatoriamente ter grau k
- **N_k**: número de nós com grau k
- Distribuição normalizada: **P(k) = N_k / N**
- A forma da distribuição de grau é uma das propriedades mais informativas da rede

### Distância Média

Média das distâncias geodésicas (menor caminho) entre todos os pares de vértices:

```
l = 1 / [N(N-1)] * sum(d_ij), para i != j
```

### Coeficiente de Clustering Local

Mede a fração dos vizinhos de um nó que estão conectados entre si:

```
C_i = 2*e_i / [k_i * (k_i - 1)]
```

onde e_i é o número de arestas entre os k_i vizinhos do nó i. Valores: C_i = 1 (totalmente conectados), C_i = 0 (nenhuma conexão entre vizinhos).

### Coeficiente de Clustering Médio

```
<C> = (1/N) * sum(C_i)
```

### Coeficiente de Clustering Global

Razão entre triângulos e todos os triplos conectados na rede:

```
C_delta = 3 * N_delta / N_3
```

Exemplo (Barabási, 2016): para uma rede simples, <C> ≈ 0.310 e C_delta = 0.375.

---

## Lattices, Redes Aleatórias e Redes Complexas

### Lattices (Redes Regulares)

- Topologia regular, grau fixo para todos os nós
- Exemplos na natureza: grafeno (2D), nanotubos, fulerenos, zeólitas grafíticas
- Alto coeficiente de clustering, mas distância média alta

### Redes Aleatórias (Modelo de Erdos-Renyi)

- Estudadas por Erdos (~1960)
- Construção: N nós, cada par conectado com probabilidade p
- Distribuição de grau **binomial** (previsível, com pico em torno do grau médio)
- Assume número fixo de nós e parceiros de interação aleatórios
- Limitação: não reproduz características de redes reais

### O Espectro Lattice-Aleatória

Redes reais situam-se **entre** os dois extremos. A questão central: as redes reais (como a PPI de levedura) são aleatórias? A resposta é **não** — elas exibem estrutura não-trivial.

---

## Propriedade Scale-Free (Livre de Escala)

### Definição

"Uma rede scale-free é uma rede cuja distribuição de grau segue uma lei de potência." (Barabási, 2016)

```
P(k) ~ k^(-gamma)
```

Em escala log-log, a distribuição aparece como uma reta com inclinação -gamma.

### Evidências Empíricas

- **Rede PPI de Levedura** (Jeong et al., 2001): 1.870 proteínas, 2.240 interações — distribuição de grau com cauda longa, típica de lei de potência
- **Internet**: distribuição de grau segue lei de potência tanto para grau de entrada (gamma_in) quanto de saída (gamma_out) da WWW
- **Outras redes**: colaboração de atores de cinema, co-autoria de físicos, co-autoria em neurociências — todas exibem lei de potência (Barabási & Albert, 2012)
- **Contraste com versão aleatória**: a rede PPI aleatorizada apresenta distribuição binomial (com pico), completamente diferente da original

### Hubs

Nas redes scale-free, existem poucos nós com grau muito alto chamados **hubs**. Esses nós dominam a estrutura da rede. Na Internet, por exemplo, hubs são nós com centenas ou milhares de conexões, visíveis como estrelas na visualização.

---

## Modelo de Barabási-Albert (BA)

### Mecanismo

O modelo BA (1999) gera redes scale-free combinando dois princípios:

1. **Crescimento contínuo**: a rede cresce — novos nós são adicionados continuamente (como na Internet, redes de citações, redes de atores, redes de proteínas)
2. **Preferential attachment (conexão preferencial)**: novos nós preferem se conectar a nós que já possuem mais conexões ("os ricos ficam mais ricos")

### Contraste com Redes Aleatórias

| Redes Aleatórias                    | Redes Reais                                                     |
| ----------------------------------- | --------------------------------------------------------------- |
| Número fixo de nós                  | Número de nós cresce continuamente                              |
| Parceiros escolhidos aleatoriamente | Preferential attachment: novos nós preferem nós mais conectados |

---

## Redes Small-World (Pequeno Mundo)

### A Hipótese dos Seis Graus de Separação

- Descrita pelo escritor Frigyes Karinthy (1929): todo par de pessoas no mundo está a no máximo 6 passos de distância
- Testada experimentalmente por **Stanley Milgram** (1967): experimento de cartas encaminhadas, média de ~5-6 intermediários (N=64 cadeias)
- Resultado moderno (Backstrom et al., 2012, dados do Facebook): a distância média caiu para **~4 graus** de separação ("Four degrees of separation")

### Formalização (Watts & Strogatz, 1998)

O modelo Watts-Strogatz descreve a transição de uma lattice regular para uma rede aleatória, passando por uma região **small-world** intermediária:

- **Lattice (p=0)**: alto clustering, alta distância média
- **Small-world (p intermediário)**: alto clustering, baixa distância média
- **Aleatória (p=1)**: baixo clustering, baixa distância média

O insight chave: adicionar um pequeno número de conexões de longo alcance a uma lattice reduz drasticamente a distância média sem destruir o clustering local.

### Propriedades da Rede PPI de Levedura (Exemplo Concreto)

| Versão       | Coef. Clustering Local | Distância Média |
| ------------ | ---------------------- | --------------- |
| Original     | 0.133                  | 4.279           |
| Aleatorizada | 0.001                  | 5.346           |

A rede original tem clustering muito maior e distância média menor — assinatura de rede small-world.

---

## Robustez e Vulnerabilidade

### Robustez a Falhas Aleatórias

Redes com lei de potência (scale-free) são **robustas a falhas aleatórias**: remover nós aleatórios tem pouco impacto na conectividade da rede, pois a probabilidade de atingir um hub é baixa.

### Vulnerabilidade a Ataques Direcionados

O mesmo tipo de rede é **especialmente vulnerável a ataques direcionados**: remover os hubs (nós de alto grau) desintegra rapidamente a rede. Isso tem implicações diretas para:

- Estratégias antivirais (bloquear proteínas hub)
- Segurança de infraestrutura (Internet, redes elétricas)
- Epidemiologia (vacinação direcionada)

---

## Predição de Links (Link Prediction)

### Problema

Dada a estrutura atual de uma rede, qual será o próximo link mais provável? (Quem você vai se relacionar?)

### Abordagens

- **Network Agnostic**: usa atributos dos nós sem considerar a topologia da rede
- **Network Aware**: usa a estrutura da rede para predizer novos links — considera vizinhança comum, centralidade, etc.

### Aplicações

- Sistemas de recomendação (sugestão de amigos em redes sociais)
- Descoberta de interações proteína-proteína desconhecidas
- Segurança (detecção de ligações suspeitas)

---

## Ciência de Redes (Network Science)

### Definição de Rede Complexa

Uma rede complexa é:

- Um grafo com **características topológicas não-triviais**
- Similar às redes do "mundo real": nem puramente regular, nem puramente aleatória
- Apresenta propriedade **scale-free** e/ou características **small-world**
- A arquitetura de redes em domínios distintos é **mais similar entre si do que se esperaria**

### Network Science como Paradigma

A ciência de redes propõe a **generalização de modelos e reuso de soluções** — convergência de vários domínios para um paradigma comum. Essa convergência ocorre em três níveis:

1. **Abstração do problema**: mesmo formalismo (grafo) para sociologia (crescimento populacional, redes sociais), biologia (redes alimentares, vulnerabilidade de espécies) e web science (reputação de sites, fenômenos virais)
2. **Abordagens**: predição de links, espalhamento/difusão (epidemias, notícias), robustez (comportamento quando nós são removidos)
3. **Medidas**: coeficiente de clustering, centralidade de nó, influência de nó, modularidade

---

## Medidas de Rede Importantes

| Medida                    | Descrição                              |
| ------------------------- | -------------------------------------- |
| Grau (degree)             | Número de conexões de um nó            |
| Distribuição de grau P(k) | Probabilidade de um nó ter grau k      |
| Distância média           | Média dos menores caminhos entre pares |
| Coeficiente de clustering | Fração dos vizinhos interconectados    |
| Centralidade de nó        | Importância do nó na rede              |
| Influência de nó          | Acessibilidade, força esperada         |
| Modularidade              | Presença de comunidades/módulos        |

---

## Aplicações em Saúde e Biologia

### Redes de Interação Proteína-Proteína (PPI)

- Rede PPI de levedura (Jeong et al., 2001): 1.870 proteínas, 2.240 interações — escala livre
- **Lethality and centrality**: proteínas essenciais tendem a ser hubs — remover um hub tem consequência letal
- Percentual de proteínas essenciais aumenta com o número de links do nó

### Interações Vírus-Hospedeiro

- Estudar interações proteicas vírus-hospedeiro requer conhecimento de arquiteturas proteicas, mecanismos evolutivos e dados biológicos (Brito & Pinney, 2017)
- Do ponto de vista biomédico, **bloquear tais interações** é o principal mecanismo de terapias antivirais
- Representação: TNF e seu receptor (Wiltgen et al., 2007)

### Redes de Interação Gênica

- Rede de interações de genes em levedura: distribuição de grau em cauda longa (scale-free)
- Contraste com versão aleatorizada: distribuição binomial

### Redes Cerebrais e Complexidade Emergente

- O cérebro humano: ~85 bilhões de neurônios, ~10.000 sinapses cada, ~1 quadrilhão de conexões
- Poder computacional estimado: 6,4 × 10^18 inst/s (equivalente a todos os computadores do mundo em 2007)
- A complexidade cerebral é **emergente**: surge de regras simples (criar conexões e reforçar as mais usadas)
- Simulação em 2013: 82.944 processadores, 40 min para simular 1 segundo do cérebro biológico (com apenas 1,73 bi neurônios)

### Modelagem Epidemiológica com Redes

- Aplicação prática: predição de risco de contaminação por COVID-19 em Salvador/BA (2020)
- Abordagem: regressão usando densidade populacional como variável preditora
- Li et al. (2018): correlação positiva entre densidade populacional e taxa anual de mortalidade por influenza
- Limitações do modelo: outras variáveis relevantes (IDH, etc.), não generalizável automaticamente

---

## Resumo das Propriedades Distintivas

| Propriedade                       | Lattice             | Aleatória        | Scale-Free      | Small-World |
| --------------------------------- | ------------------- | ---------------- | --------------- | ----------- |
| Distribuição de grau              | Delta (todos igual) | Binomial/Poisson | Lei de potência | Variada     |
| Hubs                              | Nao                 | Nao              | Sim             | Possivel    |
| Clustering                        | Alto                | Baixo            | Baixo-médio     | Alto        |
| Distância média                   | Alta                | Baixa            | Baixa           | Baixa       |
| Robustez a falha aleatória        | Média               | Média            | Alta            | Alta        |
| Vulnerabilidade a ataque nos hubs | N/A                 | N/A              | Alta            | Alta        |

---

## Referências Principais

- Barabási, A.-L. (2016). _Network Science_. Cambridge University Press.
- Barabási, A.-L., & Albert, R. (1999). Emergence of scaling in random networks. _Science_, 286, 509–512.
- Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of 'small-world' networks. _Nature_, 393, 440–442.
- Jeong, H. et al. (2001). Lethality and centrality in protein networks. _Nature_, 411, 41–42.
- Milgram, S. (1967). The small world problem. _Psychology Today_, 2(1), 60–67.
- Backstrom, L. et al. (2012). Four degrees of separation. _WebSci'12_, 33–42.
- Brito, A. F., & Pinney, J. W. (2017). Protein–Protein Interactions in Virus–Host Systems. _Frontiers in Microbiology_, 8, 1557.
- Vulliard, L., & Menche, J. (2021). Complex Networks in Health and Disease. _Systems Medicine_, 26–33.

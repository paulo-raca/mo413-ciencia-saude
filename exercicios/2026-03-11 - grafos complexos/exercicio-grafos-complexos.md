# The Eight Cities

## Block transit

- An infectious disease started to spread in one city.
- You want to reduce the spreading while looking for a cure.
- The transit among cities is exclusively by roads.
- You have a task force apt to block the transit passing by only one city.
- What is the best city to block?

> D -- Pois divide o grafo totalmente em 5 + 2 cidades. Todas as demais opções bloqueiam 6+1 cidades ou não separam.
> Sem saber de onde a doença vem, D minimiza o pior caso (5 cidades contaminadas)

## Deliver Medication

- You want to deliver medication as fast as possible to all cities
- You will choose one city to land your spaceship
  - The other you must achieve by road
  - You have seven trucks on your ship to deliver medications
- What is the best city to land?

> E -- Está a no máximo a 2 estradas de distancia de qualquer outra cidade, e a distancia média é menor que C.

# Me and My Seven Friends

- There are two communities in which I participate: university and climbing.
- Which are the communities, and who am I?

> D, pois conecta 2 grupos de nós (universide e escalada).
> B e E também separam, mas uma delas mas vira uma comunidade de apenas 2 pessoas eu+1 pessoa)
> Isso assume que é a única pessoa da universide que faz escalada.

# Zombie

Compute Betweenness and Closeness centralities of this network: https://github.com/datasci4health/datasci4health.github.io/tree/master/networks/zombie/pathways

![Closeness Centrality](zombie-closeness-centrality.png)
![Betweenness Centrality](zombie-betweenness-centrality.png)

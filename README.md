Rota Otimizada com o Algoritmo do Caixeiro Viajante (API)
Este projeto implementa uma API que calcula a rota otimizada entre um conjunto de coordenadas geográficas utilizando o algoritmo do Caixeiro Viajante. A API recebe coordenadas de locais, calcula a rota mais curta e retorna a rota otimizada e a distância total.

Tecnologias Utilizadas
Python 3.x: Linguagem utilizada para o desenvolvimento da API.

Flask: Framework utilizado para criar a API.

Geopy: Biblioteca para cálculos de distância geográfica.

Funcionalidade
A API expõe um endpoint onde você pode enviar um conjunto de coordenadas geográficas (latitude, longitude). Ela utiliza o algoritmo do Caixeiro Viajante para calcular a rota mais otimizada, ou seja, a sequência de coordenadas que minimiza a distância total percorrida.

O que a API faz:
Recebe uma lista de coordenadas no formato JSON.

Calcula a distância total percorrida se as coordenadas forem visitadas na ordem em que são fornecidas (sem otimização).

Aplica o algoritmo do Caixeiro Viajante para encontrar a sequência de coordenadas que resulta na menor distância total.

Retorna a rota otimizada e as distâncias totais (tanto otimizada quanto sem otimização).

Endpoints
POST /calcular_rota
Este endpoint recebe um conjunto de coordenadas e retorna a rota otimizada.

Requisição
A requisição deve ser feita com um JSON contendo um array de coordenadas, com o formato:

json
{
  "coordenadas": [
    [latitude1, longitude1],
    [latitude2, longitude2],
    ...
  ]
}

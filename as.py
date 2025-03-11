from geopy.distance import geodesic

#(latitude, longitude)
coordenadas = [
    (-26.176944, -50.390833),
    (-26.177500, -50.391111),
    (-26.177222, -50.391944),
    (-26.200000, -50.450000),
    (-26.185000, -50.400000),
    (-26.250000, -50.366667),
    (-26.210000, -50.420000),
    (-26.170000, -50.380000),
    (-26.190000, -50.410000),
    (-26.220000, -50.430000)
]

def calcular_distancia(p1, p2):
    return geodesic(p1, p2).kilometers

def encontrar_rota_vizinho_mais_proximo(pontos):
    n = len(pontos)
    nao_visitados = set(range(1, n))
    rota = [0]

    while nao_visitados:
        ultimo_ponto = rota[-1]
        proximo_ponto = min(nao_visitados, key=lambda i: calcular_distancia(pontos[ultimo_ponto], pontos[i]))
        rota.append(proximo_ponto)
        nao_visitados.remove(proximo_ponto)

    rota.append(0)
    distancia_total = sum(calcular_distancia(pontos[rota[i]], pontos[rota[i+1]]) for i in range(n))

    return [pontos[i] for i in rota], distancia_total

distancia_sem_otimizacao = sum(calcular_distancia(coordenadas[i], coordenadas[i+1]) for i in range(len(coordenadas)-1))
distancia_sem_otimizacao += calcular_distancia(coordenadas[-1], coordenadas[0])

rota_otimizada, distancia = encontrar_rota_vizinho_mais_proximo(coordenadas)

base_url = "https://www.google.com.br/maps/dir/"
rota_str = "/".join(f"{lat},{lon}" for lat, lon in rota_otimizada)
mapa_link = base_url + rota_str


print("Rota sem otimização (latitude, longitude):", coordenadas)
print("Distância total sem otimização (km):", round(distancia_sem_otimizacao, 2))
print("Rota otimizada (latitude, longitude):", rota_otimizada)
print("Distância total otimizada (km):", round(distancia, 2))
print("Link do Google Maps:", mapa_link)

# Classes de exemplo para os veículos utilizando polimorfismo
class Carro:
    def __init__(self, consumo_km_litro, preco_combustivel):
        self.consumo_km_litro = consumo_km_litro
        self.preco_combustivel = preco_combustivel

    def calcular_custo_viagem(self, distancia):
        litros_necessarios = distancia / self.consumo_km_litro
        return litros_necessarios * self.preco_combustivel

class Moto:
    def __init__(self, custo_por_km):
        self.custo_por_km = custo_por_km

    def calcular_custo_viagem(self, distancia):
        return distancia * self.custo_por_km


# FUNÇÃO SOLICITADA NA QUESTÃO
def calcular_custo_total_viagem(lista_veiculos):
    DISTANCIA_VIAGEM = 200  # Distância fixa de 200 km definida no enunciado
    custo_total = 0.0
    
    for veiculo in lista_veiculos:
        # O método 'calcular_custo_viagem' é chamado dinamicamente para cada tipo de veículo
        custo_total += veiculo.calcular_custo_viagem(DISTANCIA_VIAGEM)
        
    return custo_total


# Exemplo de uso (opcional para teste):
# veiculos = [Carro(consumo_km_litro=10, preco_combustivel=5.50), Moto(custo_por_km=0.30)]
# print(calcular_custo_total_viagem(veiculos))

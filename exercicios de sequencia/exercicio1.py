#Mário pretende realizar uma viagem utilizando um veículo cujo consumo médio de combustível é de 10 Km/L.
#Sabendo que percorrerá 300 000 m, é correto afirmar que o volume de combustível a ser consumido será de:
metros = int(input())
gasto = 10
quilometros = metros / 1000
litros = quilometros / gasto
print(f'Será consumido {litros} litros de gasolina')
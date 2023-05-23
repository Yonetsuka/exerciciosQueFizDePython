notas = []

while True:
    try:
        n = float(input("Informe a nota: "))
        if n < 0:
            break
        notas.append(n)
    except ValueError:
        print("A nota informada está em formato inválido")
print(notas)

print(f'Quantidade de notas {len(notas)}')

#Media das notas

soma = 0
for item in notas:
    soma += item
media = soma / len(notas)
print(f'Média das notas: {media}')

print("Notas acima da media calculada: ")
for item in notas:
    if item > media:
        print(item)
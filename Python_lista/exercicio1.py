pares = []
impares = []
cont = 0

while cont < 10:
    try:
        numero = int(input("Numero: "))
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
        cont += 1
    except ValueError:
        print("Erro.O numero digitado deve ser inteiro")

print(f"Lista pares: {pares}")
print(f"Lista impares: {impares}")
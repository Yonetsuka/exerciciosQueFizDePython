def buscar(lista,numero):
    cont = 0
    for item in lista:
        if item == numero:
            cont += 1
    return cont

lista = []
while len(lista) < 10:
    try:
        numero = int(input("Numero: "))
        lista.append(numero)
    except ValueError:
        print("Erro: o numero digitado deve ser inteiro")
print(lista)

numero = int(input("Informe um numero para buscar na lista"))
print(f'Quantidade de vezes que {numero} aparece na tela {buscar(lista,numero)}')
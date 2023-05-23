#Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
#a.Amédia aritmética dos números armazenadosna lista.
#b.O somatório dos números pares armazenados na lista.

def preenche_lista():
    lista = []
    cont = 0

    while cont < 10:
        try:
            numero = int(input("Numero: "))
            lista.append(numero)
            cont += 1
        except ValueError:
            print("Erro. O valor digitado deve ser inteiro")
    return(lista)

#fazendo média
def calcular_media(lista):
    soma = 0
    for item in lista:
        soma += item
    media = soma / len(lista)
    return(media)

#O somatório dos numeros pares
def somar_pares(lista):
    soma = 0
    for item in lista:
        if item % 2 == 0:
            soma += item
    return(soma)

lista = preenche_lista()
print(lista)
print(f'Média da lista: {calcular_media(lista)}')
print(f"Somatório dos numeros pares: {somar_pares(lista)}")
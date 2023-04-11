#2.Escreva um algoritmo que solicite 10 números e exiba o dobro de cada número digitado.
contagem = 1
while contagem != 11:
    num = int(input('Digite um número: '))
    dobro = num * 2
    print(f'O dobro desse número é {dobro}')
    contagem += 1
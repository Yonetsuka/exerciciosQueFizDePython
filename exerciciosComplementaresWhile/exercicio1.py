#1.Fazer um algoritmo que exiba na tela todos os números ímpares de 1 a n, 
#onde n é fornecido pelo usuário.
num = int(input('Digite um número para mostrar todos os ímpares até ele: '))
cont = 1
while cont <= num:
    if cont % 2 == 1:
        print(cont)
        cont+=1
    else:
        cont += 1
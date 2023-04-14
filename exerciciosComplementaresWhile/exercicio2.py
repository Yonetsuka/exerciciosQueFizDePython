#2.Fazer um algoritmo que soliciteum número inteiro Nqualquer e exiba a tabuada de N.
num = int(input('Digite um numero para mostrar a sua tabuada: '))
cont = 1;
while cont < 11:
    mult = num * cont
    print(f'{num} * {cont} = {mult}')
    cont += 1
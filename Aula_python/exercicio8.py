#8.Escreva  um  algoritmo  que  solicite  10  números  e  informe  qual  foi  o  
#menor  número digitado.
cont = 0
menor = int(input('Digite um numero'))
while cont != 9:
    num = int(input('Digite um numero: '))
    if num < menor:
        menor = num
    cont += 1
print(f'O menor número é {menor}')

#5.Escreva  um  algoritmo  que solicite 15  números  e  informe  o  somatório  de  todos  
#os números ímpares digitados.
contagem = 1
impares = 0
while contagem != 16:
    num = int(input('Digite um número: '))
    if num % 2 == 1:
        impares += num
    contagem += 1
print(f'A soma de todos os úmeros ímpares é {impares}')
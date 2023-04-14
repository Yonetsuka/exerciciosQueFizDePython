#8.Escreva  um  algoritmo  que  solicite  vários  números  inteiros  e  exiba  o  
#resultado  da  multiplicação  de  todos  os números ímpares e o somatório de todos os 
#números pares. O algoritmo deve ser finalizado quando o usuário digitar zero
valido = True
soma = 0
multiplicacao = 1
while valido == True:
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
    if num % 2 == 1:
        multiplicacao *= num
    if num == 0:
        valido = False
print(f' A soma dos número pares são {soma} e a multiplicação dos ímpares são {multiplicacao}')
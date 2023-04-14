#4.Fazer  um  algoritmo  que  leia  um  número  inteiro  positivo,  
#calcule  e  escreva  se  o  número  lido  é  um  número perfeito ou não. 
#Número perfeito é aquele cuja soma de seus divisores, exceto ele próprio, 
#é igual ao próprio número.
num = int(input('Digite um número: '))
divisor = 1
soma_f = 0
while divisor < num:
    soma_i = num % divisor
    if soma_i == 0:
        soma_f += divisor
        divisor += 1
    else:
        divisor += 1
if soma_f == num:
    print('Seu número é perfeito')
else:
    print('Seu número não é perfeito')
#Faça um algoritmo que solicita ao usuário um valor inteiro 
#e exibe uma mensagem informando se o número é par ou ímpar.
num = int(input('Digite um valor inteiro: '))
if num % 2 == 1:
    print(f'O valor {num} é ímpar')
if num % 2 == 0:
    print(f'O valor {num} é par')
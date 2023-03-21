#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
#Dica: utilize o operador módulo (resto da divisão).
num = int(input('Digite um número inteiro: '))
verificador = num % 2
if verificador == 1:
    print('O número inserido é ímpar')
if verificador == 0:
    print('O número inserido é par')
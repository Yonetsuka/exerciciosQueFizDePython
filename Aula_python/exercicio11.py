#11.Escreva um programa que solicita ao usuário o valor de N e calcule o valor de 
#𝑆 na série abaixo:
n = int(input('Digite um número: '))
num = 1
resposta = 0
while num != n:
    resposta += 1 / num
    num += 1
print(f'o resultado da equação deu {resposta}')
#Faça um algoritmo que solicita um número inteiro e exibe uma mensagem indicando se ele é positivo,
# negativo ou zero.
num = int(input('Digite um número inteiro'))
if num < 0:
    print(f'O número {num} é negativo')
elif num > 0:
    print(f'O número {num} é positivo')
elif num == 0:
    print('O número é zero')
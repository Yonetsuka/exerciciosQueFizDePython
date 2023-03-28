#Faça um algoritmo que solicita ao usuário três números e exibe na tela apenas o menor deles,
#ou uma mensagem informando que os números são iguais.
num1 = float(input('Digite um número:'))
num2 = float(input('Digite um segundo número:'))
num3 = float(input('Digite um terceiro número:'))
if num1 < num2 and num1 < num3:
    print(f'O menor número é {num1}')
elif num2 < num1 and num2 < num3:
    print(f'O menor número é {num2}')
elif num3 < num2 and num3 < num1:
    print(f'O menor número é {num3}')
elif num1 == num2 and num1 == num3:
    print(f'Os três números são iguais')
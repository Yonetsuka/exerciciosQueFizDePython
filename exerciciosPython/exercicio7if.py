#Faça um algoritmo que solicite dois números ao usuário e exiba apenas o maior deles. 
#Caso eles sejam iguais exiba a mensagem “Números Iguais”.
num1 = float(input('Digite um número:'))
num2 = float(input('Digite um segundo número'))
if num1 > num2:
    print(f'O número {num1} é maior que {num2}')
elif num1 < num2:
    print(f'O número {num1} é menor que {num2}')
elif num1 == num2:
    print('Os dois números são iguais')
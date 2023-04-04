#Faça um algoritmo que verifica se um número inteiro informado pelo usuário é múltiplo de 3.
num = int(input('Digite um número'))

resto = num % 3

match resto:
    case 0:
        print('É múltiplo de 3')
    case _:
        print('Não é múltiplo de 3')
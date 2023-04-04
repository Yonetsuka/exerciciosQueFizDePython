#Faça um programa que receba um número, digitado pelo usuário e mostre o menu para 
#selecionar o tipo de cálculo que deve ser realizado. Exiba o resultado do cálculo efetuado.
#Opção 1-O dobro Opção 2 -A metadeOpção3 -10% do número 
numero = float(input('Número: '))

print('Opção 1 - o dobro')
print('Opção 2 - A metade')
print('Opção 3 - 10% do número')

opção = int(input('Escolha uma opção: '))

match opção:
    case 1:
        resultado = numero * 2;
        print(f'O dobro de {numero} é {resultado}')
    case 2:
        resultado = numero / 2
        print(f'A metade de {numero} é {resultado}')
    case 3:
        resultado = numero * 0.10
        print(f'10% de {numero} é {resultado}')
    case _:
        print('Opção inválda')
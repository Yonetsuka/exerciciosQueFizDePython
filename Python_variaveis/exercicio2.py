#2.Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos.
# Por exemplo: 120 é triangular, pois 4 * 5 * 6 = 120. 2730 é triangular, 
#pois 13 * 14 * 15 = 2730. Faça uma função que receba um número inteiro e retorne True
#se for um número triangular e False, caso contrário.


def ver(num):
    number1 = 0
    number2 = 1
    number3 = 2
    while number3 != num:
        if number1 + number2 + number3 == num:
            print('O numero é triangular')
        else:
            print('O numero não é triangular')

triangular = int(input('Digite um numero para verificar se é triangular'))
ver(triangular)
#3.Em um jogo de dados, pode ser sorteado qualquer número entre 1 e 6. 
#Faça uma função que simule 1 milhão de lançamentos de dados e mostre quantas vezes cada 
#número foi sorteado.
import random

def girar_dados():
    cont = 0
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    num6 = 0
    while cont < 1000000:
        num = random.randrange(1,6)
        if num == 1:
            num1 += 1
        if num == 2:
            num2 += 1
        if num == 3:
            num3 += 1
        if num == 4:
            num4 += 1
        if num == 5:
            num5 += 1
        if num == 6:
            num6 += 1
        cont += 1
    print(f'Numero 1: {num1}')
    print(f'Numero 2: {num2}')
    print(f'Numero 3: {num3}')
    print(f'Numero 4: {num4}')
    print(f'Numero 5: {num5}')
    print(f'Numero 6: {num6}')

girar_dados()
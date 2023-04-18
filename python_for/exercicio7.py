#7.Escreva  um  algoritmo  que  exiba  20  números  aleatórios  sorteados  entre  1  e  50  
#(Dica:  utilize  a biblioteca random).
import random
for i in range(0,20,1):
    sort = random.randrange(1,50)
    print(f'Número: {sort}')
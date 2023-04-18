#4.Escreva um algoritmo que leia quinze números informados pelo usuário e exiba 
#a raiz quadrada de cada número (Dica: utilize a biblioteca math)
import math
for i in range(0,5,1):
    num = int(input('Digite o número: '))
    res = math.isqrt(num)
    print(f'Sua raíz quadrada é {res}')
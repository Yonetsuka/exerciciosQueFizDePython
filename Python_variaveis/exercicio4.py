#4.Crie uma função chamada bhaskara que receba 3 valores (a, b, c) 
#e calcule as raízes da fórmula de Bhāskara.Faça um teste com bhaskara(1, -4, -5)
#e a função deve exibir as raízes: 5.0e-1.0.
import math

def bhaskara(a, b, c):
    delta = math.sqrt(b ** 2 - 4 * a * c)
    raiz1 = (-b + delta) / 2 * a
    raiz2 = (-b - delta) / 2 * a
    print(f'As raízes são {raiz1} e {raiz2}')

a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))

bhaskara(a, b, c)
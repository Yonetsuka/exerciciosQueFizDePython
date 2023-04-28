#5.Escreva um programa que leia o raio de um círculo e faça duas funções: 
#uma função chamada area que  calcula  e  retorna  a  área  do  círculo  e  outra  função  
#chamada perimetro que  calcula  e  retorna  o perímetro docírculo.Utilize as fórmulas 
#abaixo:
# Área = π * r2
# Perímetro = π * 2 * r

import math

def area(raio):
    area = math.pi * raio ** 2
    print(area)

def perimetro(raio):
    perimetro = math.pi * raio
    print(perimetro)

print('1-Área')
print('2-Perímetro')
opcao = int(input('Escolha uma opção: '))
if opcao == 1:
    raio = int(input('Digite o raio do círculo: '))
    area(raio)
if opcao == 2:
    raio = int(input('Digite o raio do círculo: '))
    perimetro(raio)
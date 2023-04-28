#4.Faça uma função que recebe um número inteiro por parâmetro e retorna True se for par e 
# False se for ímpar.

def VerPar(num):
    if num % 2 == 0:
        print('Par')
    if num % 2 == 1:
        print('Ímpar')
    
var = int(input('Digite para ver se é Ímpar ou Par: '))
VerPar(var)
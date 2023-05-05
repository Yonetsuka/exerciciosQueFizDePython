#5.Faça uma função que recebe um número inteiro e retorna a quantidade de dígitos desse número.
num1 = int(input('Digite um número inteiro: '))

def verQuant(num):
    cond = True
    div = 1
    digito = 0
    while cond == True:
        if num / div > 0:
            div = div * 10
            digito += 1
        if num / div < 0:
            cond = False
    print(f'A quantidade de digitos é {digito}')

verQuant(num1)
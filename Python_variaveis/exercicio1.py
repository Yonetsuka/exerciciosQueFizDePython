#1.Crie uma função que receba três númeroscomo parâmetros,
#e retorne Truese a soma de quaisquer pares de números gera a soma do terceiro número. 
# Caso contrário retorne False.

def func():
    num1 = int(input('Dgite um numero: '))
    num2 = int(input('Digite um numero:'))
    num3 = int(input('Digite um numero:'))

    if num1 + num2 == num3 or num1 + num3 == num2 or num3 + num2 == num1:
        return True
    else:
        return False

func()
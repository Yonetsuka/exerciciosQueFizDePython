def soma(a,b):
    if type(a) == int and type(b) == int:
        c = a + b
        print(f'Resultado da soma: {c}')
    else:
        raise TypeError('Escreva as variáveis certo')

a = 2 
b= 'saffa'

try:
    soma(a,b)
except TypeError as msg:
    print(f'ERRO: {msg}')
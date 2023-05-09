from typing import Type


try:
    x = 5
    y= 8
    z = x + y
except TypeError:
    print("Ocorreu um erro, pois não é possível somar string com int")

try:
    a = int(input('Informe um número: '))
    b = int(input('Informe um número: '))
    c = a / b
    print("Resultado da divisão: ", c)
except ZeroDivisionError:
    print("Não é possível diviir por zero")
except ValueError:
    print('O valor informado não é inteiro')
except Exception:
    print('Um erro inesperado aconteceu')
finally:
    print('Fim do programa')
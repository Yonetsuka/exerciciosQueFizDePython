try:
    a = int(input('Informe um numero: '))
    b = int(input('Informe um numero: '))
    c = a / b
    if a < 0 or b < 0:
        raise TypeError
    print('Resultado da divisão', c)
except ZeroDivisionError:
    print('Não é possível dividr por zero')
except ValueError:
    print('O valor informado não é um número inteiro')
except TypeError:
    print('O número é negativo')
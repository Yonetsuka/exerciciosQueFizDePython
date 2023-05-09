while True:
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair')
    try:
        opção = int(input('Escolha uma opção: '))
    except ValueError:
        print('Digite um numero inteiro entre 1 e 5')
    if opção == 5:
        print('Fim do programa')
        break
    try:
        a = float(input('Primeiro numero: '))
        b = float(input('Segundo número'))
    except ValueError:
        print('Os valores informados não são números')
    else:
        if opção == 1:
            print(f'Soma: {a + b}')
        elif opção == 2:
            print(f'Subtração: {a - b}')
        elif opção == 3:
            print(f'Multiplicação: {a * b}')
        elif opção == 4:
            try:
                print(f'Divisão: {a / b}')
            except ZeroDivisionError:
                print('ERRO: Ocorreu uma divisão por zero')
#Leia a primeira letra do estado civil de uma pessoa e mostre uma mensagem com a sua descrição 
#(Solteiro, Casado, Viúvo, Divorciado). Mostre uma mensagem de erro, se necessário 
#(o algoritmo deve funcionar para letras maiúsculas e minúsculas).
letra = input('Informe seu estado civil(D,C,S,V): ')
match(letra):
    case 'D' | 'd':
        print('Divorciado')
    case 'C' | 'c':
        print('Casado')
    case 'S' | 's':
        print('Solteiro')
    case 'V' | 'v':
        print('Viúvo')
    case _:
        print('Opção inválido')
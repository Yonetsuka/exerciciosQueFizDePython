#Faça  um  algoritmo  que  exiba  um  Menu  com  as  opções  de  um  cardápio  de  restaurante.
# O  cliente  deve  escolher o código do prato desejado e na sequência, 
#informar se aceita pagar a gorjeta do garçom. Se o usuário aceitar, mostrar o valor final 
#(valor do prato + 10%), caso contrário, mostrar somente o valor do prato.

print('1 Picanha  25 reais')
print('2 Lasanha  20 reais')
print('3 Strogonoff  20 reais')
print('4 Bife acebolado  15 reais')
print('5 Pão com ovo  5 reais')

opcao = int(input('Escolha o prato desejado'))

match opcao:
    case 1:
        valor = 25.0
    case 2:
        valor =20.0
    case 3:
        valor = 20.0
    case 4:
        valor = 15.0
    case 5:
        valor = 5.0
    case _:
        print('Opção inválida')
        valor = 0

gorjeta = input('Você deseja pagar os 10%(sim/nao): ')
match gorjeta:
    case 'sim':
        valor = valor + valor * 10 / 100
        print(f'Valor total: {valor}')
    case 'nao':
        print(f'Valor total: {valor}')
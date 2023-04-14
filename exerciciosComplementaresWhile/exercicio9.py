#Faça um algoritmo que apresente um menu com as opções abaixo.
# Considere que osaldo deve iniciar em R$ 0,00 e acada saque ou depósito o valor do 
# saldo deve ser atualizado. Após cada operação realizada, 
#o menu deve ser exibido novamente, 
#e o programa deve ser finalizado apenas quando o usuário selecionar 
#a opção 4.
# 1-Consulta Saldo 
# 2-Realizar Saque 
# 3-Realizar Depósito 
# 4–Sair
# Escolha uma opção: 
saldo = 0
valido = True
while valido == True:
    print('1-Consultar Saldo')
    print('2-Realizar Saque')
    print('3-Realizar Depósito')
    print('4-Sair')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        print(f'Você tem {saldo}')
    if opcao == 2:
        saldo -= int(input('Digite quanto você vai sacar: '))
    if opcao == 3:
        saldo += int(input('Digite quanto você irá depositar: '))
    if opcao == 4:
        valido == False
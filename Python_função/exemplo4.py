def exibirMensagem():
    print('Olá')


def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    print(area)


def par_ou_impar(numero):
    if numero % 2 == 0:
        print('Par')
    if numero % 2 == 1:
        print('Impar')


exibirMensagem()  # chamada da função
while True:
    print('1 - Exibir uma mensagem')
    print('2 - Verificar se número é par ou ímpar')
    print('3 - Calcula área do triângulo')
    print('4 - Finalizar')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        exibirMensagem()
    elif opcao == 2:
        numero = int(input('Informe um número: '))
        par_ou_impar(numero)
    elif opcao == 3:
        base = float(input('Digite a base do triangulo: '))
        altura = float(input('Digite a altura do triângulo: '))
        calcular_area_triangulo(base, altura)
    elif opcao == 4:
        print('Fim da execução')
        break

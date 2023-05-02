#8.Faça  um  programa  para  uma  calculadora  simples  com  as  seguintes  operações:  
#adição,  subtração, multiplicação e divisão. 
#O programa começa apresentando ao usuário um menu de opções semelhante ao mostrado abaixo:
#Calculadora: 
#1 -Adição
#2 -Subtração
#3 -Multiplicação
#4 -Divisão
#5 -Sair do programa
#Selecione sua opção:
#Crie  uma  função  chamada Menu,  
#que  exiba  o  menu  acima  e  retorna  a  opção  do  usuário  para  o programa  principal. 
#Se  a  opção  for  inválida,  informe  ao  usuário  e  peça  a  ele  para  entrar  com  uma 
#opção válida.
#De   acordo   com  a   opção   do   usuário,   chame   uma   das   seguintes   funções: 
#adicao,   subtracao, multiplicacao, divisao, 
#passando como parâmetros dois números também informados pelo usuário.Após a execução da operação
#o programa volta a apresentar omenu inicial até que o usuário encerre o programa com a opção 5.
continuar = True

def menu(opção):
    if opção == 1:
        adicao()
    if opção == 2:
        subtracao()
    if opção == 3:
        multiplicacao()
    if opção == 4:
        divisao()
    if opção == 5:
        sair()

def adicao():
        num1 = int(input('Digite o primeiro numero: '))
        num2 = int(input('Digite o segundo numero: '))
        soma = num1 + num2
        print(f'Sua soma é {soma}')

def subtracao():
        num1 = int(input('Digite o primeiro numero: '))
        num2 = int(input('Digite o segundo numero: '))
        subtracao = num1 - num2
        print(f'Sua subtração é {subtracao}')

def multiplicacao():
        num1 = int(input('Digite o primeiro numero: '))
        num2 = int(input('Digite o segundo numero: '))
        multiplicacao = num1 * num2
        print(f'Sua soma é {multiplicacao}')

def divisao():
        num1 = int(input('Digite o primeiro numero: '))
        num2 = int(input('Digite o segundo numero: '))
        divisao = num1 / num2
        print(f'Sua soma é {divisao}')
def sair():
        print('Adeus')

while continuar == True:
    print('Calculadora: ')
    print('1 -Adição')
    print('2 -Subtração')
    print('3 -Multipplicação ')
    print('4 -Divisão')
    print('5 -Sair do programa')
    opção = int(input('Selecione sua opção: '))
    menu(opção)
    if opção == 5:
        break
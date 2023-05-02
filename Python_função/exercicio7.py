#7.Escreva um programa que solicita um valor inteiro ao usuário e exibe a tabuada desse número. 
#Você deverá escrever as seguintes funções:-ler_numero(): Solicita um número inteiro e 
#retorna esse número para o programa principal.-tabuada(n): Recebe como parâmetro um número 
#inteiro e exibe na tela a tabuada desse número.

def ler_numero():
    n = int(input('Digite um numero para saber a sua tabuada: '))
    return(n)

def tabuada(n):
    cont = 1
    while cont < 11:
        print(n * cont)
        cont += 1

tabuada(ler_numero())
#fazer um programa que verifique o número primo mais próximo do número
#digitado pelo usuário(precisa estar entre 1 e 1000)
n = int(input("Verificar primo mais próximo até: "))
mult=0

#for i in range(2,n):
#    if (n % i == 0):
#        print("Múltiplo de",i)
#        mult += 1

#if(mult==0):
#    print("É primo")
#else:
#    print("Tem",mult," múltiplos acima de 2 e abaixo de",n)

n = int(input("Digite um número inteiro: "))
cont = 0
i = 0

while i <= n or cont < 2:
    i = i + 1
    x = n % i
if x == 0:
    cont = cont + 1

if cont <= 2:
    print("primo")
else:
    print("não primo")
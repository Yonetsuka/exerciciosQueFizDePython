#6.Número  primo  é  aquele  que  somente  é  divisível  por  1  e  por  ele  mesmo.
#Fazer  um  algoritmo  que  solicite  um número e informe se esse número é primo ou não.
num = int(input('Digite um numero: '))
cont = 1
fin = 0
while cont <= num:
    res = num % cont
    if res == 0:
        fin += cont
    cont += 1
if fin == num + 1:
    print('O número é primo')
else:
    print('O número não é primo')
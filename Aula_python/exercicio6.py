#6.Solicite vários números  ao  usuário  (até  que  ele  digite  o  número  zero)  
#e  informe  o somatório dos números digitados.
a = True
soma = 0
while a != False:
    num = int(input('Digite um número: '))
    soma += num
    if num == 0:
        a = False
print(f'A soma dos números é {soma}')
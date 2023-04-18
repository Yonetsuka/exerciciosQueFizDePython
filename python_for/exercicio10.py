#10.Escreva um algoritmo que determine se um número N (digitado pelo usuário) é primo ou não.
n = int(input('Diite um número inteiro: '))
valido = 0
for i in range(1, n + 1, 1):
    if n % i == 0:
        valido += 1
if valido == 2:
    print('o Número é primo')
else:
    print('O número não é primo')
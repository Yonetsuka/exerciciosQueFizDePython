#8.Escreva um algoritmo que solicite o valor de N e calcule o fatorial de N.
n = int(input('Digite o número: '))
fatorial = 1
for i in range(1,n + 1,1):
    fatorial *= i
print(f'O fatorial do numero {n} é {fatorial}')
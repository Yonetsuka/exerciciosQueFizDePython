#6.Criar um algoritmo que leia deznúmeros inteiros e informe o maior e o menor número.
num = int(input('Digite um número inteiro: '))
maior = num
menor = num
for i in range(0,9,1):
    num = int(input('Digite um número inteiro: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(f'O maior número é {maior} e o menor é {menor}')
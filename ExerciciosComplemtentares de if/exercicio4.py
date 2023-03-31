#Escreva um programa que solicite um número inteiro maior do que zero e menor do que 1000 
#e exiba a soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá 
#o valor 8 (2 + 5 + 1). Se o número lido nãofor maior do que zero ou menor do que 1000, 
#o programa terminará com a mensagem “Número inválido”.

num = int(input('Digite um numero que seja maior que zero e menor que 1000:'))
if num > 0 and num < 1000:
    centena = num // 100
    dezena = (num // 10) - centena * 10
    unidade = (num // 1) - centena * 100 - dezena * 10
    resposta = centena + dezena + unidade
    print(f'A soma deu {resposta}')
else:
    print('Número inválido')
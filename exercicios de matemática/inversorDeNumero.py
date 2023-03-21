#inversor de número
numero = int(input('digite um número de três digitos:'))
numero1 = numero // 100
numero = numero % 100
numero2 = numero // 10
numero = numero % 10
numero3 = numero
print(f'o numero inverso é {numero3}{numero2}{numero1}')
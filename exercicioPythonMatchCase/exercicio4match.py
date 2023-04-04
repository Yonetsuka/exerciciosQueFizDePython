#Faça um algoritmo que leia o código da palestra de um evento e exiba o local 
#em que ela será realizada

print('1 - linux')
print('2 - banco de dados')
print('3 - Windows Server')
print('4 - Lógica  e programação')

opção = int(input('Informe a opção desejada: '))

match opção:
    case 1:
        print('Auditório')
    case 2:
        print('Auditório 2')
    case 3:
        print('Auditório 3')
    case 4:
        print('Auditório 3')
    case _:
        print('Opção inválida')
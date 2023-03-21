#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.
salário_atual = int(input('Digite o salário: '))
print(f'Seu salario antes era de {salário_atual}')
if salário_atual < 280:
    print('Haverá um aumento de 20%')
    aumento = (salário_atual / 100) * 20
    print(f'O aumento foi de {aumento}')
    salário_atual + aumento
    print(f'O salário final é de {salário_atual}')
if 280 < salário_atual < 700:
    print('Haverá um aumento de 15%')
    aumento = (salário_atual / 100) * 15
    print(f'O aumento foi de {aumento}')
    salário_atual + aumento
    print(f'O salário final é de {salário_atual}')
if 700 < salário_atual < 1500:
    print('Haverá um aumento de 10%')
    aumento = (salário_atual / 100) * 10
    print(f'O aumento foi de {aumento}')
    salário_atual + aumento
    print(f'O salário final é de {salário_atual}')
if salário_atual < 1500:
    print('Haverá um aumento de 5%')
    aumento = (salário_atual / 100) * 5
    print(f'O aumento foi de {aumento}')
    salário_atual + aumento
    print(f'O salário final é de {salário_atual}')
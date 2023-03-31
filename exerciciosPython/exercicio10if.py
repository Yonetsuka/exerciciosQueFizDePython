#Faça um algoritmo que solicite o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. 
#Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor, 
#calcular e escrever o seu salário total.

salario = float(input('Informeo salário do vendedor: '))

if salario <= 1500:
  aumento = salario * 3 / 100
  total = salario + aumento
  print(f'Salário final: {total}')
else:
  aumento1 = 1500 * 3 / 100
  aumento2 = (salario - 1500) * 5 / 100
  total = salario + aumento1 + aumento2
  print(f'Salário final: {total}')

#6.Implementar uma função que recebe como parâmetro a altura em metros (exemplo: 1.70) 
#e o sexo ('M' para masculino e 'F' para feminino) de uma pessoa e retorne o seu peso ideal,
#sendo que:Peso Ideal (para homens) = (72.7 * altura) -58
#Peso Ideal (para mulheres) = (62.1 * altura) -44.7

def pesoIdeal(altura,sexo):
    if sexo == 'M' or sexo == 'm':
        pesoIdeal = (72.7 *  altura) - 58
        print(f'Seu peso ideal é {pesoIdeal}')
    elif sexo == 'F' or sexo == 'f':
        pesoIdeal = (62.1 *  altura) - 44.7
        print(f'Seu peso ideal é {pesoIdeal}')
    else:
        print('Sexo inválido')

altura = float(input('Digite sua altura: '))
sexo = input('Digite o seu sexo: ')

pesoIdeal(altura, sexo)
#Faça um Programa que peça dois números e imprima o maior deles.
numero1 = int(input('Digite um numero:'))
numero2 = int(input('Digite outro numero:'))
if numero1 > numero2:
    print(f'{numero1} é maior que {numero2}')
if numero1 == numero2:
    print('ambos são o mesmo número')
if numero1 < numero2:
    print(f'{numero2} é maior que {numero1}')
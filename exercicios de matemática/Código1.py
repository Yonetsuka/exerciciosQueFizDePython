#calculadora de imc 
peso = float(input('informe seu peso:'))
altura = float(input('informe sua altura:'))
imc = peso / (altura * altura)
print(f'Seu imc é de {imc}')
if imc < 18.5:
    print('Você está abaixo do peso normal')
if 18.5 <= imc <= 24.9:
    print('Você está no peso normal')
if 24.9 < imc:
    print('Você está acima do peso normal')
#Faça um algoritmo que solicita ao usuário dois números inteiros. 
#O primeiro é o valor das horas e o segundo dos minutos. 
#Verifique se a hora é válida ou inválida e exiba uma mensagem correspondente 
# (São válidas as horas entre 00:00 e 23:59).
num1 = int(input('Digite o valor das horas:'))
num2 = int(input('Digite o valor dos minutos:'))
if horas >= 0 and horas <= 23 and minutos >= 0 and minutos <= 59:
    print('Horas e minutos válidos')
    print(f'{num1} horas e {num2} minutos')
else:
    print('Horas e/ou minutos inváldos')

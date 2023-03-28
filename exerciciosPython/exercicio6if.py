#Faça um algoritmo que solicita ao usuário dois números inteiros. 
#O primeiro é o valor das horas e o segundo dos minutos. 
#Verifique se a hora é válida ou inválida e exiba uma mensagem correspondente 
# (São válidas as horas entre 00:00 e 23:59).
num1 = int(input('Digite o valor das horas:'))
num2 = int(input('Digite o valor dos minutos:'))
if 0 < num1 < 23:
    valido = True
elif num1 > 23 or num1 < 0:
    valido = False
if 0 < num2 < 59:
    valido1 = True
elif num2 > 59 or num2 < 0:
    valido1 = False
if valido == True:
    if valido1 == True:
        print(f"As horas são {num1}:{num2}")
else:
    print('Valores para horas e/ou minutos inválidos')
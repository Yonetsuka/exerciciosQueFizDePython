#3.Construa um algoritmo que mostre todos os valores ímpares entre X e Y, 
#onde X e Y são fornecidos pelo usuário.
cont = 0
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número:'))
if num1 < num2:
    while num1 <= num2:
        if num1 % 2 == 1:
            print(num1)
            num1+=1
        else:
            num1 += 1
if num2 < num1:
    while num2 <= num1:
        if num2 % 2 == 1:
            print(num2)
            num2+=1
        else:
            num2 += 1
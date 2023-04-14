#5.Fazer um algoritmo que soliciteum número indeterminado de idades de um grupo de indivíduos. 
#A última idade, que não entrará nos cálculos, contém o valor da idade igual a zero. 
#Calcule a média de idade deste grupo de indivíduos.
total = 0
divisor = 0
valido = True
while valido == True:
    num = int(input('Digite quantos números de idades quiser(para acabar, escreva zero):'))
    if num == 0:
        valido = False 
    total += num
    divisor += 1
media = total / divisor
print(f'A média das idades é {media}')
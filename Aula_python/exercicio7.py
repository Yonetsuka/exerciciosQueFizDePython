#7.Solicite dois números diferentes ao usuário 
#(caso os números sejam iguais, o algoritmo deve solicitar os números novamente) 
#e informe a diferença entre o maior e o menor número. 
diferenca = 0
iguais = True
while iguais == True:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    if num1 != num2:
        iguais = False
    elif num1 == num2:
        print('Números inválidos, insira novamente')
if num1 > num2:
    diferenca = num1 - num2
    print(f'A diferença entre os números é {diferenca}')
elif num2 > num1:
    diferenca = num2 - num1
    print(f'A diferença entre os números é {diferenca}')
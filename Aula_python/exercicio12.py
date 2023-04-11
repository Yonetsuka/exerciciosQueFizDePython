#12.Faça um algoritmo que solicite um número inteiro ao usuário e calcule o fatorial desse número.
#O fatorial de  um  número N é  a  multiplicação  de N por  seus  antecessores maiores ou 
#iguais a 1.Por exemplo: o fatorial de 5 é igual a 5*4*3*2*1 = 120.
fatorial = 1
num = int(input('Digite um número para calcular seu fatorial: '))
while num != 1:
    fatorial *= num
    num -= 1
print(f'O fatorial do número é {fatorial}')
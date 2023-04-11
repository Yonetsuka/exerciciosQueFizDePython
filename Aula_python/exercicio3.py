#3.Escreva  um  algoritmo  que solicite a  idade  de  15  pessoas  e  informe  
#a  quantidade  de pessoas com idade inferior a 18 anos.
contagem = 1
pessoas = 0
while contagem != 16:
    idade = int(input('Digite sua idade: '))
    if idade < 18:
        pessoas +=1
    contagem += 1
print(f'Há {pessoas} pessoas com menos de 18 anos')
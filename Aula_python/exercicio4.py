#4.Escreva um algoritmo que solicite 10 números e informe quantos números entre 
# 100 e 200 foram digitados.
contagem = 1
entre = 0
while contagem != 11:
    num = int(input('Digite um número: '))
    if 100 < num < 200:
        entre += 1
    contagem += 1
print(f'Havia {entre} números entre 100 e 200')
#9.Faça  um  algoritmo  que  solicite  N  números  e  calcule  a  média  dos  números  pares  
#e  a média  dos  números  ímpares  (o  valor  de  N  deve  ser solicitado  ao usuário no  
#início  do programa).
n = int(input('Digite quantos números serão digitados'))
cont = 0
impar = 0
par = 0
dividir_i = 0
dividir_p = 0
while cont < n:
    num = int(input('Digite um número:'))
    if num % 2 == 1:
        impar += num
        dividir_i += 1
    if num % 2 == 0:
        par += num
        dividir_p += 1
    cont += 1
media_i = impar / dividir_i
media_p = par / dividir_p
print(f'A média dos números pares é {media_p} e dos ímpares é {media_i}')
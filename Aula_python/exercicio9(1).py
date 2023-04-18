#9.Faça  um  algoritmo  que  solicite  N  números  e  calcule  a  média  dos  números  pares  
#e  a média  dos  números  ímpares  (o  valor  de  N  deve  ser solicitado  ao usuário no  
#início  do programa).
n = int(input('Digite quantos números serão digitados:'))
cont = 0
impar = 0
par = 0
dividir_i = 0
dividir_p = 0
media_p = 0
media_i = 0
while cont < n:
    num = int(input('Digite um número:'))
    if num % 2 == 1:
        impar += num
        dividir_i += 1
    if num % 2 == 0:
        par += num
        dividir_p += 1
    cont += 1
if impar !=0:
    media_i = impar / dividir_i
if impar !=0:
    media_p = par / dividir_p
if media_i == 0:
    print(f'A média dos números ímpares é {media_i}')
elif media_p == 0:
    print(f'A média dos números pares é {media_p}')
else:
    print(f'A média dos números pares é {media_p} e dos ímpares é {media_i}')

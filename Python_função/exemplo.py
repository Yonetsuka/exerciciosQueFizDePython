#break
#para de fazer as repetições
num = 0

while True:     #loop infinito
    n = int(input('Numero: '))

    if n == -1:
        for num in range(-1, 1000000):
            print(num)
            num += 1

    if n == 0:
        break

    if n % 2 == 0:
        print('Par')

    elif n % 2 == 1:
        print('Impar')
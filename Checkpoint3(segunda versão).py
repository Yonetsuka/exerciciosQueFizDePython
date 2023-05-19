import math

# Coeficientes da equação
a = int(input("Digite o primeiro numero da equação: "))
b = int(input("Digite o segundo numero da equação: "))
c = int(input("Digite o terceiro numero da equação: "))

# Calcula o discriminante
delta = b**2 - 4*a*c

#Encontrando os vértices
x_vertice = -b / (2*a)
y_vertice = a * x_vertice**2 + b * x_vertice + c

# Verifica as raízes da equação
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Raízes reais distintas:")
    print("x1 =", x1)
    print("x2 =", x2)
    print("Soma =", x1 + x2)
    print("Produto =", x1 * x2)
    print("Xv =", x_vertice)
    print("Yv =", y_vertice)
elif delta == 0:
    x = -b / (2*a)
    print("Raízes reais iguais:")
    print("x =", x)
else:
    print("Raízes complexas.")

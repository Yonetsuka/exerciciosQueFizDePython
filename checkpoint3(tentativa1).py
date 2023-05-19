import matplotlib.pyplot as plt
import numpy as np

a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))
delta = b**2 - 4*a*c

x = np.linspace(-10, 10, 400)

y = a * x**2 + b * x + c

plt.plot(x, y)

plt.title("Gráfico da Equação Quadrática")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")

plt.show()

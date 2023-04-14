#7.Solicite um número inteiro positivo e informe a soma dos algarismos desse número
n = int(input("Digite um número inteiro: "))

soma = 0

while (n > 0):

    resto = n % 10
    n = (n - resto)/10
    soma = soma + resto


print("A soma dos números é: ", soma)

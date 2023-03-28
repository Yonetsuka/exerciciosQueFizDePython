#Faça  um  algoritmo  que  solicita  ao  usuário  uma  letra e  
#exiba  uma mensagem  informando  se  é  uma vogal ou uma consoante.
letra = input("Diite uma letra: ")
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(f"A letra {letra} é uma vogal")
else:
    print(f"A letra {letra} é uma consoante")
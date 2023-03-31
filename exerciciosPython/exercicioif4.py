#Faça  um  algoritmo  que  solicita  ao  usuário  uma  letra e  
#exiba  uma mensagem  informando  se  é  uma vogal ou uma consoante.
letra = input("Diite uma letra: ")

letra = letra.lower() #Transformando as letras em minusculas

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(f"A letra {letra} é uma vogal")
else:
    print(f"A letra {letra} é uma consoante")
#-----------------------------------------------------------------------------------
#outra forma de resolver o problema
vogais = "aeiouAIUEO"

if letra in vogais:
    print('Vogal')
else:
    print('Consoante')

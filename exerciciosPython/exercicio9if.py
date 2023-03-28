#Faça um algoritmo que  solicita ao usuário três valores correspondentes  
# aos lados de  um triângulo. Informe  se  o  triângulo  é  equilátero  
# (possui  3  lados  iguais),  isósceles  (possui  dois  lados  iguais)  
# ou escaleno (não possui lados iguais).
medida1 = float(input('Digite um dos lados do triângulo:'))
medida2 = float(input('Digite outro lado do triângulo:'))
medida3 = float(input('Digite o ultimo lado do triângulo:'))
if medida1 == medida2 == medida3:
    print('O triângulo é equilátero')
if medida1 == medida2 and medida1 != medida3 or medida3 == medida2 and medida1 != medida3 or medida1 == medida3 and medida2 != medida3:
    print('O triâgulo é isóceles')
if medida1 != medida2 and medida1 != medida3:
    print('O triângulo é escaleno')
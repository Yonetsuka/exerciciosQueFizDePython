#Faça  um  algoritmo  que  solicita  ao  usuário  as  notas  de  três  provas.
#Calcule  a  média  aritmética  e informe se o aluno foi Aprovado ou Reprovado
#(o aluno é considerado aprovado com a média igual ou superior a 6)
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
média = (nota1 + nota2 + nota3) / 3
if média >= 6:
    print('Você foi aprovado')
else:
    print('Você está reprovado :(')
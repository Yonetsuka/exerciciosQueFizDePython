#1.Escreva  um  programa  para solicitaras  notas  de  duas provas.  
#Faça  uma função que  receba  as  duas notas por parâmetro e exibe a mensagem 
#“Você foi Aprovado!” ou “Você foi Reprovado!”. Considere 6.0 a média mínima para aprovação.

def verNota():
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    if media >= 6:
        print('Você foi aprovado')
    else:
        print('Você foi reprovado')

verNota()
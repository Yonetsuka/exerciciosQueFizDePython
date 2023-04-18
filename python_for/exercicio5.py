#5.Solicite a quantidade de alunos de uma turma e a quantidade de notas. 
#Para cada aluno, solicite as suas notas e exiba a sua respectiva média
#(a média deve ser arredondada para duas casas decimais).
cont = 1
alunos = int(input('Digite o número de alunos: '))
for i in range(0,alunos,1):
    nota1 = int(input('Insira sua primeira nota: '))
    nota2 = int(input('Insira sua segunda nota: '))
    nota3 = int(input('Insira sua terceira nota: '))
    nota4 = int(input('Insira sua quarta nota: '))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    media = round(media,2)
    cont += 1
    print(f'A média do aluno {cont} é {media}')
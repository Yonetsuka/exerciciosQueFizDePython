#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
#(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa 
#o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
peso_do_peixe = int(input('quantos quilos trouxe ?'))
excesso = peso_do_peixe - 50
multa = excesso * 4
if excesso < 0:
    print('Você não trouxe nenhum pexie em excesso')
if excesso == 0:
    print('Você trouxe o limite de peixes')
if excesso > 0:
    print(f'Você trouxe {excesso} quilos a mais e terá de pagar uma multa de {multa}')
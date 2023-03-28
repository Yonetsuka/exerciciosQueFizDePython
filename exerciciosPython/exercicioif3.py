#Faça  um  algoritmo  que  solicita  ao  usuário  um  número  inteiro  e  exiba  este  número
#na  tela.  Se  o número for negativo, antes de ser exibido, 
# ele deve ser transformado no equivalente positivo.
num = int(input('Digite um numero inteiro'))
if num < 0:
    num = num * -1
print(num)
try:
    raise TypeError("ERRO !!!")
except TypeError as mensagem:
    print('Ocorreu um erro: ',mensagem)
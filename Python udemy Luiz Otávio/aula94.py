# try, except, else e finally

try: 
    print('Abri arquivo')
    8/0 # forçando erro
except ZeroDivisionError:
    print('Dividiu zero')
else: # para quando não der erro
    print('Não deu erro.')
finally:
    print('Fechar arquivo')

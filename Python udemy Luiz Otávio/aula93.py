# Try, except e finally

try:
    a = 18
    b = 0
    # print(b[0]) # causando um erro
    print('Linha 1'[10000])
    c = a / b
    print('Linha 2')
except NameError:
    print('Nome b não está definido')
except ZeroDivisionError:
    print('Dividiu por zero.')
except (TypeError, IndexError)as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome do error:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO')

print('Continuar')
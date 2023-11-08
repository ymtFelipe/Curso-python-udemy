# dir, hasattr e getattr em Python

string = 'felipe'
metodo = 'upper'

if hasattr(string, metodo):
    print('Exsite upper')
    print(string.upper())
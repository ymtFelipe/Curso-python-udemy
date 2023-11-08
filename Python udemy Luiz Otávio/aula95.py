# raise - lançamento exceções (erros)

def nao_aceito_zero(d): # essa função trata um erro caso o divisor venha como 0.
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero.')
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError (f'"{n}" Deve ser int ou float. '
                         f'"{tipo_n.__name__}" enviado')     
    return True


def divide(n, d): # faz e retorna a divisão.
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d) # enviando o divisor para testar se é 0.
    return n / d

print(divide(8, '0'))
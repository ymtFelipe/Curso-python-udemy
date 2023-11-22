def validar(f):
    def valida(x, y):
        if x < 0 or y < 0:
            raise ValueError('X e Y não podem ser negativos.')
        x *= 10
        y *= 5
        return f(x, y)
    return valida   
   
@validar
def soma(x, y):
    return x + y


print(soma(10, 10))
# Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}


dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in  produto.items()
    if chave != 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('b', 'valor c'),
]

dc = {
    chave: valor
    for chave, valor in lista
}



# print(dict(lista))
# print(dc)

# s1 = {i for i in range(10)}

print(set(range(10))) 
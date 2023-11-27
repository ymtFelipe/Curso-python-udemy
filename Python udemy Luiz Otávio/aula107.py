# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper():
    return [(cidades[c], estados[c]) for c in range(len(cidades))]


print(zipper())

# solução professor: 

# def zipper(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return [(l1[c], l2[c]) for c in range(intervalo)]
from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1, l2)))
print(list(zip_longest(l1, l2, fillvalue='Sem valor')))


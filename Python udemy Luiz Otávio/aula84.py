# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
import pprint
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [numero * 2 for numero in range(10)]
# print(lista)
txt = "Hello World"
x = txt.strip
# print(x)

#Aula 2
# Mapeamento de dados em list comprehension

produtos = [
    {'name': 'p1', 'price': 20,},
    {'name': 'p2', 'price': 10,},
    {'name': 'p3', 'price': 30,},
]

novos_produtos = [
    {**produto, 'price': produto['price'] * 1.05}
    if produto['price'] > 20 else {**produto}
    for  produto in produtos
    if produto['price'] > 10
]
pprint.pprint(novos_produtos)
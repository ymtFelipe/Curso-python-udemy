# minha solução:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = []

def zipper(l1, l2):
    contador = min(len(l1), len(l2))   
    for c in range(contador):
        lista_soma.append(l1[c] + l2[c])
    return lista_soma

print(zipper(lista_a, lista_b))
# fim da minha solução.


# solução professor:

lista_soma = []
# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)


# for i, _ in enumerate(lista_b):
#       lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)


lista_soma = [x + y for x, y in zip(lista_a, lista_b)]# Foda!
print(lista_soma)

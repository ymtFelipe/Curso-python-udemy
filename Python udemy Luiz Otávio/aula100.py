# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
# import copy
# novos_produtos = copy.deepcopy([{"nome": produto["nome"], "preco": round(produto["preco"] * 1.10, 2)} for produto in produtos])


# print(produtos)
# print(novos_produtos)

# # fazendo sem usar o deep copy
# novos_produtos = []
# for c in range(len(produtos)): 
#         novos_produtos.append({"nome": produtos[c]['nome'],"preco":round(produtos[c]['preco'] * 1.1, 2)})

# print(produtos)
# print(novos_produtos)



# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

print(sorted(produtos[0].items()))

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
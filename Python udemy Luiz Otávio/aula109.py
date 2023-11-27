from itertools import combinations, permutations, product

pessoas = [
    'João', 'Joana', 'Felipe', 'Letícia'
    ]
camisetas = [
    ['Preta', 'Branca'],
    ['p', 'm'],
    ]

def print_iter(iterator):
    print(*list(iterator), sep= '\n')
    print()

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))
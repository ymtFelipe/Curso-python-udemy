# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços':{'rua': 'tal tal', 'número': 123}{'rua': 'outra rua', 'número': 321}
#     }

pessoa = dict(nome="Luiz Otávio", sobrenome="Miranda")
pessoa = {
    "nome": "Luiz Otávio",
    "sobrenome": "Miranda",
    "idade": 18,
    "altura": 1.8,
    "endereços": [
        {"rua": "tal tal", "número": 123},
        {"rua": "outra rua", "número": 321},
    ],
}
# print(pessoa, type(pessoa))
print(pessoa["nome"])
print(pessoa["sobrenome"])

print()

for chave in pessoa:
    print(chave, pessoa[chave])


pessoa = {
    "Sobrenome": "Alcântara",
    "Idade": 27,
    "Altura": 1.85,
    "Endereço:": [
        {"Endereço 1": "Rua são marcelo", "Numero": 5000},
        {"Endereço 2": "Rua são marcos", "Numero": 1515},
    ],
}
# pessoa["Nome"] = "Felipe"
# print(pessoa["Endereço:"][0]["Numero"])

# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

# chave = "nome"

# pessoa[chave] = "Luiz Otávio"
# pessoa["sobrenome"] = "Miranda"


# print(pessoa[chave])

# pessoa[chave] = "Maria"

# del pessoa["sobrenome"]
# print(pessoa)
# print(pessoa["nome"])

# # print(pessoa.get('sobrenome'))
# if (
#     pessoa.get("sobrenome") is None
# ):  # verifica se tem uma chave chama 'Sobrenome' se não..
#     print("NÃO EXISTE")
# else:
#     print(pessoa["sobrenome"])

# print('ISSO Não vai')


####     PARTE 1


# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    "nome": "Luiz Otávio",
    "sobrenome": "Miranda",
    "idade": 900,
}

pessoa.setdefault("idade", 0)
print(pessoa["idade"])


print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))

for valor in pessoa.values():
    print(valor)

for chave, valor in pessoa.items():
    print(chave, valor)

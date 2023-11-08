a, b = 1, 2
b, a = a, b
# print(a, b)


pessoa = {
    "nome": "Aline",
    "sobrenome": "Souza",
}
(a1, a2), b = pessoa.items()
# print(a1, a2)
# print(b)


# for chave, valor in pessoa.items():
#     print(f"Chave {chave} e valor {valor}")

dados_pessoa = {
    "idade": 27,
    "altura": 1.85,
}
pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

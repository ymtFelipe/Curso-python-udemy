# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        "Pergunta": "Quanto é 2+2?",
        "Opções": ["1", "3", "4", "5", "7", "8"],
        "Resposta": "4",
    },
    {
        "Pergunta": "Quanto é 5*5?",
        "Opções": ["25", "55", "10", "51"],
        "Resposta": "25",
    },
    {
        "Pergunta": "Quanto é 10/2?",
        "Opções": ["4", "5", "2", "1"],
        "Resposta": "5",
    },
]
# count = 0
# for i in range(0, len(perguntas)):
#     print()
#     print(perguntas[i]["Pergunta"])
#     print()
#     c = 0
#     for resposta in perguntas[i]["Opções"]:
#         print(f"{c}) {resposta}")
#         c += 1
#     resposta_1 = input("Escolha uma opção: ")
#     resposta = perguntas[i]["Opções"][int(resposta_1)]
#     if resposta == perguntas[i]["Resposta"]:
#         print("Acertou 👍")
#         count += 1
#     else:
#         print("Errou ❌")
# print()
# print(f"Você acertou o total de {count}\nde {len(perguntas)} pertuntas.")
count = indice = 0
for pergunta in perguntas:
    print(pergunta["Pergunta"])
    print()
    for i, opções in enumerate(perguntas[indice]["Opções"]):
        print(f"{i}) {opções}")
    try:
        reposta = int(input("Escolha uma opção: "))
    except ValueError:
        print("Valor incorreto.")
    try:
        if str(perguntas[indice]["Opções"][reposta]) == perguntas[indice]["Resposta"]:
            print("Acertou 👍")
            print()
            count += 1
        else:
            print("Errou ❌")
    except:
        print("Errou ❌")
    indice += 1
print(f"Total de perguntas acertadas: {count}.\nde {len(perguntas)} perguntas")

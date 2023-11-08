frase = (
    "O python é uma linguagem de programação "
    "multiparadigma. "
    "Python foi criado por Guido van Rossum."
)

# letra = input("Qual a letra você deseja saber? ").upper()
# countLetra = 0
# for c in range(0, len(frase)):
#     if frase[c].upper() == letra:
#         countLetra += 1

# print(f"A letra {letra} apareceu {countLetra} vezes.")

tot_letra_apareceu = 0
letra_mais_aparece = ""
i = 0
while i < len(frase):
    tot_letra = frase.count(frase[i])

    if frase[i] == " ":
        i += 1
        continue

    if tot_letra_apareceu < tot_letra:
        tot_letra_apareceu = tot_letra
        letra_mais_aparece = frase[i].upper()

    i += 1
print(
    f"A letra que mais apareceu foi '{letra_mais_aparece}' com o total de: {tot_letra_apareceu}"
)

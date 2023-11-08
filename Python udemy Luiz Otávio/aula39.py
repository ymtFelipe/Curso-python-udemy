nome = "Felipe Alcantara"
cont = 0
new_string = ""
while True:
    new_string += "*" + nome[cont]
    cont += 1
    if cont == len(nome):
        break
print(new_string)

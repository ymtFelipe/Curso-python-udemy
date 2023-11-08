"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
name = input("Nome: ")  # pega o nome do usuário
age = int(input("Idade: "))  # pega a idade do usuário

if len(name) > 0 and age > 0:
    print(f"Seu nome é {name}")
    print(f"Seu nome invertido é {name[::-1]}")
    if " " in name:
        print("Seu nome contém espaço")
    else:
        print("Seu nome não contém espaço")
    print(f"Seu nome tem {len(name)} letras")
    print(f"A primeira letra do seu nome é {name[0]}")
    print(f"A ultima letra do seu nome é {name[-1]}")
else:
    print("Desculpe, você deixou camps vazios.")

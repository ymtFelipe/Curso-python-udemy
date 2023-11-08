import os

list = []
while True:
    print("Select one option.")
    try:
        option = int(input("1. Inserir  2. Apagar  3. Listar: "))
    except:
        print("Option wrong.")

    if option == 1:
        try:
            os.system("cls")
            list.append(input("Product name: "))
        except:
            ...
    elif option == 2:
        try:
            del list[int(input("Indice of product: "))]
            os.system("cls")
        except:
            os.system("cls")
            print("Indice of product wrong.")

    elif option == 3:
        if len(list) == 0:
            os.system("cls")
            print("Nothing to see.")
        else:
            os.system("cls")
            for c in range(0, len(list)):
                print(f"{c}  {list[c]}")

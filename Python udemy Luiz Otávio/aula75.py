def multi(num):
    if not num.isdigit():
        return print("Isso não é um número.")

    return (
        f"O dobro de {num} é {int(num)*2}\n"
        f"O triplo de {num} é {int(num)*3}\n"
        f"O quádruplo de {num} é {int(num)*4}\n"
    )


number = multi(input("Digite um numero: "))
print(number)

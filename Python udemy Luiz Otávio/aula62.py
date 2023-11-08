"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
while True:
    soma_total = 0
    numb1 = 10
    lista_total_digitos = ""
    print("EX: xxx.xxx.xxx-xx")
    list_digistos = ["746.824.890-70"]  # input("Digite o seu CPF: ").strip()
    for c in range(0, len(list_digistos[0])):  # removendo os '.' e '-'
        if list_digistos[0][c] == "." or list_digistos[0][c] == "-":
            continue
        else:
            lista_total_digitos += list_digistos[0][c]
    cpf = lista_total_digitos[:9]
    try:
        for c in cpf:  # fazendo a soma total dos 9 digitos
            soma_total += numb1 * int(c)
            numb1 -= 1
    except ValueError:
        print("CPF inválido.")
        continue
    digito1 = (soma_total * 10) % 11
    digito1 = digito1 if digito1 <= 9 else 0
    break

cpf = cpf + str(digito1)
soma_total = 0
numb1 = 11
try:
    for c in cpf:  # fazendo a soma total dos 10 digitos
        soma_total += numb1 * int(c)
        numb1 -= 1
except ValueError:
    print("CPF inválido.")

digito2 = (soma_total * 10) % 11

if digito2 > 9:
    digito2 == 0
    cpf = cpf + str(digito2)
else:
    cpf = cpf + str(digito2)

cpf.join("12121")
print(f"Seu CPF é válido.")
print(cpf)

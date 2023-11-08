"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

while True:
    soma_total = 0
    numb1 = 10
    lista_total_digitos = ""
    print("EX: xxx.xxx.xxx-xx")
    list_digistos = [input("Digite o seu CPF: ").strip()]
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
    print(digito1)
    break

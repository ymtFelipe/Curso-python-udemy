"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
  """

# num = input("Enter a int number: ")
# try:
#     if float(num) % 2 == 0:
#         print(f"The num {num} is pair.")
#     else:
#         print(f"The num {num} is odd")
# except:
#     print("This num is not a number int.")
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
try:
    date = int(input("Hour: "))

    if date >= 0 and date <= 11:
        print(f"GOOD MORNING.")
    elif date >= 12:
        print(f"GOOD AFTERNOON.")
    elif date >= 18:
        print(f"GOOD EVENING.")
    else:
        print(f"Digitou errado.")
except:
    print("Please, enter only a int numbers")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
name = input("Enter your first name: ").strip()
lenName = len(name)
if lenName <= 4:
    print("Your name is small.")
elif lenName == 5 or lenName == 6:
    print("Your name is normal.")
else:
    print("Your name is very large.")

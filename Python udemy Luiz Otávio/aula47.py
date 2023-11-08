# Faça um jogo para o usuário adivinhar qual a palavra secreta.
# - Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
# - Quando o usuário digitar uma letra, você vai conferir se a letra digitada estána palavra secreta.
#     - Se a letra digitada estiver na palavra secreta; exiba a letra;
#     - Se a letra digitada não estiver na palavra secreta; exiba *.
# Faça a contagem de tentativas do seu usuário.

secret_word = "DINNER"  # Palavra secreta
print("Have in all dinner.")
secret_word_in_asterisk = ["*"] * len(
    secret_word
)  # Colocando asterisco no lugar da letra para mostrar para o usuário

count = 0
final_word = ""

while True:
    final_word = ""
    for (
        c
    ) in (
        secret_word_in_asterisk
    ):  # Colocando a lista em uma variável. ex: [0,3,4] para 0,3,4
        final_word += c
    print(f'The word: "{final_word}".')  # Print da palavra secreta
    if (
        final_word.upper() == secret_word.upper()
    ):  # Serve para finalizar o laço do while
        break

    user_letter = input("Type a letter: ").strip().upper()  # Contador
    count += 1

    if len(user_letter) > 1:  # Verifica se ele digitou uma letra ou mais
        print("Only 1 letter.")
        continue

    if (
        user_letter in secret_word
    ):  # Aqui ele verifica se tem na palavra secreta a mesma letra digitada pelo usuario
        for c in range(0, len(secret_word)):
            if (
                secret_word[c] == user_letter
            ):  # Verificando em qual array está a letra do usuario
                secret_word_in_asterisk[c] = user_letter
    else:
        print(
            "Não tem essa letra na palavra secreta."
        )  # Print dizendo que não existe essa letra na palavra secreta
        continue

print(f"You did it. The word was: {secret_word}")
print(f"Tries: {count}")

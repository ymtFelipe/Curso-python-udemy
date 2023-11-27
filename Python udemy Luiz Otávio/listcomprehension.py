# numeros = [1,2,3,4,5,6,7,8,9,10]
# novos_numeros = [numero for numero in numeros if numero > 5]
# pares = [numero for numero in numeros if numero % 2 == 0]
# impares = [numero for numero in numeros if numero % 2 == 1 ]
# outro_if = [numero if numero != 6 else 600 for numero in numeros if numero % 2 == 0]


# print(numeros)
# print(novos_numeros)
# print(pares)
# print(impares)
# print(outro_if)

# linhas_e_colunas = [
#     (x, y) 
#     if y != 2 else (x *1000, y * 1000)
#     for x in range(1, 11)
#     for y in range(1,6)
#     if x != 2
# ]
# print(linhas_e_colunas)



# string = 'Felipe Alcantara'
# numero_de_letras = 1
# nova_sring = ['.'.join(
#     string[indice:indice + numero_de_letras] 
#     for indice in range(0, len(string), numero_de_letras)
#     )]
# print(string)
# print(nova_sring)

# nomes = ['Luiz','Maria','Helena','Joana','Felipe']
# novos_nomes = [
#     f'{nome[:-1].lower()+nome[-1].upper()}'
#     for nome in nomes]
# print(novos_nomes)


numeros = [[numero, numero ** 2] for numero in range(10)]
flat = [y for x in numeros for y in x]
print(numeros)
print(flat)


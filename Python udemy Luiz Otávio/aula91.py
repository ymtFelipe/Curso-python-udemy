# Introdução às Generator functions em python
# generator = (n for n in range(10000))

# def generator(n=0):
#     yield 1 # pausou
#     print('Continuando...')
#     yield 2 # pausou
#     print('Testando mais uma vez...')
#     yield 3 # pausou
#     print('Finalizando')
#     return 'Acabou' # aparece como StopInteration

# gen = generator(n=0) # para acessar o valor, precisa usar o next

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# for n in gen:
#     print(n)

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n >= maximum:
            return

        

gen = generator(n=5, maximum=8) # basicamente um range(5, 8)
for n in gen:
    print(n)

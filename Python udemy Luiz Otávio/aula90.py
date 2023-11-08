import sys
# Generator expression, Iterable e Interators em python
# iterator trabalha com iteravel. tem __iter__ e __next__
# generator é uma função que pausa a cada vez que chamo ela

iterable = ['Eu', 'Tenho', 'Algo']
iterator = (iterable.__iter__()) 
# print(next(iterator)) #  iter() ou __iter__() estou chamando o proximo usando next
# print(next(iterator))
# print(next(iterator))
lista = [n for n in range(100000)]
generator = (n for n in range(100000)) # Não salva todo o valor na memoria. usar next() ou for

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for n in generator:
    print(n)
# __main__
from aula99_package import modulo
import aula99_package.modulo
from aula99_package.modulo import *
# from aula99_package.modulo import soma_do_modulo

print(soma_do_modulo(3, 2))
print(aula99_package.modulo.soma_do_modulo(3, 2))
print(modulo.soma_do_modulo(3, 2))
print(variavel)
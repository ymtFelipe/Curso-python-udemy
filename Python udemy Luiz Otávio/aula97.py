

try: 
    import sys 
    sys.path.append('')

except ModuleNotFoundError:
    ...

import aula97_m

print('Este módulo se chama', __name__)
print(*sys.path, sep='\n')
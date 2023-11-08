def multi(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


def par_ou_impar(x):
    if x % 2 == 0:
        return "PAR"
    else:
        return "IMPAR"


print(multi(1, 3, 4, 5, 6))
print(1 * 3 * 4 * 5 * 6)

print(par_ou_impar(23))

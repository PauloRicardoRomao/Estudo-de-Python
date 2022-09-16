#calculando fatorial
f = 1
c = int(input('Digite um valor: '))
print("O fatorial de {} é {}! = ".format(c, c), end='')
for c in range(c, 1-1, -1):
    print("{}".format(c), end="")
    print(" x " if c > 1 else " = ", end="")
    f = f * c
print(f)
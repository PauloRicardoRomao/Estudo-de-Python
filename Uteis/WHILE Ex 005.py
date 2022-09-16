#progressão aritmética
print("Gerador de PA")
print("=-=" *11)
n = int(input('Digite o primeiro termo: ').strip())
r = int(input('Digite a razão da PA: ').strip())
cont = 0
#PA = 0
print("{}".format(n), end=' → ')
while cont < 10+1:
    n += r
    print("{}".format(n), end="")
    print("" if cont == 10 else " → ",  end="")
    cont += 1
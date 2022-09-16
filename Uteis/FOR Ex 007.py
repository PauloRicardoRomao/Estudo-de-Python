#DESCOBRINDO SE UM NÚMERO É PRIMO ou NÃO
num = int(input('Digite um número: '))
cont = 0
for c in range(1, num+1):
    if (num % c == 0):
        cont += 1
        print("\33[33m", end='')
    else:
        print("\33[31m", end='')
    print("{} ".format(c), end='')

if cont == 2:
    print("\n\33[mO número {} foi divísivel {} vezes(números em amarelo) por isso É primo".format(num, cont))
else:
    print("\n\33[mO número {} foi divísivel {} vezes(números em amarelo) por isso ele NÃO é primo".format(num, cont))
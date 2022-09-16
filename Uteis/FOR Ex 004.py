#REFAZENDO TABUADA USANDO FOR
print("Digite qual tabuada você deseja saber...")
n = int(input('Digite um número: ').strip())
print("-="*7)
for c in range(1, 10+1):
    result = c * n
    print(result)
    #ou
    #print("{}  x  {}  =  {}".format(n, c, n * c))
print("-="*7)
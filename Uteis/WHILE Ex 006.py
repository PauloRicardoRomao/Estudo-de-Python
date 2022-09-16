#GERADOR DE PA 2.0 WHILE
print("GERADOR DE PA 2.0")
print("=-="*10)
n = int(input('Digite um número: ').strip())
r = int(input('Digite a razão da PA: ').strip())
print("=-="*10)
cont = 1
termo = n
total = 0
mais = 10
print("{}".format(n), end=" → ")
while mais != 0:
    total += mais
    while cont <= total:
        termo += r
        print("{}".format(termo), end="")
        print("" if cont == mais else " → ", end="")
        cont += 1
    print("PAUSA")
    mais = int(input('Quantos termo você quer a mais?... ').strip())
print("PROGRESSÃO FINALIZADA COM SUCESSO!")


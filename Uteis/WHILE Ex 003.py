#criando menu

v1 = int(input('Digite um valor: ').strip())
v2 = int(input('Digite um valor: ').strip())
opcao = 0
while opcao != 5:
    print("-=-"*12)
    print("""[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA""")
    opcao = int(input('Qual sua decisão? ').strip())
    print("-=-" * 12)
    if opcao == 1:
        soma = v1 + v2
        print("A soma dos valores corresponde à {}".format(soma))
    elif opcao == 2:
        multiplicacao = v1 * v2
        print("O resultado da multilplicação dos valores é {}".format(multiplicacao))
    elif opcao == 3:
        if v1 > v2:
            print("O maior valor é o primeiro valor")
        else:
            print("O maior valor é o segundo valor")
    elif opcao == 4:
        v1 = int(input('Digite um novo valor: ').strip())
        v2 = int(input('Digite um novo valor: ').strip())
    else:
        print("Opção inválida tente novamente.")

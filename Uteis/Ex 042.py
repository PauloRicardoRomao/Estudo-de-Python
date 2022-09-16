#simulador loja, pagamentos
print("{:=^40}".format(" MERCADO DO SILVA "))
total = float(input('Valor da compra: R$').strip())

print("""Como será feito o pagamnto? 
[ 1 ] Á VISTA
[ 2 ] Á PRAZO""")

tipo = input('Escolha: ').strip()

if (tipo == '1'):
    print("""Pagamento Á VISTA, escolha a forma de pagamento: 
        [ 1 ] Dinherio (10% de desconto)
        [ 2 ] Cheque (10% de desconto)
        [ 3 ] Cartão (5% de desconto)""")
    forma = input('Escolha: ').strip()
    if (forma == '1'):
        print("Você tem direito a 10% de desconto.")
        total = total - (total * 10/100)

    elif (forma == '2'):
        print("Você tem direito a 10% de desconto.")
        total = total - (total * 10/100)

    elif (forma == '3'):
        print("Você tem direito a 5% de desconto.")
        total = total - (total * 5/100)

    else:
        print("Digite um opção válida.")
    print("Valor com desconto: R${:.2f}".format(total))

elif (tipo == '2'):
    print("""Pagamento Á PRAZO, escolha a forma de pagamento:
        [ 1 ] 2x no cartão (preço normal)
        [ 2 ] 3x ou mais no cartão (20% de juros)""")
    forma = input('Escolha: ').strip()
    if (forma == '1'):
        print("Pagará o preço normal total.")
        total = total / 2

    elif (forma == '2'):
        print("Terá o acréscimo de 20% de juros.")
        total = total + (total * 20/100)

    else:
        print("Digite um opção válida.")
    print("Valor de cada parcela: R${:.2f}".format(total))
else:
    print("Digite um opção válida.")
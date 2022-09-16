# ler distancia em km e retornar valor da passagem

distancia = int(input('Qual à distância da viagem?  ').strip())

print("Para uma viagem de {}km.".format(distancia))

if (distancia > 0):
    if (distancia > 200):
        valor_pass = distancia * 0.50
        print("O valor da passagem será de R${:.2f}".format(valor_pass))
    else:
        valor_pass = distancia * 0.45
        print("O valor da passagem será de R${:.2f}".format(valor_pass))
else:
    print("A distância tem que ser maior que 0")
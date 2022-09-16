#DETECTOR DE PALINDROMO

"""
#MINHA MANEIRA
frase = input('Digite uma frase: ').strip().upper()
print("A frase: {}...".format(frase))

frase = frase.replace(' ', '')

for c in range(1, 0, -1):
    inverso = frase[len(frase)::-1]
    #print(inverso)

if inverso == frase:
    print("\n\33[33mÉ um PALÍNDROMO.")
else:
    print("\n\33[31mNÃO é um PALÍNDROMO.")
"""

#maneira da aula
"""frase = input('Digite uma frase: ').strip().upper()
print("A frase {}".format(frase))
palavras = frase.split()
junto = ''.join(palavras)
print(junto)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(inverso)
if inverso == junto:
    print("\n\33[33mÉ um PALÍNDROMO.")
else:
    print("\n\33[31mNÃO é um PALÍNDROMO.")"""

#FORMA MAIS SIMPLES

frase = input('Digite uma frase: ').strip().upper()
print("A frase {}".format(frase))
palavras = frase.split()
junto = ''.join(palavras)
print(junto)
inverso = junto[::-1]
print(inverso)

if inverso == junto:
    print("\n\33[33mÉ um PALÍNDROMO.")
else:
    print("\n\33[31mNÃO é um PALÍNDROMO.")

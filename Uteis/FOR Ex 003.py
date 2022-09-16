#Soma dos impares multiplos de 3 entre 1 e 500
s = 0
"""for c in range(1, 500):
    resto = c % 2
    if resto == 1:
       resto = c % 3
       if resto == 0:
            s = s + c
print("O somatório dos números ímpares multiplos de 3 é igual à {}".format(s))
"""

#ou
cont = 0 # se quiser mostrar quantos numeros foram somados
for c in range(1, 500+1, 2):
    resto = c % 3
    if resto == 0:
        cont = cont + 1 #cont += 1
        s = s + c #s += c
print("A soma dos números ímpares múltiplos de 3 é {} e foram somados {} números".format(s, cont))
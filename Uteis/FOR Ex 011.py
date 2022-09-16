#analisador completo
#minha forma
"""cont = 0
contf = 0
contf20 = 0
contm = 0
SOMAIDADE = 0
maior = 0
menor = 0

for c in range(1, 5):
    print("-=-"*5, end='')
    print("{}ª pessoa".format(c), end='')
    print("-=-" * 5)

    nome = input('Digite o nome: ').strip()
    idade = int(input('Digite a idade: ').strip())
    sexo = input('Digite o sexo[M/F]: ').strip().upper()

    cont += 1
    SOMAIDADE += idade #para achar a media soma a idade de todos


    #CONTAR PESSOAS DO SEXO F
    if sexo == 'F':
        contf += 1
        if idade <= 20:
            contf20 += 1
    else:
        contm += 1
        if c == 1:
            maior = idade
            menor = idade
        else:   #analisa qual a idade mais alta entre os homens
            if idade > maior:
                maior = idade
            if idade < menor:
                menor = idade

MEDIAIDADE = SOMAIDADE/cont
print("-=-"*10)
print("A média de idade do grupo é de {:.2f} anos.".format(MEDIAIDADE))
print("O homem mais velho do grupo tem {} anos".format(maior))
print("Ao todo são {} mulheres no grupo com menos de 20 anos.".format(contf20))
print("-=-"*10)"""

#forma da aula

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmaulher20 = 0

for p in range(1, 5):
    print("---------{}ª pessoa---------".format(p))
    nome = input('Digite o nome: ').strip()
    idade = int(input('Digite a idade: ').strip())
    sexo = input('Digite o sexo[M/F]: ').strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmaulher20 += 1
mediaidade = somaidade/4
print("A média de idade do grupo é de {} anos".format(mediaidade))
print("O homem mais velho tem {} e se chama {}".format(maioridadehomem, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(totmaulher20))


#Analise de dados de grupo/ cadastro
cont = 0
masc = 0
fem = 0
maior = 0
menor = 0
soma_idade = 0
nome_velho = ''
nome_novo = ''
while True:
    print("*-*"*12)
    print("\33[1;42mCADASTRE UMA PESSOA")
    print("\33[0m*-*"*12)
    nome = input('Digite o nome: ').strip()
    idade = int(input('Digite a idade: ').strip())
    sexo = input('Qual o sexo? [F/M]').strip()
    cont += 1
    soma_idade += idade
    print("---" * 12)
    continuar = input('Quer continuar? [S/N]').strip()
    print("---" * 12)
    if sexo in 'Mm':
        masc += 1
    elif sexo in 'Ff':
        fem += 1
    if cont == 1:
        maior = idade
        menor = idade
        nome_velho = nome
        nome_novo = nome
    elif cont > 1:
        if idade > maior:
            maior = idade
            nome_velho = nome
        elif idade < menor:
            menor = idade
            nome_novo = nome
    if continuar in 'Nn':
        break
media_idade = soma_idade / cont
print(f"\33[32mForam cadastradas {cont} pessoas.")
print(f"Dessa {cont} pessoas, {masc} são do sexo masculino e {fem} são do sexo feminino.")
print(f"A pessoa mais velha cadastrada possuí {maior} anos e se chama {nome_velho} e a mais ", end="")
print(f"nova possuí {menor} anos e se chama {nome_novo}, \na média de ", end="")
print(f"idade do grupo equivale à {round(media_idade, 3)} anos.")
